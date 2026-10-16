---json
{
  "id": "google_android_crie_aplica__es_para",
  "title": "Google_Android_crie_aplicações_para",
  "categoria": "03-linguagens",
  "subcategoria": "go",
  "resumo": "**Arquivo Original:** `Google_Android_crie_aplicações_para.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "android",
    "aplica",
    "crie",
    "google",
    "linguagens",
    "para"
  ],
  "perguntas_tipo": [
    "Como utilizar Google_Android_crie_aplicações_para?",
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

# Google_Android_crie_aplicações_para

> **Arquivo Original:** `Google_Android_crie_aplicações_para.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 3

Capítulo1
Construasuaprimeiraaplicaç ão
Comopassardotempoostelefonescelularesforamevoluindo,ganhandocadavez
maisrecursosesetornandoumitemquaseindispensávelnavidadaspessoas.Mas
nãofoiapenasissoquemudou.Tambémhouveumamudan çasignificativaparanós,
osdesenvolvedoresdesoftware.
Antes,omercadodedesenvolvimentoparacelulareserapraticamenterestrito
aosfabricanteseoperadorasquecontrolavamacriaç ãoeinclusãodosaplicativosem
seusaparelhos.Aliberaç ão,porpartedosfabricantes,deumkitdedesenvolvimento
desoftware(SDK)parasuasplataformaseacriaç ãodelojasparaadistribuiç ãode
aplicativosviabilizouaaberturadestemercadoparapraticamentequalquerempresa
oudesenvolvedor,criandoassimnovasoportunidadesdenegócio.
AplataformaAndroiddesfrutahojedeumpapeldedestaquenomercado,tanto
pelaquantidadesignificativadedispositivosproduzidoscomotambémporofere-
cerumaAPIrica,disponibilizandofácilacessoaváriosrecursosdehardware,tais
comoWi-FieGPS,alémdeboasferramentasparaodesenvolvedor. Afacilidade
dedesenvolverutilizandoumalinguagemdeprogramaç ão(Java)bastantedissemi-

## Página 4

CasadoCódigo
nada,asimplicidadeebaixocustoparaapublicaç ãodeaplicativosnalojaGoogle
PlayeaquantidadededispositivosAndroidemusonomundosófazemaumentar
apopularidadedaplataforma.
SegundoorelatóriodoInternationalDataCorporation(IDC)publicadoem
maiode2012,oAndroidpossui59%domercadodesmartphonesesomaaquantia
de89,9milhõesdeaparelhosdistribuídosapenasnoprimeirotrimestredesteano
(2013),emtodoomundo. Emsegundolugar,apareceoiOSqueéosistemaope-
racionaldoAppleiPhone. Ográfico1.1demonstraaparticipaç ãonomercadodos
principaissistemasoperacionaiseaquantidadedeaparelhosdistribuídos.
Figura1.1:Participaçãonomercado.Fonte:IDC
OIDCtambémprevêqueem2016oAndroidaindapossuiráamaiorfatiado
mercado,com52,9%.AdisputapelosegundolugarseráacirradaentreiOSeWin-
dowsPhone7.Ográfico 1.2ilustraaprevisãorealizadapeloIDC.
2

## Página 5

CasadoCódigo Capítulo1. Construasuaprimeiraaplicação
Figura1.2:Previsãodomercadopara2016.Fonte:IDC
Jánomercadodetablets,oiPaddetémotronocom68%enquantooGoogle
apostaemseuprimeirotablet,oNexus7aopre ço199dólares,paraganharterreno
tentandorepetirosucessodoAmazonKindleFirequetambémutilizaAndroid.
1.1 Conheça o Android
Desenvolvidoespecialmenteparadispositivosmóveiscomoaparelhoscelulareseta-
blets,oAndroidéumaplataformacompostadeumsistemaoperacional, middlewa-
reseumconjuntodeaplicativosprincipaiscomoosContatos,NavegadordeInternet
eoTelefonepropriamentedito. Alémdisso,existeoAndroidSDKqueéumcon-
juntodeferramentaseAPIsparaodesenvolvimentodeaplicativosparaaplataforma,
utilizandoalinguagemJava. Nodecorrerdolivro,vamosabordaremdetalhesos
componentesexistentesnoAndroidalémdemostrarcomointegrá-losparacriar
aplicaçõesricasemfuncionalidadesecomumausabilidadeagradável.
BaseadonoLinux,osistemaoperacionalAndroidteveseudesenvolvimento
iniciadoem2003pelaempresaAndroidInc. Em2005,aempresafoiadquirida
peloGoogle,quehojelideraodesenvolvimentodoAndroid. Ummarcoimpor-
tantedestatrajetóriaaconteceuem2007,comacriaç ãodaOpenHandsetAlliance
(http://www.openhandsetalliance.com/),queéumaassociaç ãodeempresasdesoft-
ware,hardwareetelecomunicações,cujamissãoédesenvolverumaplataformapara
dispositivosmóveisquesejacompleta,abertaegratuita.Tambémem2007ocorreu
3

## Página 6

1.1. ConheçaoAndroid CasadoCódigo
olan çamentodaversãobetadoprimeiroSDKparaAndroid!Apósdiversasversões
emelhorias,emjunhode2012foianunciadooAndroid4.1,codinome Jelly Bean.
Um pouco mais de história
QuersabermaissobreahistóriadoAndroid,suasversões,eevolu-
ções? Entãovisite http://www.xcubelabs.com/the-android-story.phpe
http://www.theverge.com/2011/12/7/2585779/android-history
Nestaúltimaversão,ainterfacegráficaestámaisrefinadaeevoluída,novasfun-
cionalidadescomo widgetsredimensionáveis,possibilidadedeusarpastasparaorga-
nizarasáreasdetrabalhoenovasaçõesquepodemserexecutadassemdesbloquear
ateladoaparelhoforamadicionadas,incluindoacessarrapidamenteacâmerapara
capturaraqueleflagra.Eporfalarnisto,oaplicativodacâmerarecebeuaten çãoes-
pecialeagoracontacomfotospanorâmicasquepodemsertiradassimplesmente
movendooaparelhodeumladoaoutroemaisainda,contatambémcomumpode-
rosoeditordeimagens,dentreoutrasváriasfuncionalidades.
Parafacilitaracomunicaç ão,agoraépossívelconectardoisdispositivosdire-
tamenteatravésdoWi-FiDirecteaintroduç ãodo Bluetooth HDP(Health Device
Profile)permiteaconexãoentreoseuaparelhoedispositivosvoltadosparaasaúde
ebem-estar.Jáonovorecurso Android Beam,utilizandotecnologiaNFC(Near Field
Communication),permitecompartilharaplicativos,contatos,vídeosemúsicas,livre
dequalquertipoconfiguraç ão,comapenasumtoque.Outrafacilidadeadicionada
foiodesbloqueiodoaparelhoatravésdoreconhecimentodafacedousuário. Em
umateladeconfiguraç ão,ousuáriopreviamenteregistraoseurostoedepois,para
desbloquearoaparelho,bastaposicionaracâmerafrontalquefaráoreconhecimento
eliberaráoacesso.Muitolegal,nãoémesmo?
Android é código aberto!
OAndroidécódigoabertoedistribuídosoblicen çaApache2.0,o
quequerdizerquevocêtemacessoaoscódigos-fonteetambémpode
contribuircomoprojeto!Saibamaisem http://source.android.com
4

## Página 7

CasadoCódigo Capítulo1. Construasuaprimeiraaplicação
1.2 Configure o ambiente para desenvolvimento
Antesdecriaranossaprimeiraaplicaç ãoAndroid,énecessáriobaixareinstalaro
AndroidSDKqueestádisponívelem http://developer.android.com/sdk.Escolhao
pacotemaisadequadodeacordocomoseusistemaoperacional,faç aodownloade
instale.Umdetalheimportanteéqueo Java Development Kit(JDK)éumrequisito
necessário,portanto,sevocêaindanãoopossui,faç aodownloadesigaasinstru-
çõesdeinstalaç ãoem http://www.oracle.com/technetwork/java/javase/downloads/
index.html.
Figura1.3:PáginadedownloaddoAndroidSDK
Nestemomentooquetemosinstaladosãoapenasasferramentasquefazemparte
doAndroidSDK.PrecisaremosagoraselecionarebaixarasAPIsparaasquaispre-
tendemosdesenvolvernossasaplicações.Porenquanto,utilizaremosaversão2.3.3
(API10)efuturamentevamosusarrecursosnovosdaplataformaefaremosatran-
siçãoentreasversões.
Abrao Android SDK Manager. Oaplicativobuscaráinformaçõessobreasver-
sõesdisponíveisetraráselecionadaaversãomaisrecente. Nãocedaàtentaç ãode
baixartudooqueestádisponível,poisotempodedownloadprovavelmentedemo-
5

## Página 8

1.2. Configureoambienteparadesenvolvimento CasadoCódigo
rariamaisdoqueotempodeleituradestelivro.Desmarqueoquevierselecionadoe
escolhaapenasaop ção SDK Platform doitem Android 2.3.3,comodemons-
traaimagemabaixo:
Figura1.4:SDKManager
TambémprecisaremosdeumaIDEparaauxiliarodesenvolvimento.Aolongo
destelivroutilizaremosoEclipsecomumpluginespecíficoqueauxilianodesenvol-
vimentoparaAndroid.OEclipsepossuidiferentesdistribuições,sendoquealgumas
sãoindicadasparadesenvolvimentodeaplicaçõesparaAndroid.Sãoelas:
1) EclipseClassic
2) EclipseIDEforJavaDevelopers
3) EclipseIDEforJavaEEDevelopers
Essasversõesseencontramdisponíveisparadownloadem http://www.eclipse.
org/downloads.
6

## Página 9

CasadoCódigo Capítulo1. Construasuaprimeiraaplicação
Sevocêaindanãotemumapreferênciaporalgumadistribuição,umaboaescolha
éaEclipseClassic.Ainstalaç ãodaIDEébastantesimples,bastandodescompactá-
laemumdiretóriodesuapreferência.Jáestamosquaseprontos!Partiremosagora
paraainstalaç ãodopluginADT(Android Development T ools)quefornecerátodas
asfacilidadesparaacriaç ãoecodificaç ãodeumprojetoAndroidnoEclipse.
AinstalaçãodopluginéfeitaapartirdogerenciadordeatualizaçõesdoEclipse.
Portanto,inicieaIDEesigaasinstruçõesaseguir:
1) VáatéomenuHelp>InstallNewSoftware...
2) Cliquenobotãoadd,paraadicionarumnovorepositório
3) Najanelaqueseráapresentada,escolhaumnomeparaorepositório,ADTPlu-
ginporexemplo,einformeaseguinteURL https://dl-ssl.google.com/android/
eclipse/
4) CliqueemOKparafinalizar
5) Umalistagemseráapresentada,marqueaop çãoDeveloperTools parainstalar
todosositensnecessários
6) CliqueemNextparaprosseguircomainstalaç ão
7) Leiaeaceiteostermosdaslicen çasecliqueem finish
8) ReinicieoEclipseconformesugeridoparaconcluirainstalaç ão
Figura1.5:MenuHelp
7

## Página 10

1.2. Configureoambienteparadesenvolvimento CasadoCódigo
Figura1.6:Adicionandoumnovorepositório
8

## Página 11

CasadoCódigo Capítulo1. Construasuaprimeiraaplicação
Figura1.7:Escolhendooqueseráinstalado
9

## Página 12

1.2. Configureoambienteparadesenvolvimento CasadoCódigo
Figura1.8:Aceitandoostermosdalicen ça
Figura1.9:ReiniciandooEclipse
Apósotérminodainstalaç ão,énecessárioconfiguraropluginADTparaen-
contraroAndroidSDKinstaladopreviamente. Paraisto,váatéomenu Window
10

## Página 13

CasadoCódigo Capítulo1. Construasuaprimeiraaplicação
> Preferences(paraquemusaMac: Eclipse> Preferences),noladoes-
querdoselecioneoitem Android.Porfim,nopainelqueseráapresentadoinforme
olocalemqueoAndroidSDKestáinstalado.
Figura1.10:ConfigurandooSDK
1.3 Escrev a oHelloWorld!
Agora que temos o ambiente de desenvolvimento preparado, estamos prontos
paraescrevernossaprimeiraaplicaç ãoAndroid! Comoumaprimeiraexperiên-
ciaemumanovaplataforma,vamosdesenvolverumclássico Hello World. No
Eclipse,devemoscriarumnovoprojetoAndroid,atravésdomenu File> New
> Project....Nanovajanelaqueseráapresentada,selecioneaop ção Android
Application Project,comomostraafigura 1.11.
11

## Página 14

1.3. EscrevaoHelloWorld! CasadoCódigo
Figura1.11:CriandoumnovoprojetoAndroid
Natelaseguinte,escolhaumnomeparaoseuprojeto,nonossocaso,vamos
chamarde HelloAndroid.Éimportanteescolheronomedaaplicaç ãoetambém
dopacotecomcautela,poisessesdoisnomesserãoutilizadosparaidentificarsua
aplicaçãoquandoforfeitaumapublicaç ãonoGooglePlay. Paranossaaplicaç ão,
escolhemosonome HelloAndroid(nocaso,mesmonomedoprojeto)eopacote
br.com.casadocodigo.helloandroid.
Aop ção Build SDK permiteselecionarqualéaversãodoAndroidqueserá
utilizadapornossaaplicaç ão.Comoapenasaversão2.3.3(API10)foiinstalada,esta
éaúnicaopçãodisponívelnomomento.Aop ção Minimum Required SDK indica
qualéaversãomínimaexigidaparaexecutaroaplicativo.Vamosdeixarcomoestá.
Aimagem 1.12mostracomoficouaconfiguraç ãodoprojeto.
12

## Página 15

CasadoCódigo Capítulo1. Construasuaprimeiraaplicação
Figura1.12:Escolhendoumnomeepacoteparaaaplicaç ão
Prossigaparaopróximopassoclicandoem Next. Umatelacomomostraa
figura1.13seráapresentadaparaquevocêpossacustomizaroíconedoaplicativose
desejar. Selecionenovamenteaop ção Next. Apróximatelasugereacriaç ãode
uma BlankActivity,conformedemonstraaimagem 1.14.Nenhumaalteraçãoé
necessárianestatela.
13

## Página 16

1.3. EscrevaoHelloWorld! CasadoCódigo
Figura1.13:Personalizandooíconedaaplicaç ão
14

## Página 17

CasadoCódigo Capítulo1. Construasuaprimeiraaplicação
Figura1.14:CriandoumaActivity
Aoselecionar Next,vamosparaoúltimopasso,queconsisteemdefinironome
da Activityetambémdolayoutqueseráutilizadoporela.Mantenhaasinforma-
çõesdaformaqueestão,assimcomomostraafigura 1.15.Parafinalizaracriaç ãodo
projeto,cliqueem Finish.
15

## Página 18

1.3. EscrevaoHelloWorld! CasadoCódigo
Figura1.15:DefinindoonomedaActivity
ComaajudadoADT,umnovoprojetofoicriadocomasconfiguraçõesescolhi-
das.Esseprojetojáestácomtudoqueénecessárioparaserexecutado.Entraremos
emmaisdetalhesdepois,agoraoquequeremosveréaaplicaç ãofuncionando,certo?
Selecioneomenu Run> Run,umacaixadediálogo Run as vaiaparecer.Escolha
aop çãoAndroidApplicationecliqueem OK,comonafigura 1.16:
16

## Página 19

CasadoCódigo Capítulo1. Construasuaprimeiraaplicação
Figura1.16:MenuRun
Ops!Algumproblemaaconteceu.Surgiuumacaixadediálogodizendoquenão
temosnenhumdispositivocompatívelinstalado.
Figura1.17:Nenhumdispositivovirtualconfigurado
Defato,nãocriamosnenhumdispositivovirtual(Android Virtual Device, A VD)
17

## Página 20

1.3. EscrevaoHelloWorld! CasadoCódigo
pararodarnossaaplicaç ão!Vamosaproveitarefazerissoagora,respondendo Yesà
perguntasequeremoscriarumdispositivo.Acaixadediálogoéfechadaeoaplica-
tivo Android Virtual Device Managerseráiniciado.
Natelaapresentada,cliqueem Newparacriarumnovodispositivovirtual.Faç a
aconfiguraçãoconformenafigura 1.18.
Figura1.18:Criandoumnovodispositivovirtual
Agoraésóexecutaroprojetonovamente.Comojáexisteum A VDcriadopara
aplataformaalvodonossoaplicativo,oemuladorseráiniciadoautomaticamente.
Ainicializaçãodoemuladorpodedemorarumpouco,aproveiteparabuscaruma
xícaradecafé.Quandoretornar,oaplicativojádevetersidoiniciadonoemuladore
umatelasemelhanteaestaserámostrada:
18

## Página 21

CasadoCódigo Capítulo1. Construasuaprimeiraaplicação
Figura1.19:HelloAndroid!
Dica
Nãoénecessárioreiniciaroemuladorparatestarumanovaversão,
entãoadicaémantê-losempreabertoparaeconomizarotempodeini-
cialização.
1.4 Conheça a estrutura do projeto
Játemosaprimeiraversãodonosso Hello World. Ébemverdadequeaindanão
fizemosnenhumacodificaç ão,entãovamosanalisaraestruturadoprojetoetudo
aquiloquefoigeradoautomaticamenteparaqueessamágicaacontecesse.Nafigura
19

## Página 22

1.4. Conheçaaestruturadoprojeto CasadoCódigo
1.20,podemosidentificarcincopastasprincipais( src, gen, assets, bin, libs
e res)alémdeumareferênciaparaabibliotecaAndroidqueestásendoutilizada:
Figura1.20:Estruturadoprojeto
1) src-pastadedicadaaoarmazenamentosdoscódigos-fontedoprojetoeserá
ondecolocaremosasclassesJavaquecriaremosemnossaaplicaç ão.Repareque
jáexisteuma MainActivity.javaquefoicriadaautomaticamentequando
criamosoprojeto;
2) res-dedicadoaoarmazenamentoderecursos(arquivosdelayout,imagens,ani-
maçõesexmlcontendovalorescomo strings, arraysetc.),acessíveisatravés
daclasse R;
3) assets-diretórioparaoarmazenamentodearquivosdiversosutilizadospor
suaaplicação.Diferentementedosrecursosarmazenadosnapasta res,estessão
20

## Página 23

CasadoCódigo Capítulo1. Construasuaprimeiraaplicação
acessíveisapenasprogramaticamente;
4) gen-armazenacódigosgeradosautomaticamentepeloplugin,comoaclasse R
quemantémreferênciasparadiversostiposderecursosutilizadosnaaplicaç ão;
5) libs-pastaparaarmazenarbibliotecasdeterceirosqueserãoutilizadaspela
aplicação;
6) bin-localutilizadopelosprocessosdecompilaç ãoeempacotamentoparaman-
terarquivostemporáriosecódigoscompilados.
Nodiretórioraizdoprojetotambémexistemalgunsarquivos,sendoumdeles,
o AndroidManifest.xml,obrigatórioparatodaaplicaç ãoAndroid.Essearquivo
contéminformaçõesessenciaissobreasuaaplicaç ãoesobreoqueénecessáriopara
executá-la,incluindoaversãomínimadoAndroid. Onomedopacoteescolhido
duranteacriaç ãodoprojeto,porexemplo,éarmazenadoláparaservircomoiden-
tificadorúnicodasuaaplicaç ão.
Omanifestotambémdescreveoscomponentes(activities, services, content pro-
viderse broadcast receivers)quefazempartedaaplicaç ão,possibilitandoqueosis-
temaoperacionalAndroidsejacapazdeidentificá-losedeterminarquandoserão
executados. Duranteolivro,vamosaprendercomotrabalharcomessesdiferentes
componentes.Nocódigoaseguir,a activity MainActivityéquemrepresenta
ocomponentequeéiniciadoquandoexecutamosaaplicaç ão.
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
package="br.com.casadocodigo.helloandroid"
android:versionCode="1"
android:versionName="1.0" >
<uses-sdk
android:minSdkVersion="8"
android:targetSdkVersion="15" />
<application
android:icon="@drawable/ic_launcher"
android:label="@string/app_name"
android:theme="@style/AppTheme" >
<activity
android:name=".MainActivity"
android:label="@string/title_activity_main" >
21

## Página 24

1.4. Conheçaaestruturadoprojeto CasadoCódigo
<intent-filter>
<action android:name="android.intent.action.MAIN" />
<category
android:name="android.intent.category.LAUNCHER" />
</intent-filter>
</activity>
</application>
</manifest>
As activitiessãocomponentesdaplataformaAndroid,capazesdeapresentaruma
telaparainteragircomosusuários. Atravésdelaspodemostirarumafoto,enviar
umemail,visualizarumaimagemenavegarnaInternet. Geralmenteumaaplica-
çãoécompostaporvárias activities,sendoumadelasa activityprincipalqueé
executadaquandoainiciamos. Ocódigoaseguirdemonstraaatividadeprincipal
( MainActivity.java)donossoprojetoHelloWorldquefoicriadaautomatica-
mentepeloADTplugin:
1 public class MainActivity extends Activity {
2
3 @Override
4 public void onCreate(Bundle savedInstanceState ) {
5 super.onCreate(savedInstanceState);
6 setContentView(R.layout.activity_main);
7 }
8
9 @Override
10 public boolean onCreateOptionsMenu(Menu menu) {
11 getMenuInflater().inflate(R.menu.activity_main, menu);
12 return true;
13 }
14 }
Para criar uma atividade, basta fazer com que nossa classe estenda a
classe Activity do Android, como pode ser visto na linha 1. Já na li-
nha 6, passamos para o métodosetContentViewo identificador do layout,
R.layout.activity_main,quedevesercarregadoparaconstruirainterfacegrá-
ficadanossa Activity.Ébastantecomumetambémrecomendadoqueasinfor-
maçõesreferentesalayoutseinterfacesgráficasestejamexternalizadasemarquivos
22

## Página 25

CasadoCódigo Capítulo1. Construasuaprimeiraaplicação
XML,separadosdocódigodaaplicaç ão.Essaseoutrasboaspráticasnósaprendere-
mosnodecorrerdolivro.
Vamosprosseguirverificandooarquivo activity_main.xml,queseencon-
tranodiretório res/layout/doprojeto.
1 <RelativeLayout
2 xmlns:android="http://schemas.android.com/apk/res/android"
3 xmlns:tools="http://schemas.android.com/tools"
4 android:layout_width="match_parent"
5 android:layout_height="match_parent" >
6
7 <TextView
8 android:layout_width="wrap_content"
9 android:layout_height="wrap_content"
10 android:layout_centerHorizontal="true"
11 android:layout_centerVertical="true"
12 android:padding="@dimen/padding_medium"
13 android:text="@string/hello_world"
14 tools:context=".MainActivity" />
15
16 </RelativeLayout>
Recursos gráficos do ADT
QuandoabrimosumarquivodelayoutnoEclipsecomoADTins-
talado,eleéapresentadoemumvisualizadordelayouts(abaGraphical
Layout),noqualépossívelverificarcomoolayoutestáficandoalémde
contarcomop çõesparaconfigurardiversosatributos.Tambémépossí-
velutilizaresserecursoparaadicionarelementosdelayoutedeentrada
dedados.ParaveroXMLresultanteselecioneaoutraabaquepossuio
nomedoarquivo.Paraconhecermaissobreosrecursosdisponíveisno
ADTvisite http://developer.android.com/tools/help/adt.html.
Neste arquivo de definição de layout temos dois elementos declarados, o
RelativeLayouteo TextView,comseusrespectivosatributos.Comoonome
sugere,o RelativeLayout(linha1)éumelementoparaorganizaç ãodolayoutda
tela,permitindoconfigurarasuaalturaelargura.
23

## Página 26

1.4. Conheçaaestruturadoprojeto CasadoCódigo
Jáo TextViewéum widgetutilizadoparaapresentarnatelaumainforma-
çãotextual. Ovaloraserexibidoporesteelementoestáespecificadoatravésdo
atributo text. Repare que na linha 13 o valor queTextViewdeve exibir é
@string/hello_world. Aquitemosnovamenteumcasonoqualaexternaliza-
çãoérecomendadaprincipalmenteparafacilitarainternacionalizaç ãodaaplicaç ão,
suportandováriosidiomasdiferenteseparaatémesmoreaproveitarmensagens.
O valor que será utilizado no TextView será na verdade o con-
teúdo da string que possui o identificadorhello_world. No arquivo
res/values/strings.xmlépossívelobservarcomoissofoidefinido:
1 <resources>
2 <string name="app_name">HelloAndroid</string>
3 <string name="hello_world">Hello world!</string>
4 <string name="menu_settings">Settings</string>
5 <string name="title_activity_main">MainActivity</string>
6 </resources>
Nalinha3,declaramosuma stringcomonome hello_worldcujovaloré
“HelloWorld!”.Porconvenção,oarquivo strings.xmléondedefinimosrecursos
dotipo string,ouseja,textosquequeremosexibirdealgumamaneiraemnossa
aplicação. Parafinalizar,altereovalorda string hello_world para "Hello
Android!"eexecuteaaplicaç ãonovamente.Oresultadodestaalteraç ãopodeser
vistonaimagem 1.21
Dica:Acessando o AVDM anager e SDKM anager pelo
Eclipse
Apósainstalaç ãoeconfiguraç ãodoADT,atravésdomenu Window
épossívelfazerumacessorápidoaoAVDManagereSDKManagerpara
baixarnovasversõesdoAndroidetambémcriarnovosdispositivosvir-
tuais!
24

## Página 27

CasadoCódigo Capítulo1. Construasuaprimeiraaplicação
Figura1.21:HelloAndroid
1.5 HelloWorld2.0
Paramelhoraranossaaplicaç ão,iremosincluirmaisalgumascoisaseaproveitar
paraentenderalgunspontosfundamentaisdodesenvolvimentoAndroid.Emnossa
versãomelhoradadoHelloWorld,ousuárioinformaráseunomeemumacaixade
texto,pressionaráumbotãoeaaplicaç ãoapresentaráumasaudaçãopersonalizada.
Aaplicaçãoficarácomaseguinteaparência:
25

## Página 28

1.5. HelloWorld2.0 CasadoCódigo
Figura1.22:Versãomelhorada
Podemosmodificarolayout activity_main.xmljáexistente,paraincluir
umcampoondeousuárioiráinformaroseunome. Essecampopodesercriado
utilizandoum widgetdotipo EditText,noqualpodemosinclusiveindicarqueo
mesmoreceberáofocodaaplicaç ão:
<EditText
android:id="@+id/nomeEditText"
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:inputType="textPersonName" >
<requestFocus />
</EditText>
Alémdisso,tambémteremosqueincluirumbotão,atravésdo widget Button:
<Button
android:id="@+id/saudacaoButton"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_gravity="center"
android:text="@string/surpreenda_me" />
Nestemomento,parafacilitaracriaç ãodolayoutcomestesnovoselementos,ire-
mossubstituiro RelativeLayoutporum LinearLayoutquepermitecolocar
um widgetporlinha.Comestesnovoselementospodemosmontaratelacompleta
donovo Hello Worldqueficarácomoocódigoaseguir:
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
26

## Página 29

CasadoCódigo Capítulo1. Construasuaprimeiraaplicação
android:layout_width="match_parent"
android:layout_height="match_parent"
android:orientation="vertical" >
<TextView
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:text="@string/titulo" />
<EditText
android:id="@+id/nomeEditText"
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:inputType="textPersonName" >
<requestFocus />
</EditText>
<Button
android:id="@+id/saudacaoButton"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_gravity="center"
android:text="@string/surpreenda_me" />
<TextView
android:id="@+id/saudacaoTextView"
android:layout_width="match_parent"
android:layout_height="wrap_content" />
</LinearLayout>
Nositensrecémadicionados,reparequecolocamosumatributo android:id
queéimportante, poisposteriormenteprecisaremosreferenciaremanipulares-
sescomponentesvisuais. Tambéménecessáriocriaras stringsqueserãouti-
lizadascomootítulo,orótulodobotãoetambémumasaudaç ão. Nossoarquivo
strings.xmldeveráficarassim:
<resources>
<string name="app_name">HelloAndroid</string>
<string name="hello_world">Hello Android!</string>
27

## Página 30

1.5. HelloWorld2.0 CasadoCódigo
<string name="menu_settings">Settings</string>
<string name="title_activity_main">MainActivity</string>
<string name="titulo">Informe seu nome</string>
<string name="surpreenda_me">Surpreenda-me</string>
<string name="saudacao">Olá</string>
</resources>
Aoexecutarmosaaplicaç ãonovamentejáperceberemosasmudan çasrealizadas
eoresultadoseráigualàimagem 1.22. Comoaindanãoprogramamosnenhuma
açãoparaobotãodisponívelnatela,aopressioná-lo,nadadediferenteacontece.
Para obter o resultado esperado, criaremos um método na nossa
MainActivity que responderá a esta ação apresentando ao usuário uma
saudaçãopersonalizada.Entãovamosconfigurarnossobotãoparaquequandoele
sejapressionadoummétodosejainvocado.Paraisso,utilizaremoso onClick:
<Button
android:id="@+id/saudacaoButton"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_gravity="center"
android:text="@string/surpreenda_me"
android:onClick="surpreenderUsuario"/>
Informamos que o método a ser acionado após o clique do botão é o
surpreenderUsuario,atravésdapropriedade onClick.Estemétodo devene-
cessariamenteserpúblicoerecebercomoparâmetroumobjetodotipo Viewqueé
umareferênciadobotãoquefoipressionado:
public void surpreenderUsuario(View v){
}
Nesse método, precisamos modificar o conteúdo do widget
saudacaoTextViewparaqueelemostreoconteúdoinformadono EditText.
Paraisso,vamosprecisarqueaclasse MainActivitypossuareferênciaparaesses
elementos.Vamoscome çardeclarandoatributosparao EditTexteo TextView:
public class HelloAndroidActivity extends Activity {
private EditText nomeEditText;
private TextView saudacaoTextView;
28

## Página 31

CasadoCódigo Capítulo1. Construasuaprimeiraaplicação
@Override
public void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.main);
}
public void surpreenderUsuario(View v) { }
//demais códigos existentes
}
Nométodo onCreate,temosqueconseguirasreferênciasparaoscomponen-
tes.Podemosfazerissoatravésdométodo findViewById:
@Override
public void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.activity_main);
this.nomeEditText = (EditText) findViewById(R.id.nomeEditText);
this.saudacaoTextView = (TextView)
findViewById(R.id.saudacaoTextView);
}
Agoraquejátemosasreferênciasparaosobjetos,podemosobterovalordi-
gitadopelousuário,queestáarmazenadono EditTexteatribuí-locomocon-
teúdodo TextView. Pararealizarestaoperaç ão,bastaimplementarométodo
surpreenderUsuariodessaforma:
public void surpreenderUsuario(View v) {
Editable texto = this.nomeEditText.getText();
this.saudacaoTextView.setText(texto);
}
Porfim,vamosadicionara string saudacao,queestádefinidanoarquivo
strings.xml, paracomporamensagemfinalparaousuário. Paraisso, basta
recuperá-laatravésdométodogetResources:
String saudacao = getResources().getString(R.string.saudacao);
Podemosfazeraleituradessasaudaç ãonométodo onCreateeusaramensa-
gemnanossaimplementaç ãode surpreenderUsuario,comonocódigoaseguir:
29

## Página 32

1.5. HelloWorld2.0 CasadoCódigo
public class MainActivity extends Activity {
private EditText nomeEditText;
private TextView saudacaoTextView;
private String saudacao;
@Override
public void onCreate(Bundle savedInstanceState ) {
super.onCreate(savedInstanceState);
setContentView(R.layout.activity_main);
this.nomeEditText = (EditText) findViewById(R.id.nomeEditText);
this.saudacaoTextView =
(TextView) findViewById(R.id.saudacaoTextView);
this.saudacao = getResources().getString(R.string.saudacao);
}
public void surpreenderUsuario(View v) {
Editable texto = this.nomeEditText.getText();
String msg = saudacao + " " + texto.toString();
this.saudacaoTextView.setText(msg);
}
//demais códigos existentes
}
Agora,podemosexecutaressaaplicaç ão,queserásimilaràfigura 1.23
Figura1.23:HelloWorld2.0
30

## Página 33

CasadoCódigo Capítulo1. Construasuaprimeiraaplicação
1.6 Conclusão
NestecapítuloaprendemosumpoucodahistóriadoAndroidesuasversõeseti-
vemosoprimeirocontatocomoAndroidSDKecomaEclipseIDE.Criamosum
projetodeexemplo,buscamosentenderseusdetalheseorganizaç ão,alémdefazer
modificaçõesnocódigoelayoutparatermosnossaprimeiraexperiência.Nocapí-
tuloseguinteabordaremositensessenciaisparaodesenvolvimentoAndroid.
31

## Página 35

Capítulo2
Entendaofuncionamentodo
Android
ApósdesenvolvernossoprimeiroprojetonaplataformaAndroid,éimportanteco-
nhecerumpoucomaisdoselementosqueacompõeetambémdofuncionamento
básicodoAndroid.Estecapítuloapresentacomoasaplicaçõessãogeradaseexecu-
tadas,quaissãooscomponentesdeaplicaç ãoexistentesnaplataforma,comoelesse
comunicametambémcomooselementosdeinterfacegráficaestãoorganizados.
2.1 A execução das aplicações
AsaplicaçõesimplementadasutilizandoalinguagemJavasãoexecutadasatravésde
umamáquinavirtual,baseadaemregistradoreseotimizadaparaconsumirpouca
memória,chamada Dalvik. AocontráriodamáquinavirtualJavaqueexecuta by-
tecodes,aDalvikutilizaarquivosnoformato .dexgeradosapartirdeclassesJava
compiladas.Estaconversãoéfeitapelaferramenta dxqueacompanhaoAndroid

## Página 36

2.1. Aexecuçãodasaplicações CasadoCódigo
SDK.
Basicamente,oqueéfeitoéoagrupamentodeinformaçõesduplicadasquese
encontramespalhadasemdiversosarquivos .classemumarquivo .dex,com
tamanhomenordoqueosarquivosqueooriginaram.O dxtambémfazaconversão
de bytecodesparaumconjuntodeinstruçõesespecíficodamáquinavirtualDalvik.
Depoisdecriado,oarquivo .dexetodososrecursosutilizadosnaaplicaç ão,
comoimagenseícones,sãoadicionadosemumarquivo .apk,queéoaplicativo
propriamentedito,capazdeserinstaladoemumdispositivo.Estesarquivosseen-
contramnapasta bindoprojeto.
Épossíveldistribuirsuaaplicaç ãoparaoutraspessoasapenasfornecendooar-
quivo .apk.Noentanto,paracolocá-lanaloja Google Playalgunsoutrospassossão
necessários,osquaisserãodetalhadosemoutromomento.Afigura 2.1demonstrao
processodegeraç ãodoaplicativo.
Figura2.1:Processodegeraç ãodoaplicativo
NosistemaoperacionalAndroid,paracadaaplicaç ãoéatribuídoumusuário
únicodesistemaeapenasesteusuáriorecebepermissõesparaacessarseusarquivos.
Alémdisso,porpadrão,cadaaplicaç ãoéexecutadaemumprocessopróprio,que
possuitambémsuaprópriainstânciadamáquinavirtualDalvik.Sendoassim,elaé
executadadeformaseguraeisoladadasdemais.
Nestecontexto,umaaplicaç ãonãopodeacessararquivosdeoutraetampouco
acessardiretamenterecursosdosistemaoperacionalcomoalistadecontatos,câ-
mera,gpserede,semqueousuárioexplicitamenteautorizeoacessoduranteains-
talaçãodela.Diantedessasrestriçõesdeseguran ça,comotiramosproveitodetoda
ainfraestruturadoAndroidetambémdeaplicativosdeterceirosparaincrementar
asfuncionalidadesdanossaaplicaç ão,incluindoporexemplo,umrecursodecaptu-
rarfotosevídeosecompartilharviae-mail?Esseéjustamenteopontoquevamos
abordarnapróximase ção.
34

## Página 37

CasadoCódigo Capítulo2. EntendaofuncionamentodoAndroid
2.2 Conheça as Intents e Intent Filters
As Intentsgeralmentesãocriadasapartirdeaçõesdousuárioerepresentama
intençãodeserealizaralgo,comoiniciaroaplicativodecorreioeletrônicodoAn-
droidouiniciarareproduç ãodeumamúsica. Formalmente,as Intentspodem
serdefinidascomomensagensenviadasporumcomponentedasuaaplicaç ão(uma
activity,porexemplo)paraoAndroid,informandoa intençãodeinicializaroutro
componentedamesmaaplicaç ãooudeoutra. Aimagem 2.2demonstraasop ções
apresentadaspeloAndroidquecorrespondemàsaplicaçõesquesãocapazesdetra-
tarainten çãoinformadapelousuário.Nesteexemplo,desejou-secompartilharum
textoselecionado.
Figura2.2:Aplicaçõesquepodemresponderàinten çãodecompartilhar
35

## Página 38

2.2. ConheçaasIntentseIntentFilters CasadoCódigo
Esteéumrecurso-chavenoAndroidpoiséatravésdelequepodemosfazercom
queasaplicaçõescolaborementresi,disponibilizandofuncionalidadesquepodem
serreutilizadas,semanecessidadedeimportarcódigosoudependênciasparaden-
trodasuaaplicaç ão. Atravésde Intentsépossíveliniciarnovas activities,
comofazerumabuscaeselecionarumcontatodotelefone,abriraaplicaç ãodema-
pascomascoordenadasdelocalizaç ãodoGPS,abrirumapáginadaweb,tirarfotos
utilizandoacâmeraetc.,apenasreaproveitandofuncionalidadesjáexistentes,dispo-
nibilizadaspelosaplicativosinstaladosnoaparelho.
Alémdisso,aplicativosdeterceiros,assimcomoosnossos,podemdisponibilizar
novasfuncionalidadesacessíveisvia Intents.Existem,porexemplo,aplicativosde
leituradecódigosdebarraquepodemserchamadospelasuaaplicaç ãoparalê-los
utilizandoacâmeradoaparelhoedevolveroresultadoparaserprocessadoporum
métododasuaaplicação.Podemoscriareutilizaras Intentsdediversasmaneiras
easeguirveremosalgunsexemplos.Otrechodecódigoabaixomostracomoabrir
umapáginautilizandoonavegadorqueacompanhaoAndroid:
Uri uri = Uri.parse("http://www.android.com");
Intent intent = new Intent(Intent.ACTION_VIEW, uri);
startActivity(intent);
Uma Urifoicriadaapartirdeuma stringrepresentandoaURLquedeseja-
mosvisitar.Emseguida,instanciamosumanova Intentinformandoaaç ãoque
gostaríamosdeexecutar( Intent.ACTION_VIEW),juntamentecoma Uricriada,
echamamosométodo startActivitydaclasse Activitypassandoa intent.
Reparequenãoindicamosexatamentea activityquedeveseriniciadapara
abrirositedesejado. Nestecaso,anossa Intentéclassificadacomoimplícita.
Combasenaaç ão Intent.ACTION_VIEWeonoconteúdodaUrida Intent,
oAndroiddecidequaléatividademaisadequadapararesolveraURLinformada.
Nestecasooescolhidoéonavegador.
Aseguir,temosumexemplodecomoiniciarumanovaatividadeexistentena
nossaaplicação,passandonoconstrutorda Intentaclassecorrespondenteàati-
vidadequedeveseriniciada.
Intent intent = new Intent(this, OutraAtividade.class);
startActivity(intent);
Diferentementedoexemploanterior,agoranósinformamos exatamentequalati-
vidadedeveseriniciada,ouseja,agoranossa Intentéexplícita. Geralmenteas
36

## Página 39

CasadoCódigo Capítulo2. EntendaofuncionamentodoAndroid
Intentsexplícitassãoutilizadasapenasparainteraç ãoentrecomponentesdeuma
mesmaaplicação,jáqueénecessárioconhecerocomponentequedeveráserativado,
enquantoasimplícitassãousadasparaativarcomponentesdeoutraaplicaç ão,for-
necendoinformaçõesadicionais,comoaaç ãoe Uri,paraqueoAndroidlocalizeo
componenteadequado.
Outracaracterísticaimportanteéquepodemoscolocarinformaçõesextrasna
Intentqueserãoutilizadasposteriormentepelocomponenteiniciadoporela.Para
exemplificar,considerequeanossaaplicaç ãodevetirarumafotoearmazená-laem
umapastaespecífica.
OAndroidjápossuiumaplicativoquerealizaestatarefa,eoquequeremosé
chamá-loapartirdanossaaplicaç ãoparacapturaraimagemesalvá-laemumlocal
determinado. Ocódigoabaixoiniciaa Activitydecâmeradoaparelho,infor-
mandoolocalenomedesejadoparaoarmazenamentodaimagemcapturada:
/*
O exemplo considera que existe a pasta LivroDeAndroid
e que o aplicativo tem permissão de escrita.
*/
Uri uri = Uri.fromFile(
new File("/sdcard/LivroDeAndroid/hello_camera.jpg"));
Intent intent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
intent.putExtra(MediaStore.EXTRA_OUTPUT, uri);
startActivity(intent);
Esseexemplotambémutiliza Intentsimplícitas,poisemnenhummomento
foiindicadoqualaclassede Intentdeveriaserutilizada.Emresumo,uma Intent
éoconjuntodeinformaçõesnecessáriasparaativarumcomponentedeumaapli-
cação.Écompostabasicamentede5informações.
NomedoComponente
Onomedocomponente édefinidopelonomecompletodaclasseeonomedo
pacotedefinidono AndroidManifest.xmlquerepresentamocomponenteque
deveseroencarregadodetratara Intent.
Quandocriamosuma Intentexplícitacomoconstrutor Intent(this,
OutraAtividade.class),onomedocomponenteécriadoautomaticamente.
37

## Página 40

2.2. ConheçaasIntentseIntentFilters CasadoCódigo
Noentanto,tambémépossíveldefini-lodeformaprogramática,utilizandoosméto-
dos setComponent(), setClass()ou setClassName()daclasse Intent.
Ação
Aação éuma stringquedefineoquedeveserrealizado. Existemdiversas
açõesgenéricasnoAndroid,disponibilizadascomoconstantesnaclasse Intent.
Algunsexemplosdeconstantessão:
•ACTION_CALL-indicaqueumachamadatelefônicadeveserrealizada.
•ACTION_VIEW-indicaquealgumdadodeveserexibidoparaousuário.
•ACTION_EDIT-indicaquesedesejaeditaralgumainformaç ão.
•ACTION_SENDTO-indicaquesedesejaenviaralgumainformaç ão.
Enquantoa Intentdeclaraoque deveserfeito,ocomponentequearecebe
éoresponsávelpordefinircomoaaçãoseráexecutada.Ouseja,paraumamesma
ação,podemostercomportamentosdistintosquandoelaforexecutadapordiferen-
tescomponentes.Umexemplodissoéa ACTION_VIEW,quepodeserutilizadatanto
paraindicarquedesejamosabrirumapáginadaInternetquantoparaabririnforma-
çõesdeumcontatoarmazenadonotelefone.
Dados
Os dados de uma Intent são representados através de umaUri e a
partir dela, a aplicação decide o que deve ser feito. No primeiro exemplo de
uso de intents criamos uma Uri para a página que gostaríamos de visi-
tar. Outroexemploseriacriaruma IntentinformandoumaUricomvalor“
content://contacts/people/”,queabririaoscontatosdotelefone:
Uri uri = Uri.parse("content://contacts/people/");
Intent intent = new Intent(Intent.ACTION_VIEW, uri);
startActivity(intent);
Informaçõesextras
Asinformaçõesextras sãoquaisqueroutrosdadosnecessáriosparaqueocom-
ponenteexecuteaaç ãoapropriadamente. Elespodemserinformadosatravésdos
extrasda Intent.
38

## Página 41

CasadoCódigo Capítulo2. EntendaofuncionamentodoAndroid
Noexemploanterior,passamosuma Uricomoextraparainformarolocalonde
afotodeveriaserarmazenada.Alémdisso,podemostambéminformaroutrostipos
dedadoscomo strings,tiposprimitivos, arrayseobjetosserializáveis. Para
incluirumdadocomoextra,utilizamosométodo putExtradaclasse Intent,
fornecendouma stringcomoidentificadordodadoeoseurespectivovalor.Re-
lembrecomocódigoabaixo,noqualo MediaStore.EXTRA_OUTPUTéoidentifi-
cadordainformaç ãoea uriéoextra:
intent.putExtra(MediaStore.EXTRA_OUTPUT, uri);
Categoria
Acategoria,representadaapenasporuma string,servecomoinformaç ão
adicionalparaauxiliaroAndroidnaescolhadequalcomponenteéomaisadequado
pararecebera Intent.Podemosadicionarváriascategoriasauma Intentatravés
dométodo addCategory.Assimcomoasações,existemváriascategoriasprede-
finidas,comoa Intent.CATEGORY_APP_MUSIC,que,quandocolocadaemuma
Intent,informaráaoAndroidqueuma Activitycapazdereproduzirmúsicas
deveseracionada.
2.3 Como as intents são resolvidas
Asinformaçõescontidasnas IntentssãoutilizadaspeloAndroidparalocalizar
ocomponenteadequado,geralmenteuma activity,paraexecutaraaç ãodese-
jada.Quandoonomedecomponenteéinformado,oAndroidinicializaexatamente
aquelecomponente,semnecessidadedeavaliaraaç ãooucategoria.
Poroutrolado,quandoonomenãoéinformado,énecessárioconsultarquais
sãooscomponentesexistentescomahabilidadedeexecutaraaç ãodesejadaeque
pertencemàscategoriasexistentesna Intent.Adicionalmente,oAndroidtambém
podeprocurarporcomponentescapazesderesolvera Urirepassadaetambémde
lidarcomoformatodosdados,o MIME type,informado.
A pergunta que deve estar latente é: como o Android sabe ou encontra a
Activityquedeveseriniciada,apenasinformandoessesdadosna Intent? A
respostaéquenãoexistemágicaeemalgumlugardeveestarespecificadoquede-
terminadasaçõespodemserresolvidasporumdadocomponente.
Adefiniçãodequaisaçõesumcomponenteestáaptoaresponder,bemcomoa
quaiscategoriaselepertenceetambémquaisdadoselesabetratar,érealizadaatravés
de intent filters quesãoconfiguradosnoarquivo AndroidManifest.xml.
39

## Página 42

2.4. ConstruçãodanossaprimeiraIntent CasadoCódigo
Nonossoprimeiroexemplojáexisteadeclaraç ãodeum intent filter no
AndroidManifest.xmlparaa Activityprincipaldanossaaplicaç ão:
...
<activity
android:name=".MainActivity"
android:label="@string/title_activity_main" >
<intent-filter>
<action android:name="android.intent.action.MAIN" />
<category android:name="android.intent.category.LAUNCHER" />
</intent-filter>
</activity>
...
Este intent filter indicaqueaatividade MainActivityéaquelaquedeve
seriniciadaaoabriraaplicaç ãoequetambémdeveserlistadacomoumaaplicaç ão
doAndroidquepodeserutilizadaporumusuário.Os intent filters podem
aindadeclarar,alémdaaç ãoedacategoria,ostiposdedadoscomosquaisocom-
ponenteécapazdelidar,comoumaimagemporexemplo:
<data android:mimeType="image/*" />
Combasenestastrêsinformações( action, categorye data),oAndroid
écapazdeselecionarqualéocomponentemaisadequadopararesponderauma
Intentimplícita,comparandooquefoipassadona Intentcomaquiloqueestá
declaradonos intent filters dosaplicativos.Nossasaplicaçõespodemdefinir
intent filters comaçõesecategoriasprópriasoufazerusodasjáexistentes
paraexporfuncionalidadesparaasdemaisaplicações.
2.4 Construção da nossa primeira Intent
Agora que já sabemos utilizar asIntents e compreendemos os Intent
Filters,vamostirarproveitodistoalterandoonossoHelloWorld2.0paraincluir
uma activityqueiráresponderauma intentimplícita.
A ideia é que na nossa aplicação de exemplo existam duas atividades: a
MainActivity, quecontinuarásendoutilizadaparaousuárioinformaroseu
nome,ea SaudacaoActivity,queseráresponsávelapenasporexibirumasau-
daçãoparaousuárioapartirdasinformaçõescontidasna intent. Elatambém
possuiráumacategoriaprópriaeresponderáaumaaç ãoespecífica.Afigura 2.3de-
monstraaideia.
40

## Página 43

CasadoCódigo Capítulo2. EntendaofuncionamentodoAndroid
Figura2.3:HelloWorldutilizandointents
Primeiramente,devemoscriarumnovo XMLdelayoutqueseráutilizadopela
SaudacaoActivityparaexibiramensagemdesaudaç ãoparaousuário.Paraisto,
acesseomenu File> New> Android XML Layout File. Informeonome
doarquivocomo saudacao,nãoénecessárioalterarnenhumaoutrainformaç ão,
comonafigura 2.4:
41

## Página 44

2.4. ConstruçãodanossaprimeiraIntent CasadoCódigo
Figura2.4:CriandoumnovoXMLdelayout
Nestenovolayoutincluiremosapenasum TextViewparamostrarasaudaç ão
aousuário.Ocódigoficaráassim:
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
android:layout_width="match_parent"
android:layout_height="match_parent"
android:orientation="vertical" >
<TextView
android:id="@+id/saudacaoTextView"
android:layout_width="match_parent"
android:layout_height="wrap_content"/>
42

## Página 45

CasadoCódigo Capítulo2. EntendaofuncionamentodoAndroid
</LinearLayout>
Comolayoutpronto,vamoscriarumanova Activityparaaaplicação,através
domenu File> New> Class. Nacaixadediálogoapresentada,selecioneo
pacote br.com.casadocodigo.helloandroideparaonomedaclasseinforme
SaudacaoActivity,conformeafigura 2.5epressione Finish.
Figura2.5:Criandoumanovaclasse
Podemosentãocriaranossa SaudacaoActivity,queherdaráde Activity:
43

## Página 46

2.4. ConstruçãodanossaprimeiraIntent CasadoCódigo
public class SaudacaoActivity extends Activity {
// teremos que implementar o método onCreate
}
Na implementação do método onCreate, teremos a chamada para
super.onCreateeemseguidaprecisamosindicarqualo layoutseráutilizado,
quenonossocasoseráolayout saudacao:
public class SaudacaoActivity extends Activity {
@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.saudacao);
}
}
Podemosdefinirconstantesparaidentificaroextraquea intentpossui,pois
vamosutilizá-lanosmétodos onCreate:
public class SaudacaoActivity extends Activity {
public static final String EXTRA_NOME_USUARIO =
"helloandroid.EXTRA_NOME_USUARIO";
@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.saudacao);
}
}
Com isso, podemos recuperar aIntent, que nos foi passada através do
método getIntent, e checar se existe um extra com o identificador defi-
nido, ou seja, se aIntent possui o nome do usuário para a exibição da
saudação. Caso exista um extra, obtemos o seu valor utilizando o método
intent.getStringExtra(EXTRA_NOME_USUARIO). Se aintentfornecida
nãopossuinenhumextra,entãoapresentamosumavisoparaousuário.
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
44

## Página 47

CasadoCódigo Capítulo2. EntendaofuncionamentodoAndroid
setContentView(R.layout.saudacao);
TextView saudacaoTextView =
(TextView) findViewById(R.id.saudacaoTextView);
Intent intent = getIntent();
if (intent.hasExtra(EXTRA_NOME_USUARIO)) {
String saudacao = getResources().getString(R.string.saudacao);
saudacaoTextView.setText(saudacao + " " +
intent.getStringExtra(EXTRA_NOME_USUARIO));
} else {
saudacaoTextView.setText("O nome do usuário não foi informado");
}
}
Em seguida, precisaremos alterar o métodosurpreenderUsuario da
MainActivityparadeixardeexibirasaudaç ãoecriara Intentqueacionará
anovaatividade. Comisso,vamosterquedefinirtambémaaç ãoeacategoriada
atividadequeacabamosdecriar.Podemosfazerissodefinindomaisduasconstantes
naclasse SaudacaoActivity:
public class SaudacaoActivity extends Activity {
public static final String EXTRA_NOME_USUARIO =
"helloandroid.EXTRA_NOME_USUARIO";
// As duas novas constantes
public static final String ACAO_EXIBIR_SAUDACAO =
"helloandroid.ACAO_EXIBIR_SAUDACAO";
public static final String CATEGORIA_SAUDACAO =
"helloandroid.CATEGORIA_SAUDACAO";
// método onCreate
}
Nométodo surpreenderUsuario,criamosumanova Intentcomaaç ão
desejadaenelaadicionamosacategoriadefinidaanteriormente.Emseguida,incluí-
moscomoinformaçãoextraovalorinformadono EditText.Eporfim,iniciamos
umanova activitypassandoa Intentcriada.
public void surpreenderUsuario(View v) {
Intent intent = new Intent(SaudacaoActivity.ACAO_EXIBIR_SAUDACAO);
45

## Página 48

2.5. Componentesdeaplicação CasadoCódigo
intent.addCategory(SaudacaoActivity.CATEGORIA_SAUDACAO);
String texto = nomeEditText.getText().toString();
intent.putExtra(SaudacaoActivity.EXTRA_NOME_USUARIO, texto);
startActivity(intent);
}
Jáqueaexibiçãodamensagemdesaudaç ãoéresponsabilidadedeoutraativi-
dade,podemosexcluirdolayoututilizadopela MainActivityo TextViewque
tinhaessepapel. Noarquivodelayout activity_main.xml,removaoúltimo
TextViewdeclarado,como id @saudacaoTextView,poisnãoprecisaremos
maisdele.
Asúltimasalteraçõesparaquenossa SaudacaoActivitypossarespondera
uma Intentserãofeitasnoarquivo AndroidManifest.xml.
Vamosadicionarumnovoblocode activity,declaraçõesnasquaisestabele-
cemosquea SaudacaoActivityrespondepela ACAO_EXIBIR_USUARIOetam-
bématendea intentsquepertencemà CATEGORIA_SAUDACAO:
<activity
android:name="br.com.casadocodigo.helloandroid.SaudacaoActivity">
<intent-filter>
<action android:name="helloandroid.ACAO_EXIBIR_SAUDACAO" />
<category android:name="helloandroid.CATEGORIA_SAUDACAO" />
<category android:name="android.intent.category.DEFAULT" />
</intent-filter>
</activity>
Quando desejamos que uma activity receba intents implícitas,
é obrigatório que no intent filter também seja incluída a categoria
android.intent.category.DEFAULT.Paracada activityépossíveldefinir
váriosintent filters,comconfiguraçõesdiferentesdeaç ãoecategoria.Jápo-
demosexecutaraaplicaç ãoparatestar!Oresultadodeveseromesmoapresentado
naimagem 2.3.
2.5 Componentes de aplicação
Até aqui já desenvolvemos uma aplicação de exemplo e já tivemos contato
comumdoscomponentesmaisimportantesdaplataformaAndroid,quesãoas
46

## Página 49

CasadoCódigo Capítulo2. EntendaofuncionamentodoAndroid
Activities.Agorachegouomomentodeconhecerquaissãoosoutrostiposde
componentes.
Paraconstruirumaaplicaç ãoAndroid,podemosutilizarquatrotiposdecompo-
nentes,cadaqualcomumpropósitoeciclodevidabemdefinidos,sãoeles: activities,
services, content providerse broadcast receivers.
•Activities-umaatividaderepresentaumatelacominterfacegráficacapazde
promoveralgumtipodeinteraç ãocomousuário. Jáutilizamosestetipode
componenteparaimplementarnossaprimeiraaplicaç ão.Umaaplicaç ãoAn-
droidpodesercompostadediversas activitiesparafornecerumconjuntode
funcionalidadesparaousuário.
•Services-osserviçossãocomponentesexecutadosemsegundoplanoeque
nãodispõemdeinterfacegráfica.Seuobjetivoprincipalérealizartarefasque
podemconsumirmuitotempoparaexecutar,semcomprometerainteraç ão
dousuáriocomalguma activity.Tocarumamúsicaoufazerodownload
deumarquivosãoexemplosdefuncionalidadesquepodemserimplementa-
dasutilizando services.
•Contentproviders -osprovedoresdeconteúdosãocomponentesqueper-
mitemoacessoemodificaç ãodedadosarmazenadosemumbancodedados
SQLitelocal,dearquivosarmazenadosnoprópriodispositivooumesmoda-
dosarmazenadosnaweb.Oscontentproviderspodemserexpostosparauso
poroutrasaplicações,comoobjetivodecompartilhardados,ouseremutili-
zadosapenaspelaaplicaç ãoqueoscontém.
•Broadcastreceivers -sãocomponentescapazesderesponderaeventospro-
pagadospelosistemaoperacionalAndroid,comoporexemploonívelbaixo
dabateria,oueventosoriginadosporumaaplicaç ão,comoorecebimentode
umanovamensagemdetexto.
NãoénecessárioqueumaaplicaçãoAndroidtenhatodosestescomponentesmas
éimportanteconhecê-losparaque,nomomentodeprojetaraaplicaç ão,possamos
selecionarocomponenteadequadoparaatenderàsnecessidades.Noscapítulos 5e
6vamosexplorarmaisousodecadacomponente.
47

## Página 50

2.6. CiclodevidadaActivity CasadoCódigo
2.6 Ciclo de vida daActivity
A Activityéumcomponentedeaplicaç ãocomumciclodevidaespecífico.
Quandoousuárioacessaaaplicaç ão,navegapelasop ções,saiouretornaparaa
mesma,asatividadesqueacompõempassamporumasériedeestadosdociclode
vida.Entendercomoelefuncionaéimportanteparaprepararaaplicaç ãoparalidar
comsituaçõesquepodeminterferirnasuaexecuç ão,taiscomoorecebimentode
umaligação,desligamentodateladoaparelhoouaindaaaberturadeoutraaplica-
çãofeitapelousuário.Aimagem 2.6ilustraociclodevidada Activity.
Figura2.6:CiclodevidadaActivity.Fonte:developer.android.com
Semprequea Activitymudadeestado, oAndroidacionaummétodo(
callback)correspondente.Assimqueousuárioiniciaumaaplicaç ão,oAndroid
criaaatividadeprincipalqueestádeclaradano AndroidManisfest.xmlein-
vocaoseumétodo onCreate.Comojávimos,énestemétodoqueatribuímosqual
layoutseráutilizadopelanossaatividadeetambéminicializamosvariáveiserecursos
necessários.
Emseguida,oAndroidinvocaosmétodos onStartelogoapóso onResume.
A Activitytorna-sevisívelparaousuárionoestado Startedeassimpermanece
atéosmétodos onPause(visívelparcialmente)ou onDestroyseremchamados.
Quandoa Activityestánoestado Resumeddizemosqueelaestáno foreground
epoderealizarinteraç ãocomousuário.
A Activitymudaparaoestado Pausedquandoforparcialmenteencoberta
48

## Página 51

CasadoCódigo Capítulo2. EntendaofuncionamentodoAndroid
poroutra Activity,quepodenãoocupartodaatelaousertransparente. Seo
usuáriosairdaaplicaç ãoouiniciaroutraatividadequeencubratotalmenteaque
estásendoexecutada,entãoométodo onStopéinvocadoea Activityvaipara
o background.Mesmonãosendomaisvisívelpelousuário,a Activityconti-
nuainstanciadaecomseuestadointernoinalterado,ouseja,daformacomoestava
quandoemexecuç ão.
Quandouma Activityestánosestadosde Pausedou Stopped,osistema
operacionalpoderemovê-ladamemória,invocandooseumétodo finishouen-
cerrandoarbitrariamenteoseuprocesso.Nestascondições,ométodo onDestroy
édisparado.Apósdestruída,sea Activityforabertanovamente,elaserárecriada.
Podemossobrescreveressesmétodosparaacrescentaraçõesquedevemserrea-
lizadasemdeterminadoestágiodociclodevida.Porexemplo,quandoa Activity
nãoestivermaisvisível,podemosliberarrecursostaiscomoumaconexãoderede,
ouainda,salvarosdadosdigitadospelousuárionométodo onPauseeencerraras
threadsemexecuçãonométodo onDestroy.Ocódigoaseguirmostraosmétodos
quepodemossobrescrever:
public class MinhaActivity extends Activity {
@Override
public void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
// A activity está sendo criada
}
@Override
protected void onStart() {
super.onStart();
// A activity está prestes a se tornar visível
}
@Override
protected void onResume() {
super.onResume();
// A activity está visível
}
@Override
protected void onPause() {
super.onPause();
/* Outra activity está recebendo o foco. Esta activity
ficará pausada */
}
49

## Página 52

2.7. Layouts,WidgetseTemas CasadoCódigo
@Override
protected void onStop() {
super.onStop();
// A activity não está mais visível mas permanece em memória
}
@Override
protected void onDestroy() {
super.onDestroy();
// A activity está prestes a ser destruída (removida da memória)
}
}
Lembre-sesempredeinvocaraimplementaç ãopadrãodométodoqueestá
sendosobrescrito.Porexemplo,seestiversobrescrevendoométodo onStop,então
invoqueantesométodo super.onStop().
2.7 Layouts,W idgets eTemas
Semdúvidaumainterfacegráficacomboausabilidadeequeprovêumaexcelente
experiênciadeuso,assimcomofuncionalidadesbemimplementadas,sãofatores
importanteparaosucessodeumaaplicaç ão mobile.AplataformaAndroidnosofe-
receumbomconjuntodecomponentesvisuais,oschamados widgets,bemcomo
opçõesdelayoutvariadasparaacriaç ãodainterfacecomousuário.
OelementofundamentaldeumainterfacegráficanaplataformaAndroidéa
View. Apartirdelaéquesãoderivadostodososdemaiselementoscomobotões,
imagens, checkboxes,camposparaentradaeexibiç ãodetextosetambém widgets
maiscomplexoscomoseletoresdedata,barrasdeprogressoedepesquisaeaté
mesmoum widgetparaexibirpáginasweb,o WebView. Aimagemabaixomos-
traalgunsdeles:
Figura2.7:Algunswidgetsdisponíveis
50

## Página 53

CasadoCódigo Capítulo2. EntendaofuncionamentodoAndroid
Outraclasseessencialéa ViewGroup,quetemcomocaracterísticaespeciala
possibilidadedeconteroutras Viewseéabaseparatodasasclassesqueconstituem
layouts.Odiagramadafigura 2.8mostraahierarquiadesseselementos.
Figura2.8:HierarquiadeViews
OutrorecursointeressantedisponibilizadopeloAndroidéacriaç ãodeestilose
temasparapersonalizarasuaaplicaç ão. Sevocêjátrabalhoucomfolhasdeestilo
CSSedesignparawebperceberáasimilaridadeentreeles. Paradefinirumestilo,
bastacriarumXMLem res/values/definindoaspropriedadesdesejadas,como
noexemploabaixoquedefineacordotextoeotipodefonte:
<?xml version="1.0" encoding="utf-8"?>
<resources>
<style name="TitleFont"
parent="@android:style/TextAppearance.Large">
<item name="android:layout_width">fill_parent</item>
<item name="android:layout_height">wrap_content</item>
<item name="android:textColor">#FFBA00</item>
<item name="android:typeface">monospace</item>
</style>
</resources>
Háaindaapossibilidadedederivarestilosexistentes. Nalinha3,fazemosisto
informandoqualéoestilo-pai.Paraaplicaroestiloemum TextViewporexemplo,
bastareferenciaroestilodessamaneira:
<TextView style="@style/TitleFont" android:text="@string/titulo" />
51

## Página 54

2.8. Conclusão CasadoCódigo
Comoédeseimaginar,ostemassãoconjuntosdeestilosquepodemserapli-
cadosemumaouemtodasas activitiesdaaplicação. Paraexperimentaressere-
curso,noarquivo AndroidManifest.xmldanossaaplicaç ãodeexemplo,pode-
mosincluiroatributo android:theme="@android:style/Theme.Black"na
tag applicationeexecutaraaplicaç ãonovamente.Agoraelaestácomumaapa-
rênciamaisescuracomomostradonafigura 2.9.
Figura2.9:AplicaçãoHelloAndroidcomoutrotema
2.8 Conclusão
Nestecapítulocompreendemoscomoasaplicaçõessãogeradaseempacotadaspara
execuçãonamáquinavirtualDalvik,alémdeumavisãogeraldoscomponentes
deaplicação(activities, services, content providerse broadcast receivers).Atravésde
exemplos,exploramosumrecurso-chavenaplataformaAndroidquesãoas Intents.
Alémdisso,foiapresentadoociclodevidada Activityeemquaissituaçõesela
52

## Página 55

CasadoCódigo Capítulo2. EntendaofuncionamentodoAndroid
mudadeestado.
Aorganizaçãodoselementosdeinterfacegráfica,widgetselayoutsfoiapresen-
tadaassimcomoautilizaç ãodeestilosetemasparaamodificaç ãodaaparênciada
aplicação. Todosositensapresentadosaquiservemcomoalicerceparaosdemais
capítulos,quefazemusodessesconceitosfundamentaisparaodesenvolvimentode
aplicaçõesconcretasecadavezmaiselaboradas.
53

## Página 57

Capítulo3
Domineosprincipaiselementosde
InterfaceGráfica
Nestecapítuloiremosexploraraconstruç ãodeinterfacesgráficasedaremosinício
àimplementaçãodeumaaplicaç ãoquenosacompanharádurantetodoorestante
dolivro.Aaplicaç ãoqueiremosdesenvolverserviráparanosajudaracontrolaros
gastosrealizadosemnossasviagensdelazerounegócios.Nãoéumaideiarevolu-
cionária,masiránosajudarmuito,poisumaaplicaç ãoassimpossuiumdomínio
muitorico,alémderevelarproblemascomunsdodesenvolvimentoparaAndroid.
Nossaaplicaçãoserábatizadade BoaViagemenelapoderemoscriarumanova
viagem,informandoosdestinos,datasdechegadaepartidaeseelaédenegóciosou
lazer.Paracadaviagem,poderemosinformarosgastosrealizadosporcategoria,tais
comoalimentação,passeios,locomo çãoehospedagem.

## Página 58

CasadoCódigo
Código fonte completo do projeto
Casoqueira,vocêpodeconsultarocódigofontecompletodo Bo-
aViagem, que deixei disponível no meu github:https://github.com/
joaobmonteiro/livro-android.
Osexemplosestãoorganizadosporcapítulo. Portanto,fiqueàvon-
tadeparabaixar,consultar,sugerirmelhoriaseincrementaraaplicaç ão.
Tambémsedeveráinformarqualoor çamentodisponívelparaarealizaç ãoda
viagem. Estainformaçãopoderáserusadaparaqueaaplicaç ãonosalertequando
estivermospróximosdeultrapassarolimitedegastosestabelecido.Estassãoasfun-
cionalidadesprincipaisenodecorrerdolivroaprenderemosoutrascoisascomoa
capturadefotos,usodoGPSemapas,integraç ãoecompartilhamentodedadosque
vocêpodeposteriormenteincluircomonovafuncionalidadedoaplicativo.Aima-
gem3.1mostraalgumasdesuastelas.
Figura3.1:TelasdoBoaViagem
Paracome çar,vamoscriarastelascomoobjetivodeconhecerosdiversostipos
de layouteos widgetsbásicosparacomporformuláriosdeentradadedadoseno
capítuloseguinteincluiremosapersistênciadestesdados. Entãovamoslá! Caso
queiraseguircodificando,crieumnovoprojetoAndroid,comonomeBoaViageme
opacote br.com.casadocodigo.boaviagem,damesmaformaquefizemosno
capítulo1.
Nesteprimeiromomentonospreocuparemoscomasduastelasiniciaisdaapli-
cação,ateladelogineatelainicialdeop ções,comumentechamade dashboard.
Abaixotemosoprotótipocomosdetalhesdostiposdelayoutqueiremosutilizar.
56

## Página 59

CasadoCódigo Capítulo3. DomineosprincipaiselementosdeInterfaceGráfica
Figura3.2:Teladeloginedashboard
3.1 LinearL ayout
Paraateladelogin,utilizaremoso LinearLayout,quepermiteaorganizaç ãodos
elementosdeformalinear,posicionandoitensumabaixodooutro,quandoconfi-
guradocomorientaç ãovertical,ouumaoladodooutro,quandoconfiguradocom
orientaçãohorizontal.Àsvezesescolheraorientaç ãocertacausaumpoucodecon-
fusão,entãoadicaéselembrardequeaorientaç ãodizrespeitoàdire çãonaqualos
itensserãoincluídosnatela.Ouseja,naorientaç ãovertical,ositensserãoincluídos
nolayoutdecimaparabaixoenaorientaç ãohorizontal,daesquerdaparaadireita.
Entãoparafazerumateladeloginparecidacomadoprotótipo 3.2,utilizaremos
um LinearLayout,comorientaç ãovertical. Paraestatela,podemoscriarum
novoarquivodelayoutcomonomede login.xml.Oprimeiropassoédefiniro
LinearLayoutquequeremosedizerqueaorientaç ãoserávertical:
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
android:layout_width="match_parent"
57

## Página 60

3.1. LinearLayout CasadoCódigo
android:layout_height="match_parent"
android:gravity="center_vertical"
android:orientation="vertical" >
<!-- Campos virão aqui -->
</LinearLayout>
Para especificar um layout existem dois atributos fundamentais: o
layout_width(linha3),queindicaalarguradoelemento,e layout_height
(linha4),queindicaasuaaltura. Hádoisvaloresimportantesparaestesatributos
quesãoo match_parenteo wrap_content. Oprimeirovalorindicaqueo
tamanhodeveseromesmoqueodoelemento-paienquantoosegundoindicaque
otamanhodevesergrandeosuficienteparaabrigaroconteúdoaserexibido.
Note que na linha 5 utilizamos um outro atributo, que é o
android:gravity="center_vertical". Ele indica que o layout deve fi-
carcentralizadoverticalmentenatela.Aorientaç ãoquedesejamoséinformadano
atributo android:orientation.
O próximo passo é exibir a logo da aplicação. Para isso, podemos in-
cluir um ImageView, que deve ficar ao centro e mostrar a imagem de
android:src="@drawable/logo".Comisso,bastaterumaimagememumar-
quivo logo.pngecolocá-lanosdiretórios drawabledoprojeto.
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout ...>
<ImageView
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_gravity="center"
android:layout_marginBottom="50dp"
android:src="@drawable/logo" />
</LinearLayout>
Agora,podemosincluiroscamposparaqueousuárioforne çaseuloginesenha
paraentrarnaaplicaç ão.Precisaremosdecomponentes TextViewparamostrara
descriçãodoscampos,comosefossem labels,etambémdo EditTextparaocampo
ondeousuáriodigitaráseulogin:
58

## Página 61

CasadoCódigo Capítulo3. DomineosprincipaiselementosdeInterfaceGráfica
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout ...>
<!-- Logo -->
<TextView
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:text="@string/usuario" />
<EditText
android:id="@+id/usuario"
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:inputType="text" >
<requestFocus />
</EditText>
</LinearLayout>
Repareno EditText:definimosumatributo android:inputType,parain-
dicarqueessecampoéumasimplesentradadetexto,ouseja,caracteresalfanumé-
ricos.Tambémutilizamoso <requestFocus>paraqueestecamporecebaofoco
quandoatelaforexibida.
Comisso,parafazermosocampodesenha,bastacriarmosumnovo EditText
cujo android:inputTypesejadotipo textPassword:
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout ...>
<!-- Logo -->
<!-- Campo de login do usuário -->
<TextView
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:text="@string/senha" />
<EditText
android:id="@+id/senha"
android:layout_width="match_parent"
59

## Página 62

3.1. LinearLayout CasadoCódigo
android:layout_height="wrap_content"
android:inputType="textPassword" />
</LinearLayout>
Como adicionar rolagem vertical
Os layouts do Android não suportam por padrão a rolagem ver-
ticaldatela. Parateressafuncionalidade, énecessárioutilizaruma
ScrollView e colocar o layout que precisa da rolagem como seu
elemento-filho.
Alémdostipos texte textPassword,tambémexistemdiversosoutros,tais
comoo number,queindicanúmerosefazcomqueotecladoexibidoparadigitaç ão
sejaapenasotecladonumérico; phone,paranúmerosdetelefone; datee time,
parainformaçõesdedataehora. Paravertodasasop çõesdisponíveisconsultea
documentaçãoem http://developer.android.com/reference.
Agorabastafazermosobotãoentrar,usandoaTag Button:
<Button
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:layout_gravity="bottom"
android:onClick="entrarOnClick"
android:text="@string/entrar" />
Nessebotão,vinculamosaaç ão entrarOnClickquefaráaautenticaçãodo
usuárioe,casosejabem-sucedida,iniciaráa activityda dashboard.Vamosim-
plementarestemétodona BoaViagemActivityqueutilizaráolayoutdatelade
loginqueacabamosdedefinir.
public class BoaViagemActivity extends Activity {
public void entrarOnClick(View v) { }
}
Notequefizemosométodo entrarOnClickrecebendocomoparâmetroum
objetodotipo View. Vamosimplementaralógicadologindentrodessemétodo
60

## Página 63

CasadoCódigo Capítulo3. DomineosprincipaiselementosdeInterfaceGráfica
eminstantes. Masprimeiro,faremoscomque,quandoa BoaViagemActivity
sejacriada,elafiqueassociadaaolayoutdologin.Paraisso,vamosreescreveromé-
todo onCreateeinvocarométodo setContentView,passandoumareferência
aolayoutdelogin.
public class BoaViagemActivity extends Activity {
@Override
public void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.login);
}
public void entrarOnClick(View v) { }
}
A classeR
Aclasse RégeradaautomaticamentepeloADT,utilizandoasferra-
mentasdoSDK,eserveparamapearosrecursosexistentesnoaplicativo
naformadeconstantes. Dessaforma,podemosreferenciarfacilmente
arquivosdelayout, widgetseoutrostiposderecursoscomo strings::
e arrays.
Nessecome ço,faremosumaautenticaç ãosimples,naqualousuárioinformado
deveser“leitor”easenhadeveser“123”. Masparaissotemosquerecuperaruma
referênciaparaoscamposdeusuárioesenhaqueestãonatela,paratermosacesso
aostextospresentesnoscampos.Noprópriométodo onCreate,vamosrecuperar
referênciasparaosdois EditText,atravésdométodo findViewById.
public class BoaViagemActivity extends Activity {
private EditText usuario;
private EditText senha;
@Override
public void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.login);
61

## Página 64

3.1. LinearLayout CasadoCódigo
usuario = (EditText) findViewById(R.id.usuario);
senha = (EditText) findViewById(R.id.senha);
}
}
Note que foi passado para o findViewById uma referência para
R.id.usuario e em seguida paraR.id.senha. Essas são referências para
os EditTextquecriamosanteriormentenatelaedemosonomede usuarioe
senha.
Comessescomponentesrecuperados,agorapodemosdescobrirqualéotexto
queestánelesquandoométodo entrarOnClickforinvocado:
public void entrarOnClick(View v) {
String usuarioInformado = usuario.getText().toString();
String senhaInformada = senha.getText().toString();
if("leitor".equals(usuarioInformado) &&
"123".equals(senhaInformada)) {
// vai para outra activity
} else{
// mostra uma mensagem de erro
}
}
}
Nocasodefalhanaautenticaç ão,deve-seexibirumamensagemparaousuário,
atravésdo widget Toast,queserveparaapresentarumanotificaç ãorápidaparao
usuário,informandooresultadodealgumaoperaç ão.Épossíveldefinirporquanto
tempoamensagemficarávisível,atravésdeumaduraç ão Toast.LENGTH_SHORT
ou Toast.LENGTH_LONG.
if("leitor".equals(usuarioInformado) &&
"123".equals(senhaInformada)) {
// vai para outra activity
} else {
String mensagemErro = getString(R.string.erro_autenticao);
Toast toast = Toast.makeText(this, mensagemErro,
Toast.LENGTH_SHORT);
toast.show();
}
62

## Página 65

CasadoCódigo Capítulo3. DomineosprincipaiselementosdeInterfaceGráfica
Reparequerecuperamosamensagemdeerroemumarquivo strings.xml,
atravésde R.string.erro_autenticacao,ouseja,temosnessearquivouma
mensagemcujonomeé erro_autenticacao:
1 <?xml version="1.0" encoding="utf-8"?>
2 <resources>
3 <!-- mensagens padrão -->
4
5 <string name="erro_autenticacao">Usuário ou senha inválidos</string>
6 </resources>
A única coisa que falta agora é redirecionar o usuário para outraacti-
vity caso a autenticação seja feita corretamente. Para isso, criaremos uma
DashboardActivityquevamosimplementarnaspróximasse çõesefalarque,ao
autenticar,essa activityseráiniciada:
if("leitor".equals(usuarioInformado) &&
"123".equals(senhaInformada)){
startActivity(new Intent(this,DashboardActivity.class));
} else {
String mensagemErro = getString(R.string.erro_autenticao);
Toast toast = Toast.makeText(this, mensagemErro,
Toast.LENGTH_SHORT);
toast.show();
}
3.2 RelativeLayout
Opróximopassoécriarolayouteaatividadeparaexibirateladeop çõesda
nossa aplicação, o dashboard. Para esta tela, utilizaremos uma combinação do
LinearLayout,queacabamosdever,como RelativeLayout. Ébastanteco-
mum,emuitasvezesnecessário,aninhardiversostiposdelayout.
O RelativeLayout,umdosmaispoderososeversáteisdisponíveisnaplata-
formaAndroid,permiteposicionarumelementoemumlocalrelativoaoutrocom-
ponente.Épossível,porexemplo,posicionarumaimagem abaixodeumbotão,que
ficaà esquerdadeum TextView. VamoscriarumnovoarquivoXMLdelayout
chamado dashboard.xml.Oobjetivoéquetenhamos,alémdateladelogin,uma
novatelacomasaçõesquepodemosfazernaaplicaç ão,comonaimagem 3.3.
63

## Página 66

3.2. RelativeLayout CasadoCódigo
Figura3.3:Teladeloginedashboarddaaplicaç ão
Paraconstruirmosessanovatela,vamosadicionaro RelativeLayoutque
deveocupartodooespaçorestantedeixadopelo LinearLayout:
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
xmlns:android="http://schemas.android.com/apk/res/android"
android:layout_width="match_parent"
android:layout_height="match_parent"
android:background="#333333"
android:orientation="vertical">
<TextView
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_gravity="center"
android:text="@string/app_name"
android:textAppearance="?android:attr/textAppearanceLarge" />
<RelativeLayout
android:layout_width="match_parent"
android:layout_height="match_parent"
android:background="#015488">
64

## Página 67

CasadoCódigo Capítulo3. DomineosprincipaiselementosdeInterfaceGráfica
<!-- Vamos adicionar elementos aqui -->
</RelativeLayout>
</LinearLayout>
Pararepresentarcadaop çãoda dashboard,vamosutilizar TextViewsqueserão
alinhadosdeformarelativaaosdemaiselementosnatela.Paraposicionaroprimeiro
elementoda dashboardnocantosuperioresquerdo,incluiremosum TextViewque
defineumtamanhodemargemesquerda( layout_marginLeft)eparaotopo
(layout_marginTop).
Esteelementonãopossuinenhumainformaç ãoespecíficadelayoutrelativo,
apenasdemargens,masservirádereferênciaparaopróximo TextView. Este,
porsuavez,ficaránocantosuperiordireito. Então,iremoscolocá-loaoladodi-
reitodoseucomponente-pai(opróximo RelativeLayout),utilizandooatributo
layout_alignParentRight=true. Tambéméprecisoalinharoseutopocom
odo TextViewâncorareferenteao“NovoGasto”. Paraisto,utiliza-seoatributo
layout_alignTopinformandoo iddoelementoqueseráareferência,nocasoé
o“@id/novo_gasto”,veja:
<RelativeLayout ...>
<TextView
android:id="@+id/novo_gasto"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_marginLeft="50dp"
android:layout_marginTop="80dp"
android:clickable="true"
android:drawableTop="@drawable/novo_gasto"
android:onClick="selecionarOpcao"
android:text="@string/novo_gasto"
android:textColor="#FFFFFF"
android:textStyle="bold" />
<TextView
android:id="@+id/nova_viagem"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
65

## Página 68

3.2. RelativeLayout CasadoCódigo
android:layout_alignParentRight="true"
android:layout_alignTop="@id/novo_gasto"
android:layout_marginRight="50dp"
android:clickable="true"
android:drawableTop="@drawable/nova_viagem"
android:onClick="selecionarOpcao"
android:text="@string/nova_viagem"
android:textColor="#FFFFFF"
android:textStyle="bold" />
</RelativeLayout>
Tambémemrelaçãoao TextViewdonovogasto,alinhamosoitem“Minhas
Viagens”àesquerdae,paramantê-lonapartedebaixodatela,especificamosqueele
devesealinharcomoaregiãoinferiordocomponente-pai,atravésdapropriedade
android:layout_alignParentBottom="true".
Oúltimo TextView, paraaop çãodeconfiguraçõesdaaplicaç ão, utilizao
TextViewanteriorparasealinharnaregiãoinferiordatelaetambémsealinha
àdireitacombaseno TextViewda“NovaViagem”.Éimportanteressaltarquepo-
demosobteromesmoresultado(mesmodesigndetela)utilizandooutrostiposde
layoutsouutilizandoosmesmos layoutsmasdeformadiferentedasapresentadas
aqui:
<RelativeLayout ...>
<!-- Novo gasto e nova viagem -->
<TextView
android:id="@+id/minhas_viagens"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_alignLeft="@id/novo_gasto"
android:layout_alignParentBottom="true"
android:layout_marginBottom="120dp"
android:clickable="true"
android:drawableTop="@drawable/minhas_viagens"
android:onClick="selecionarOpcao"
android:text="@string/minhas_viagens"
android:textColor="#FFFFFF"
android:textStyle="bold" />
66

## Página 69

CasadoCódigo Capítulo3. DomineosprincipaiselementosdeInterfaceGráfica
<TextView
android:id="@+id/configuracoes"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_alignBottom="@id/minhas_viagens"
android:layout_alignRight="@id/nova_viagem"
android:clickable="true"
android:drawableTop="@drawable/configuracoes"
android:onClick="selecionarOpcao"
android:text="@string/configuracoes"
android:textColor="#FFFFFF"
android:textStyle="bold" />
</RelativeLayout>
Dessaforma,ocódigocompletoutilizandoosdois layoutsficaassim:
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
xmlns:android="http://schemas.android.com/apk/res/android"
android:layout_width="match_parent"
android:layout_height="match_parent"
android:background="#333333"
android:orientation="vertical" >
<TextView
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_gravity="center"
android:text="@string/app_name"
android:textAppearance="?android:attr/textAppearanceLarge" />
<RelativeLayout
android:layout_width="match_parent"
android:layout_height="match_parent"
android:background="#015488" >
<TextView
android:id="@+id/novo_gasto"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
67

## Página 70

3.2. RelativeLayout CasadoCódigo
android:layout_marginLeft="50dp"
android:layout_marginTop="80dp"
android:clickable="true"
android:drawableTop="@drawable/novo_gasto"
android:onClick="selecionarOpcao"
android:text="@string/novo_gasto"
android:textColor="#FFFFFF"
android:textStyle="bold" />
<TextView
android:id="@+id/nova_viagem"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_alignParentRight="true"
android:layout_alignTop="@id/novo_gasto"
android:layout_marginRight="50dp"
android:clickable="true"
android:drawableTop="@drawable/nova_viagem"
android:onClick="selecionarOpcao"
android:text="@string/nova_viagem"
android:textColor="#FFFFFF"
android:textStyle="bold" />
<TextView
android:id="@+id/minhas_viagens"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_alignLeft="@id/novo_gasto"
android:layout_alignParentBottom="true"
android:layout_marginBottom="120dp"
android:clickable="true"
android:drawableTop="@drawable/minhas_viagens"
android:onClick="selecionarOpcao"
android:text="@string/minhas_viagens"
android:textColor="#FFFFFF"
android:textStyle="bold" />
<TextView
android:id="@+id/configuracoes"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
68

## Página 71

CasadoCódigo Capítulo3. DomineosprincipaiselementosdeInterfaceGráfica
android:layout_alignBottom="@id/minhas_viagens"
android:layout_alignRight="@id/nova_viagem"
android:clickable="true"
android:drawableTop="@drawable/configuracoes"
android:onClick="selecionarOpcao"
android:text="@string/configuracoes"
android:textColor="#FFFFFF"
android:textStyle="bold" />
</RelativeLayout>
</LinearLayout>
Dica
UtilizeavisualizaçãográficadolayoutnaIDEparaterumapréviade
comoestáficandoatela.
Pararepresentarcadaop çãona dashboardutilizamoso widget TextViewque,
alémdapossibilidadedeexibirtextos,tambémpodeexibirumaimagemassociada.
Essasimagenspodemserposicionadasàesquerda,àdireita,acimaouabaixodo
textoqueseráexibido.Nonossocaso,optamosporcolocá-laacimadotexto,infor-
madoaimagemdesejadanoatributo drawableTop.Tambémespecificamosque
nossos TextViewspodemserclicados,atravésdoatributo clickableequeo
textodeveestaremnegritoeserdacorbranca(atributos textStylee textColor
respectivamente).
Cuidados com muitos layouts aninhados
Utilizarmuitoslayoutsaninhadospodetrazerproblemasdedesem-
penho. Prefiradesenvolverlayoutsquepossuempoucosníveisdeani-
nhamento.Consulteoseguinteguiaparaobterdicasdecomomelhorar
odesempenhonessassituações http://developer.android.com/training/
improving-layouts/index.html
Paradarmoscontinuidadeàimplementaç ãodatelainicialdeop ções,vamos
usaraclasse DashboardActivity. Estanovaatividadedeveutilizarolayout
69

## Página 72

3.2. RelativeLayout CasadoCódigo
dashboard.xmleresponderaosmétodosdisparadosquandoumaop çãoforse-
lecionada.Porenquanto,ocódigodelaficaráassim:
public class DashboardActivity extends Activity {
@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.dashboard);
}
public void selecionarOpcao(View view) {
/*
com base na view que foi clicada
iremos tomar a ação correta
*/
TextView textView = (TextView) view;
String opcao = "Opção: " + textView.getText().toString();
Toast.makeText(this, opcao, Toast.LENGTH_LONG).show();
}
}
Éimportantelembrarquetodasasatividadesqueforemcriadasdevemserde-
claradasno AndroidManifest.xml.Alémdisso,queremossuprimirabarrade
títulopadrão,oquetambéméfeitono AndroidManifest.xmlconfigurando
paranossaaplicaç ãootema @android:style/Theme.NoTitleBar.Comisso,
o AndroidManifest.xmlficaráparecidocom:
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
package="br.com.casadocodigo.boaviagem"
android:versionCode="1"
android:versionName="1.0" >
<uses-sdk android:minSdkVersion="10" />
<application
android:icon="@drawable/ic_launcher"
android:label="@string/app_name"
android:theme="@android:style/Theme.NoTitleBar" >
<activity
70

## Página 73

CasadoCódigo Capítulo3. DomineosprincipaiselementosdeInterfaceGráfica
android:name=".BoaViagemActivity"
android:label="@string/app_name" >
<intent-filter>
<action android:name="android.intent.action.MAIN" />
<category
android:name="android.intent.category.LAUNCHER" />
</intent-filter>
</activity>
<activity android:name=".DashboardActivity" />
</application>
</manifest>
Comateladelogine dashboardprontas,podemosexecutaranossaaplicaç ãoe
compararastelascriadascomosprotótiposapresentadosnaimagem 3.2.Ficaram
parecidas,nãoémesmo?
Dica
Duranteodesenvolvimentodoslayoutsdaaplicaç ão,écomumexe-
cutarmosoaplicativováriasvezesparavercomoestáficando.Paraevitar
quesejanecessárionavegareirselecionandoop çõesatéchegarnaacti-
vitydesejada,incluao intent-filternaactivityasertestadapara
queelasejaaprimeiraaseriniciada.
3.3 TableLayout
Aspróximastelasqueiremosimplementarserãoacriaç ãodeumanovaviageme
oregistrodeumnovogasto. Sãotelastipicamentedecadastroepermitirãoque
sejamexploradosdiversos widgetsparaentradadedados,taiscomoos Spinner,
DatePickerenossojáconhecido EditText,alémdemaisumtipodelayout,o
TableLayout.Oprotótipodastelaséoseguinte:
71

## Página 74

3.3. TableLayout CasadoCódigo
Figura3.4:Telasdecadastrodeviagemedegasto
Começaremospelateladecadastrodeumanovaviagem. Paraestelayoututi-
lizaremosumacombinaç ãode LinearLayoute TableLayout. Comoonome
sugere,o TableLayoutpermiteacriaçãodelayoutscomaorganizaç ãoemformato
detabelas,similarao <table>doHTML.Oelemento TableRowéutilizadopara
representarumalinhaeseuselementos-filhosrepresentamumacélula.Porexemplo,
seuma TableRowpossuidoiselementos,entãoaquelalinhapossuiduascolunas.
Aindapodemosutilizarqualqueroutra viewquenãoa TableRowpararepre-
sentarumalinha.Nestecaso,a viewutilizadarepresentaumacélulaeumaúnica
colunaparaaquelalinha.Ouseja,comissotemosumcomportamentoparecidocom
o colspandoHTML,noqualumacélulaseestendeporváriascolunas.
O TableLayouttambémtemoutracaracterísticaimportante:todososseus
elementos-filhosnãopodemespecificaroatributo layout_width,queporpadrão
jápossuemovalor MATCH_PARENT.Noentanto,oatributo layout_heightpode
serdefinido(ovalorpadrãoé WRAP_CONTENT),excetoquandooelemento-filhofor
uma TableRowqueterásempreovalor WRAP_CONTENT.
Isto por um lado é bom, pois evita que tenhamos que especificar inúme-
ros atributos de layout, mas por outro, pode limitar as situações de uso do
72

## Página 75

CasadoCódigo Capítulo3. DomineosprincipaiselementosdeInterfaceGráfica
TableLayoutpornãotermosesteajustefino. Estacaracterísticanoslevouain-
cluirum LinearLayoutparaincluirmosumtítulocentralizadonatela. Ainda
utilizamosuma ScrollViewparaproverarolagemdatelaquandonecessário.
<?xml version="1.0" encoding="utf-8"?>
<ScrollView xmlns:android="http://schemas.android.com/apk/res/android"
android:layout_width="match_parent"
android:layout_height="match_parent" >
<TableLayout
xmlns:android="http://schemas.android.com/apk/res/android"
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:stretchColumns="0,1,2" >
<LinearLayout
android:background="#015488"
android:orientation="vertical" >
<TextView
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_gravity="center"
android:text="@string/nova_viagem"
android:textAppearance=
"?android:attr/textAppearanceLarge"
android:textStyle="bold" />
</LinearLayout>
</ScrollView>
O TableLayoutpossuidoisatributosmuitoúteisparaajustarotamanhodas
colunas.Umdeleséo stretchColumns(linha10),quepermitequeascolunasin-
dicadasocupemtodooespaçodisponívelentreosseuselementos-filhoseopróprio
TableLayout.Comoaconfiguraç ãodelarguradonossolayouté MATCH_PARENT,
entãoascolunasdevemexpandiroseutamanhodemodoaocupartodaatela.
Ooutroatributoéo shrinkColumnsqueindicaquedeterminadascolunas
podemterseutamanhoreduzidoquandorequisitadopelo TableLayout. Ova-
lordessesatributoséoíndice(iniciandoem 0)referenteàscolunasdesejadas. O
TableLayoutadicionaaslinhaseoselementosdelayoutnasequênciaemqueapa-
73

## Página 76

3.3. TableLayout CasadoCódigo
recemnoXML,incrementandoautomaticamenteoíndicedacoluna.
Senecessário,épossívelinformaraqualcolunadeterminadoelementopertence
utilizandooatributo layout_column.Porém,aordemsequencialdeveserrespei-
tada,ouseja,nãoépossívelincluirumelementonacolunadeíndice1edepoisum
elementonacolunadeíndice 0,nemviaXML,nemprogramaticamente.Quando
umnúmerodasequênciaéomitido,o TableLayoutassumequeaquelaéuma
colunavazia.Portanto,fazerusodo layout_columnfazmaissentidoquandode-
sejamosincluircolunasvaziasparacriarespaçoentreoselementosepossivelmente
incluí-lasno shrinkColumns.
Agora,bastacolocarmososelementosqueirãocomporolayoutecadaumadas
colunas.Nasduasprimeiraslinhasdatabela,teremosacaixadetextoparaqueseja
informadoodestinoelogoacimadelaum TextViewparaolabeldocampo:
<TextView android:text="@string/destino" />
<EditText
android:id="@+id/destino"
android:inputType="text" >
</EditText>
Emseguida, maisum TextViewparaolabeldo“TipodaViagem”eum
RadioGroupquevaiconteros RadioButtonparafazerasop çõescomo“Lazer”e
“Negócios”.
<TextView android:text="@string/tipo_da_viagem" />
<RadioGroup
android:id="@+id/tipoViagem"
android:orientation="horizontal" >
<RadioButton
android:id="@+id/lazer"
android:checked="true"
android:text="@string/lazer" />
<RadioButton
android:id="@+id/negocios"
android:layout_marginLeft="30dp"
android:text="@string/negocios" />
</RadioGroup>
74

## Página 77

CasadoCódigo Capítulo3. DomineosprincipaiselementosdeInterfaceGráfica
Aseguir,temosmaisumalinhaqueiráconteroslabelsparadoiscampos:“Data
deChegada”e“DatadeSaída”. Comonãoqueremosquecadaelementofiqueem
umalinhaesim queosdoiselementosocupemamesma,vamosenvolvê-losnum
TableRow,ondecadaumocuparáumacoluna:
<TableRow>
<TextView
android:layout_gravity="center"
android:text="@string/data_da_chegada" />
<TextView
android:layout_gravity="center"
android:text="@string/data_da_saida" />
</TableRow>
Logoabaixodotexto“DatadeChegada”e“DatadeSaída”temosbotõesque
serãoutilizadosparaabrircaixasdediálogoespecíficasparasele çãodedatas, o
DatePickerDialog. Também utilizaremos estewidget na tela de registro de
umnovogasto. Veremoscomoutilizá-lonase ção 3.4. Posteriormente,revisitea
ViagemActivityparaimplementaressesdoisitens.
<TableRow>
<Button
android:id="@+id/dataChegada"
android:onClick="selecionarData"
android:text="@string/selecione" />
<Button
android:id="@+id/dataSaida"
android:onClick="selecionarData"
android:text="@string/selecione" />
</TableRow>
Porfim,montamososcamposparaovalordoor çamentoequantidadedepes-
soas,alémdeumbotãoparaconfirmarocadastrodaviagem:
<TextView android:text="@string/orcamento" />
<EditText
75

## Página 78

3.3. TableLayout CasadoCódigo
android:id="@+id/orcamento"
android:inputType="numberDecimal" />
<TableRow>
<TextView
android:layout_width="wrap_content"
android:text="@string/quantidade_de_pessoas" />
<EditText
android:id="@+id/quantidadePessoas"
android:inputType="number" />
</TableRow>
<Button
android:onClick="salvarViagem"
android:text="@string/salvar" />
Comolayoutpronto,crieumanovaatividadechamada ViagemActivity
e para abri-la precisamos adicionar a implementação correta do método
selecionarOpcao da DashboardActivity. O código deste método será
assim:
1 public void selecionarOpcao(View view) {
2 switch (view.getId()) {
3 case R.id.nova_viagem:
4 startActivity(new Intent(this, ViagemActivity.class));
5 break;
6 }
7 }
Quandoumitemforselecionado,estemétodoseráchamadorecebendocomo
parâmetroa Viewquefoiclicada.Utilizandoo idda Viewsaberemosqualitem
foiselecionadoeentãoexecutaremosaaç ãodesejada.Aoexecutaraaplicaç ãono-
vamenteeselecionaroitem“NovaViagem”teremoscomoresultadoumatelaseme-
lhanteàseguinte:
76

## Página 79

CasadoCódigo Capítulo3. DomineosprincipaiselementosdeInterfaceGráfica
Figura3.5:Teladecadastrodeumanovaviagem
3.4 DatePicker
O DatePickeréumwidgetprojetadoparaasele çãodedatasquepodeserutilizado
tantodemaneiradireta,incluindo-odiretamentenolayout,comoindireta,através
deumacaixadediálogo( DatePickerDialog)apresentadaparaousuário.
Apesardesermaissimples,autilizaç ãodiretado DatePickernãoécomum,
umavezqueo widgettempropor çõesexageradas,ocupandoumespaçoconsiderável
natela.Suaformadeusomaiscomuméatravésdo DatePickerDialog.
Paraexemplificaroseuusoetambémdarprosseguimentoàimplementaç ãoda
nossaaplicação,vamosdesenvolverolayouteaatividadereferentesaoregistrode
umnovogasto,deacordocomoprotótipodateladecadastrodosgastos,comona
figura3.6.
77

## Página 80

3.4. DatePicker CasadoCódigo
Figura3.6:Telasdecadastrodeviagemedegasto
OarquivoXMLdelayoutseráo gasto.xmleaclassedaatividadeseráa
GastoActivity.Olayoutdestatelautilizaelementosquejáconhecemoseéfor-
madoporum LinearLayouteum TableLayout,inseridosdentrodeuma
ScrollView,quevamosimplementaraospoucos.
Primeiropodemosfazerapartesuperiordatela,comum“banner”escrito“Novo
Gasto”eonomedodestino,pararepresentarseutítulo.Paraistoutilizaremosum
LinearLayoutaplicandoumacordiferente,comoatributo background,ein-
cluiremosdois TextViewsparaasinformaçõestextuais:
<?xml version="1.0" encoding="utf-8"?>
<ScrollView xmlns:android="http://schemas.android.com/apk/res/android"
android:layout_width="match_parent"
android:layout_height="match_parent" >
<LinearLayout
78

## Página 81

CasadoCódigo Capítulo3. DomineosprincipaiselementosdeInterfaceGráfica
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:orientation="vertical" >
<LinearLayout
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:background="#015488"
android:orientation="vertical" >
<TextView
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_gravity="center"
android:text="@string/novo_gasto"
android:textAppearance=
"?android:attr/textAppearanceLarge"
android:textStyle="bold" />
<TextView
android:id="@+id/destino"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_gravity="center"
android:textAppearance=
"?android:attr/textAppearanceLarge"
android:textStyle="bold" />
</LinearLayout>
</LinearLayout>
</ScrollView>
Emseguida,vamosfazerum TableLayoutcomduaslinhaseduascolunas.
Emcadacolunaficaráumcampo,nocaso,naesquerdaficaráovalor,enadireita,a
data.Nalinhadecimaficaráadescriç ãoenalinhainferiorficaráoprópriocampo.
Ocampoparaadataconteráapenasumbotão,queaoserclicado,irádispararo
método selecionarDatadaatividadequeabreacaixadediálogoparaasele ção
dadataderealizaç ãodogasto.
<?xml version="1.0" encoding="utf-8"?>
<ScrollView ...>
79

## Página 82

3.4. DatePicker CasadoCódigo
<LinearLayout ...>
<!-- Parte superior da tela -->
<TableLayout
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:stretchColumns="0,1">
<TableRow>
<TextView android:text="@string/valor" />
<TextView
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_gravity="center"
android:text="@string/data" />
</TableRow>
<TableRow>
<EditText
android:id="@+id/valor"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:inputType="numberDecimal" />
<Button
android:id="@+id/data"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_gravity="center"
android:onClick="selecionarData"
android:text="@string/selecione" />
</TableRow>
</TableLayout>
<!-- Mais campos virão aqui -->
</LinearLayout>
80

## Página 83

CasadoCódigo Capítulo3. DomineosprincipaiselementosdeInterfaceGráfica
</ScrollView>
Paraimplementarmosa activityefazê-laabriracaixadediálogoparaasele ção
dadatacorretamente,nométodo onCreateinicializamostrêsvariáveispararepre-
sentaroano,mêsediacombasenadataatual.Adicionalmente,alteramosotexto
dobotãoparaexibiradataatualemanterousuárioinformadosobreadataquefoi
selecionada.
public class GastoActivity extends Activity {
private int ano, mes, dia;
private Button dataGasto;
@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.gasto);
Calendar calendar = Calendar.getInstance();
ano = calendar.get(Calendar.YEAR);
mes = calendar.get(Calendar.MONTH);
dia = calendar.get(Calendar.DAY_OF_MONTH);
dataGasto = (Button) findViewById(R.id.data);
dataGasto.setText(dia + "/" + (mes+1) + "/" + ano);
}
}
Ométodo selecionarDataapenasinvocaométodo showDialogdapró-
pria Activitypassandoumidentificadorqueindicaodiálogoquedeveseraberto.
Estaidentificaçãoénecessária,poispodemosterinúmerasdiálogosgerenciadospela
mesma activity.Écomumencontrarcódigosquefazemusodeconstantespararepre-
sentarosdiálogosqueserãoabertos,noentanto,preferimosutilizaroidentificador
daprópria viewquedesejaabrirodiálogoumavezqueelejáéúnicoparaolayout
ejáestádeclarado.
public void selecionarData(View view){
showDialog(view.getId());
}
Quandoométodo showDialogéinvocadoparacriarumacaixadediálogo
pelaprimeiravez,ométodo onCreateDialogéchamado,passandooidentifica-
dorinformado,paraquesejainstanciadoumnovo DatePickerDialog. Sefor
81

## Página 84

3.4. DatePicker CasadoCódigo
necessárioexecutaralgumaoperaçãoparaalterarinformaçõesdacaixadediálogo
semprequeelaforaberta,bastariareescreverométodo onPrepareDialog.
Porfim,temosqueimplementarum listenerqueseráresponsávelportratar
oresultado, ouseja, adataescolhidapelousuário. Issosefazatravésdadefi-
niçãodeumaclasseanônima, queimplementa OnDateSetListener, parao
listenerutilizado. Estaclassepossuiapenasummétodoqueseráinvocadopelo
próprio DatePickerDialogquandoumadataforselecionada,queéométodo
onDateSet.
Nestemétododevemoscolocarnossasregrasdenegócio,comoacriaç ãodeuma
dataouatualizaç ãodeumajáexistente,algumtipodevalidaç ãoparaverificarsea
datapertenceaumperíodoválidoetc.Alémdissoéimportanteexibirparaousuá-
rio,atítulodeinformaç ão,qualfoiadataselecionada. Emnossaimplementaç ão,
recuperamososvaloresdeano,mêsediainformadoseatualizamosotextodobotão
paraapresentarcomorespostaaousuário.Agorajátemosasele çãodadatadogasto
funcionando!
@Override
protected Dialog onCreateDialog(int id) {
if(R.id.data == id){
return new DatePickerDialog(this, listener, ano, mes, dia);
}
return null;
}
private OnDateSetListener listener = new OnDateSetListener() {
@Override
public void onDateSet(DatePicker view,
int year, int monthOfYear, int dayOfMonth) {
ano = year;
mes = monthOfYear;
dia = dayOfMonth;
dataGasto.setText(dia + "/" + (mes+1) + "/" + ano);
}
};
Agoraqueasnossasdatasfuncionamejápermitimosaescolhadela,podemos
voltaraolayoutdo gasto.xml. Aindadentrodo LinearLayout,adicionamos
osdoiscamposparaadescriç ãoeolocaleumbotãoparacadastrarogasto:
<TextView
82

## Página 85

CasadoCódigo Capítulo3. DomineosprincipaiselementosdeInterfaceGráfica
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:text="@string/descricao" />
<EditText
android:id="@+id/descricao"
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:inputType="text" />
<TextView
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:text="@string/local" />
<EditText
android:id="@+id/local"
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:inputType="text" />
<Button
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:onClick="registrarGasto"
android:text="@string/gastei" />
83

## Página 86

3.5. Spinner CasadoCódigo
Figura3.7:Sele çãodedatascomDatePickerDialog
Classes anônimas
Paraosdesenvolvedoresqueaindanãoestãoacostumadoscoma
sintaxedoJava, écomumestranharadefiniç ãodeclassesanônimas.
Existemdiversosartigosnainternetqueexplicamcomocompreendê-
las e quando usar, sendo que uma das explicações mais comenta-
dasestádisponívelnoblogdaCaelum,em http://blog.caelum.com.br/
classes-aninhadas-o-que-sao-e-quando-usar/
3.5 Spinner
Nateladeregistrodegastosvamosincluirum widgetparasele çãodeitensemuma
listasuspensa. Conhecidoemoutrasplataformascomo combo boxou drop-down,
noAndroideste widgetédenominadode spinner.
Nanossaaplicaç ão,gostaríamosdeclassificarnossosgastosentrealimentaç ão,
hospedagem,combustíveletc.Paraisto,vamosdeclararum spinnereespecifica-
remosoatributo android:promptquerepresentaotítuloqueseráapresentando
quandoalistadeop çõesforaberta.
<TextView
84

## Página 87

CasadoCódigo Capítulo3. DomineosprincipaiselementosdeInterfaceGráfica
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:text="@string/categoria" />
<Spinner
android:id="@+id/categoria"
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:prompt="@string/categoria" >
</Spinner>
Notequenadeclaraç ãodo spinnernãoinformamosquaissãoasop çõesdis-
poníveis.Istoporquecadaitemdo Spinneréuma view-filhaqueéproveniente
deum SpinnerAdapter.Portantodevemoscarregarositenspreviamenteemum
SpinnerAdaptereatribuí-loao spinnerparaqueasop çõespossamserexibidas.
Já estão disponíveis na plataforma Android o ArrayAdapter e o
SimpleAdapter que podem ser utilizados para criar os itens dospinner.
Utilizaremosnestemomentoo ArrayAdapterquepermite,porexemplo,carregar
diretamenteumalistadeop çõesdefinidasemumarquivoderecurso. Então,no
arquivo strings.xml,definimosumarrayde stringscomascategoriasdesejadas,
daseguintemaneira:
1 <string-array name="categoria_gasto">
2 <item>Alimentação</item>
3 <item>Combustível</item>
4 <item>Transporte</item>
5 <item>Hospedagem</item>
6 <item>Outros</item>
7 </string-array>
No método onCreate da GastoActivity, criamos um novo
ArrayAdaptere o atribuímos aospinnerde categorias conforme o código
abaixo:
1 private Spinner categoria;
2 @Override
3 protected void onCreate(Bundle savedInstanceState) {
4 super.onCreate(savedInstanceState);
5 setContentView(R.layout.gasto);
6
85

## Página 88

3.5. Spinner CasadoCódigo
7 // busca a data atual para mostrar no botão
8
9 ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(
10 this, R.array.categoria_gasto,
11 android.R.layout.simple_spinner_item);
12 categoria = (Spinner) findViewById(R.id.categoria);
13 categoria.setAdapter(adapter);
14 }
Paracriaro ArrayAdapterutilizamosométodo createFromResource,
passandoocontextoatual,oidentificadordoarraydeop çõesquedefinimosno
strings.xmleoiddolayoutqueseráutilizadoparaapresentarasop ções.Mais
umaveznosbeneficiamosdoqueestádisponívelnaplataformaeutilizamosolayout
android.R.layout.simple_spinner_itemjádefinido.Executeaaplicaç ãoe
vejao spinnerfuncionando.
Figura3.8:UsodoSpinnereSpinnerAdapter
86

## Página 89

CasadoCódigo Capítulo3. DomineosprincipaiselementosdeInterfaceGráfica
3.6 ListViews
Comastelasdecriaç ãodeumanovaviagemeregistrodegastoscriadas,precisamos
dealgumaformalistarasviagensegastosrealizadosparaquepossamosverosdeta-
lhesetambémrealizaroutrasoperaçõescomoeditareremover.Paraimplementar
estafuncionalidadeutilizaremoso widget ListViewquetemacapacidadedeexibir
itensemumalistagem.Osprotótiposdanossalistagemdeviagensedegastossão
osseguintes:
Figura3.9:Listagensdeviagensegastos
Aoacessaraop çãoMinhasViagens,seráapresentadaumalistadeviagensca-
dastradaseaoselecionarumitemdalista,ousuáriopoderávisualizarosgastosre-
alizadosnaquelaviagememoutralistagem.
Comoanecessidadedecriaressestiposdelistagensébastantefrequente,apla-
taformaAndroidprovêalgumasfacilidadesparaasuacriaç ãoatravésdeumtipoes-
pecialdeatividade,a ListActivity.Estaclassejápossuium widget ListView
associadobastandoqueaelesejaatribuídoum ListAdapterparaproverositens
87

## Página 90

3.6. ListViews CasadoCódigo
queserãoexibidosnalista,seguindoamesmaideiado Spinner.Comisso,pode-
mosinclusiveutilizarum ArrayAdapterquealémdainterface SpinnerAdapter
tambémimplementa ListAdapter.
Podemosentãoterumanovaclassechamada ViagemListActivityquealém
deherdarde ListActivity,tambémimplemente OnItemClickListenercom
oobjetivodetrataroeventodisparadoquandoumitemdalistaéselecionado:
public class ViagemListActivity extends ListActivity
implements OnItemClickListener {
}
Nométodo onCreate,temosquecriarumnovo ArrayAdapterpassandoo
layoutdesejadoeositens.Tambémrecuperamosa ListViewassociada,atravésdo
método getListViewqueganhamosporcontadaheran ça. Aessa ListView,
atribuímosum listenerqueéaprópriaatividade,jáquefizemosnossaclasseimple-
mentar OnItemClickListener.
@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setListAdapter(new ArrayAdapter<String>(this,
android.R.layout.simple_list_item_1, listarViagens()));
ListView listView = getListView();
listView.setOnItemClickListener(this);
}
private List<String> listarViagens() {
return Arrays.asList("São Paulo", "Bonito", "Maceió");
}
Repare que utilizamos um layout padrão do Android,
android.R.layout.simple_list_item_1, como o layout da linha da
ListView. Alémdisso,ébemverdadequeositensdalista,ouseja,asviagens
realizadas,deveriamestararmazenadosemumbancodedadoseseremrecuperados
deláparaexibiç ão. Noentanto,nestemomentoestamospreocupadosapenasem
montarastelaseaslógicasdenavegaç ão. Nospreocuparemoscompersistência
nopróximocapítulo,quandorevisitaremosestaatividadeparaincluiroscódigos
definitivos.
88

## Página 91

CasadoCódigo Capítulo3. DomineosprincipaiselementosdeInterfaceGráfica
Quandoumaviagemdalistaforselecionada,gostaríamosdenavegarparaa
lista de gastos realizados durante aquela viagem. Implementamos isto no mé-
todo onItemClick,queéométodode OnItemClickListenerinvocadopela
ListViewquandoumiteméescolhido.Nestemomento,apresentamosadescriç ão
doitemselecionadoapenasparaefeitodedepuraç ãoeiniciamosaatividaderefe-
renteàlistagemdegastos.
@Override
public void onItemClick(AdapterView<?> parent, View view, int position,
long id) {
TextView textView = (TextView) view;
String mensagem = "Viagem selecionada: " + textView.getText();
Toast.makeText(getApplicationContext(), mensagem,
Toast.LENGTH_SHORT).show();
startActivity(new Intent(this, GastoListActivity.class));
}
Para esta listagem de gastos, precisaremos criar outra atividade, a
GastoListActivity,queserábastantesimilaràqueacabamosdeimplementar,
veja:
1 public class GastoListActivity extends ListActivity
2 implements OnItemClickListener {
3
4 @Override
5 protected void onCreate(Bundle savedInstanceState) {
6 super.onCreate(savedInstanceState);
7
8 setListAdapter(new ArrayAdapter<String>(this,
9 android.R.layout.simple_list_item_1, listarGastos()));
10 ListView listView = getListView();
11 listView.setOnItemClickListener(this);
12 }
13
14 @Override
15 public void onItemClick(AdapterView<?> parent, View view,
16 int position, long id) {
17 TextView textView = (TextView) view;
18 Toast.makeText(this,"Gasto selecionado: " + textView.getText(),
19 Toast.LENGTH_SHORT).show();
20 }
89

## Página 92

3.6. ListViews CasadoCódigo
21
22 private List<String> listarGastos() {
23 return Arrays.asList("Sanduíche R$ 19,90",
24 "Táxi Aeroporto - Hotel R$ 34,00",
25 "Revista R$ 12,00");
26 }
27 }
Novamenteutilizamosum ArrayAdaptereummétodoparasimularare-
cuperaçãodositensquedevemserexibidos. Independentementedaviagemque
foiescolhida,osgastosapresentadossãosempreosmesmos.Nãosepreocupecom
issoagora,poisiremosrefatoraressescódigosefazerocarregamentodosgastosde
acordocomaviagemselecionada, diretamentedobancodedados.Aoexecutara
atividade ViagemListActivityeescolherumitemdalista,teremososeguinte
resultado:
Figura3.10:Listagemdeviagensegastos
Apesardetersidosimplesdeimplementareseremplenamentefuncionais,nos-
saslistagensnãotêmumvisualelegante.Masistonãoéumproblema,poispodemos
customizarnossas ListViewsedeixá-lascomumaaparênciamaisrica.Oquefa-
remosagoraéincluirumaimagemparadiferenciarotipodaviagemassimcomo
incluirinformaçõesdoperíodoeototaldosgastosrealizados. Paraalistagemde
gastosdestacaremosascategoriascomcoresdiferentesefaremosumagrupamento
pordata.Oprotótipoaseguirservecomoreferênciaparaimplementaç ão:
90

## Página 93

CasadoCódigo Capítulo3. DomineosprincipaiselementosdeInterfaceGráfica
Figura3.11:Protótipodelistagenspersonalizadas
Anteriormentefizemosusoda ListActivityquejápossuiuma ListView
associada, cujolayoutconsistesimplesmentedeum TextView. Paralistagens
personalizadasprecisamosdefinirumlayoutconformeodesejadoeatribuí-loà
ListView. Para isso, crie um novo arquivo XML de layout com o nome de
lista_viagem.xml.
Nesselayout,vamosadicionarum LinearLayoutcomorientaçãohorizontal,
poisnossatelaédivididaemumlado,esquerdo,paraaimagemeoutroladoparaos
dadosdaviagem.
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
xmlns:android="http://schemas.android.com/apk/res/android"
android:layout_width="match_parent"
android:layout_height="match_parent"
android:orientation="horizontal">
<!-- adicionaremos os outros componentes aqui -->
91

## Página 94

3.6. ListViews CasadoCódigo
</LinearLayout>
No primeiro elemento dentro desse layout horizontal, faremos um outro
LinearLayoutdessa vez com orientação vertical, onde teremos a imagem de
acordocomotipodaviagem.
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout ...>
<LinearLayout
android:layout_width="wrap_content"
android:layout_height="match_parent"
android:gravity="center"
android:orientation="vertical" >
<ImageView
android:id="@+id/tipoViagem"
android:layout_width="wrap_content"
android:layout_height="wrap_content" />
</LinearLayout>
<!--
ainda faltam aqui os componentes do lado direito
com os dados das viagens
-->
</LinearLayout>
E para finalizar, outro LinearLayout com orientação vertical com 3
TextViewparamostrarodestino,dataegastodaviagem.
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout ...>
<!-- aqui está o LinearLayout com a ImageView dentro -->
<LinearLayout
android:layout_width="wrap_content"
android:layout_height="match_parent"
android:layout_marginLeft="10dp"
android:orientation="vertical" >
92

## Página 95

CasadoCódigo Capítulo3. DomineosprincipaiselementosdeInterfaceGráfica
<TextView
android:id="@+id/destino"
android:layout_width="wrap_content"
android:layout_height="wrap_content" />
<TextView
android:id="@+id/data"
android:layout_width="wrap_content"
android:layout_height="wrap_content" />
<TextView
android:id="@+id/valor"
android:layout_width="wrap_content"
android:layout_height="wrap_content" />
</LinearLayout>
</LinearLayout>
Quandosetrabalhacomlistagenspersonalizadaséimportantedefiniroidenti-
ficadordos widgetsqueirãoexibirainformaç ãopoisseránecessáriomanipulá-los
na activity. Reparequenãodefinimosnenhumtextoparaos TextViewse
nemumaimagemparao ImageViewpoisseusvaloresserãodefinidosemtempo
deexecução,deacordocomalinhaaserexibida.
Naclasse ViagemListActivityiremossubstituiro ArrayAdapterqueusa-
mosnométodo onCreate,quenãosuportaolayoutcustomizadosquedefinimos,
porum SimpleAdapter.Este adapterébastanteversátil,poispermitefazeruma
correlaçãoentreosdadoseos widgetsquedevemexibi-los,permitindoousode
layoutsarbitrários,tantoem ListViewsquantoem Spinners.
Paracriarum SimpleAdapterénecessárioinformarum Arrayde String
com as chaves que serão utilizadas para recuperar os dados, juntamente de
umoutro Arraycomosidentificadoresdos widgets(osmesmosdefinidosno
lista_viagem.xml)queexibirãoosdados.Oselementosdos arrayssãocor-
relacionados,ouseja,osdadosarmazenadoscomachave“imagem”devemserexi-
bidospelo widgetcomidentificador R.id.tipoViagem.Dessaforma,ométodo
onCreateserámodificadoparaficarcomo:
@Override
protected void onCreate(Bundle savedInstanceState) {
93

## Página 96

3.6. ListViews CasadoCódigo
super.onCreate(savedInstanceState);
String[] de = {"imagem", "destino", "data", "total"};
int[] para = {R.id.tipoViagem, R.id.destino, R.id.data, R.id.valor};
SimpleAdapter adapter =
new SimpleAdapter(this, listarViagens(),
R.layout.lista_viagem, de, para);
setListAdapter(adapter);
getListView().setOnItemClickListener(this);
}
Éprecisoalterarométodo listarViagenspararetornarumalistaqueserá
utilizadapelo SimpleAdaptercomasinformaçõesaseremexibidas.Alistaéfor-
madaporumconjuntodemapas,cujaschavesdevemserosidentificadoresdefinidos
no String[] de.
public class ViagemListActivity extends ListActivity
implements OnItemClickListener {
private List<Map<String, Object>> viagens;
private List<Map<String, Object>> listarViagens() {
viagens = new ArrayList<Map<String,Object>>();
Map<String, Object> item = new HashMap<String, Object>();
item.put("imagem", R.drawable.negocios);
item.put("destino", "São Paulo");
item.put("data","02/02/2012 a 04/02/2012");
item.put("total","Gasto total R$ 314,98");
viagens.add(item);
item = new HashMap<String, Object>();
item.put("imagem", R.drawable.lazer);
item.put("destino", "Maceió");
item.put("data","14/05/2012 a 22/05/2012");
item.put("total","Gasto total R$ 25834,67");
viagens.add(item);
94

## Página 97

CasadoCódigo Capítulo3. DomineosprincipaiselementosdeInterfaceGráfica
return viagens;
}
}
Observe também que incluímos para a chave imagem o valor
R.drawable.negocios que é o identificador da imagem que deve ser utili-
zadapelo ImageView,mapeadono int[] para como R.id.tipoViagem.
Lembre-sedeterasimagensnoseudiretório drawable.
O SimpleAdapter,emtempodeexecuç ão,decidecomofazero binddosdados
informadosdeacordocomotipode viewfornecido.Os widgetssuportadospelo
SimpleAdaptersãoaquelesqueimplementamainterface Checkable,comoo
TextVieweo ImageView.Noentanto,épossívelfazeraatribuiç ãodedadospara
outrostiposde views,implementandoum ViewBinder.Faremosalgoassimpara
alistagemdegastos.
Porfim,faltouapenasajustarométodo onItemClickpararecuperaraviagem
deacordocomaposiç ãoselecionadanatelaeexibiratravésdo Toast.makeText
umainformaçãosobreessaviagem.Comisso,ocódigodométodoficará:
public class ViagemListActivity extends ListActivity
implements OnItemClickListener {
private List<Map<String, Object>> viagens;
@Override
public void onItemClick(AdapterView<?> parent,
View view, int position, long id) {
Map<String, Object> map = viagens.get(position);
String destino = (String) map.get("destino");
String mensagem = "Viagem selecionada: "+ destino;
Toast.makeText(this, mensagem, Toast.LENGTH_SHORT).show();
startActivity(new Intent(this, GastoListActivity.class));
}
// métodos listarViagens e onCreate
}
Agoraseexecutarmosaaplicaç ãovamosteralistagempersonalizadadeviagens.
95

## Página 98

3.6. ListViews CasadoCódigo
Figura3.12:Listadeviagenspersonalizada
Aversãopersonalizadadalistagemdegastosdeveexibirositensdalistaemcores
diferentes,deacordocomacategoria.Alémdisso,osgastosdevemestaragrupados
pordata,paramelhoraraorganizaç ãoeausabilidade.
Continuaremosutilizandoo SimpleAdapterparaalimentara ListViewe
criaremosumaimplementaçãodainterface ViewBinderpararealizaro bindentre
osdadoseos widgetsdolayoutdaformaquedesejamos.
O ViewBinderseráoresponsávelporidentificarquaisgastossãodamesma
dataeexibirumseparadorna ListViewparaagrupá-los.Alémdisso,deacordo
comacategoria,o ViewBinderiráalteraracordefundodoitemdalistagem.
Vamoscriarumnovolayoutnoarquivo lista_gasto.xmlcomadefiniçãodeum
LinearLayoutcomorientaçãovertical,queconteráum TextViewparamostrar
adatadaviagem:
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
android:layout_width="match_parent"
android:layout_height="match_parent"
android:background="@color/titulo"
android:orientation="vertical" >
<TextView
android:id="@+id/data"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_gravity="right"
android:textColor="@android:color/white"/>
</LinearLayout>
96

## Página 99

CasadoCódigo Capítulo3. DomineosprincipaiselementosdeInterfaceGráfica
Valeressaltarnovamenteque,comoprecisaremosmanipularos widgetsviacó-
digoJava,énecessárioqueosmesmospossuamum id,inclusiveo LinearLayout
poisasuacordefundoseráalteradaemtempodeexecuç ãodeacordocomacate-
goria.
Porfim,adicionamostambémoutro LinearLayoutcomdois TextViewpara
exibiradescriç ãoeocustodaviagem:
<LinearLayout ...>
<!-- TextView para a data -->
<LinearLayout
android:id="@+id/categoria"
android:layout_width="match_parent"
android:layout_height="match_parent"
android:orientation="vertical" >
<TextView
android:id="@+id/descricao"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:textColor="@android:color/black" />
<TextView
android:id="@+id/valor"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:textColor="@android:color/black" />
</LinearLayout>
</LinearLayout>
Paramanternossocódigoorganizadoeparafacilitaralteraçõesposteriores,ire-
mosexternalizaroesquemadecoresutilizadonalistagem,assimcomofazemos
comas strings. OAndroidpermiteautilizaç ãoedefiniç ãodecoresemarqui-
vosderecurso.Então,vamoscriarnodiretório res/valuesumarquivochamado
colors.xml.Ascoresforamdefinidasdaseguintemaneira:
1 <?xml version="1.0" encoding="utf-8"?>
2 <resources>
3
97

## Página 100

3.6. ListViews CasadoCódigo
4 <color name="titulo">#015488</color>
5 <color name="categoria_alimentacao">#9FC5F8</color>
6 <color name="categoria_hospedagem">#6FA8DC</color>
7 <color name="categoria_transporte">#0099CC</color>
8 <color name="categoria_outros">#ACBFD5</color>
9
10 </resources>
Nome do arquivo de cores
Nãoexisteumaregrasobreonomedoarquivoser colors.xml,
vocêpoderiausarqualqueroutronome. Noentanto,éconvencionado
queumarquivoquecontenhaadefiniç ãodascoresaseremusadasnuma
aplicaçãoAndroidteráessenome.
AscoresestãonoformatoRGBcodificadasemhexadecimal.Onomeatribuído
àcorsetornaráoseuidentificador,sendopossívelacessá-laviaclasse R,comopor
exemplo, R.color.categoria_alimentacao. Valelembrarque,assimcomo
as stringse drawables,ascoresdevemseracessadasviaaAPIderecursosdo
Android.
Começamoscriandoos Arraysdentrodométodo onCreateparautilizarmos
o SimpleAdaptertambémna GastoListActivity:
public class GastoListActivity extends ListActivity
implements OnItemClickListener {
@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
String[] de = { "data", "descricao", "valor", "categoria" };
int[] para = { R.id.data, R.id.descricao,
R.id.valor, R.id.categoria };
SimpleAdapter adapter = new SimpleAdapter(this,
listarGastos(), R.layout.lista_gasto, de, para);
setListAdapter(adapter);
98

## Página 101

CasadoCódigo Capítulo3. DomineosprincipaiselementosdeInterfaceGráfica
getListView().setOnItemClickListener(this);
}
}
Agoraprecisamosdaimplementaç ãodométodo listarGastos,quedevolve
umalistacontendomapascomaspropriedadesaseremusadas:
public class GastoListActivity extends ListActivity
implements OnItemClickListener {
private List<Map<String, Object>> gastos;
// método onCreate aqui
private List<Map<String, Object>> listarGastos() {
gastos = new ArrayList<Map<String, Object>>();
Map<String, Object> item = new HashMap<String, Object>();
item.put("data", "04/02/2012");
item.put("descricao", "Diária Hotel");
item.put("valor", "R$ 260,00");
item.put("categoria", R.color.categoria_hospedagem);
gastos.add(item);
// pode adicionar mais informações de viagens
return gastos;
}
}
Eométodo onItemClickusandoanovalistadegastosparaexibirainforma-
çãoquandoclicada.
public class GastoListActivity extends ListActivity
implements OnItemClickListener {
// atributos, método onCreate e listarGastos
@Override
public void onItemClick(AdapterView<?> parent, View view,
int position, long id) {
Map<String, Object> map = gastos.get(position);
99

## Página 102

3.6. ListViews CasadoCódigo
String descricao = (String) map.get("descricao");
String mensagem = "Gasto selecionada: " + descricao;
Toast.makeText(this, mensagem,Toast.LENGTH_SHORT).show();
}
}
Agora,sónosrestafazero ViewBinder,queficaráresponsávelporidentificar
osgastosdamesmadata,exibiroseparadorna ListViewparatermosoagrupa-
mentoemudaracordefundodoitemdalistagem.
Acriaçãodo ViewBinderéfeitaatravésdeumanovaclassequeimplemente
essainterfacenaqualsedeveráimplementarométodo setViewValue.Eleretorna
um booleaneéchamadopelo SimpleAdapterparacadaelementodalistain-
formadaemsuacriaç ão.Paraele,sãopassadostrêsparâmetros:
•View-recuperadaapartirdeum idpassadono String para[];
•Object-queéovalorarmazenadocomachaveequivalenteao String
de[].
•String-umarepresentaç ãoemformatotextododadopassado( Object
data),queseráouoresultadodométodo toString()ouuma String
vazia,sendogarantidoqueseuvalorjamaisseránulo.
Portanto,podemoscriarumaclassenova,privada,em GastoListActivity,
queherdede ViewBinder:
public class GastoListActivity extends ListActivity
implements OnItemClickListener {
// atributos, método onCreate, listarGastos e onItemClick
private class GastoViewBinder implements ViewBinder {
@Override
public boolean setViewValue(View view, Object data,
String textRepresentation) {
// vamos implementar esse método
}
}
}
100

## Página 103

CasadoCódigo Capítulo3. DomineosprincipaiselementosdeInterfaceGráfica
Estemétododeveretornar truecasoo bindtenhasidorealizado. Casoore-
tornoseja false,o SimpleAdaptertentarárealizarobindautomaticamentepara
ostiposde viewssuportados( Checkable, TextViewe ImageView).Senãofor
possívelrealizaro binduma IllegalStateExceptionserálançada.
Parafazermosoagrupamento,temosqueverificarqualéa Viewqueestásendo
processada.
Casosejaadatadogasto,entãoprecisamoscomparartambémseestegastofoi
realizadonamesmadataprocessadaanteriormenteousefoiemumanovadata.
Sendoumadatadiferentedaanterior,entãodevemosexibiroseparador,quena
verdadeéapenasum TextViewcujovaloréadatadogasto. Casosejamiguais,
ouseja,osgastosforamrealizadosnamesmadata,entãotemosquesuprimiro
TextViewcom view.setVisibility(View.GONE), dando a impressão de
agrupamento.Outraop çãodevisibilidadeéa View.INVISIBLEporém,diferen-
tementedo View.GONE,a viewnãoéexibidamascontinuaocupandolugarno
layout.
Asegundacomparaç ãotratado LinearLayoutqueenglobatodasasinfor-
maçõesdosgastoseserefereàcategoria. Nestecaso,odadopassadoparaomé-
todoéopróprioidentificadordacorquedeveserutilizadacomocordefundodo
LinearLayout.
public class GastoListActivity extends ListActivity
implements OnItemClickListener {
// atributos, método onCreate, listarGastos e onItemClick
private String dataAnterior = "";
private class GastoViewBinder implements ViewBinder {
@Override
public boolean setViewValue(View view, Object data,
String textRepresentation) {
if(view.getId() == R.id.data){
if(!dataAnterior.equals(data)){
TextView textView = (TextView) view;
textView.setText(textRepresentation);
dataAnterior = textRepresentation;
view.setVisibility(View.VISIBLE);
} else {
101

## Página 104

3.6. ListViews CasadoCódigo
view.setVisibility(View.GONE);
}
return true;
}
if(view.getId() == R.id.categoria){
Integer id = (Integer) data;
view.setBackgroundColor(getResources().getColor(id));
return true;
}
return false;
}
}
}
Por fim, agora basta indicarmos no método onCreate da
GastoListActivity que o adapter usará oViewBinder que acabamos
decriar.Fazemosissoatravésdométodo setViewBinderdo adapter.
@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
String[] de = { "data", "descricao", "valor", "categoria" };
int[] para = { R.id.data, R.id.descricao,
R.id.valor, R.id.categoria };
SimpleAdapter adapter = new SimpleAdapter(this, listarGastos(),
R.layout.lista_gasto, de, para);
adapter.setViewBinder(new GastoViewBinder());
setListAdapter(adapter);
getListView().setOnItemClickListener(this);
}
102

## Página 105

CasadoCódigo Capítulo3. DomineosprincipaiselementosdeInterfaceGráfica
Figura3.13:Listapersonalizadadegastos
3.7 Menus
Osmenus,damesmamaneiraqueos dialogscomoo DatePickerDialog,sãoele-
mentosimportantesdeinteraç ãocomousuáriodoaplicativoepodemserutilizados
paralheapresentarop çõesquepodemsertantoglobais,quandodizemrespeitoa
umaconfiguraçãoouestadodaaplicaç ão,oucontextuaisquandoaop çãoestárela-
cionadacomalgumitemselecionado,porexemplo.
Atéaversão3.0doAndroid,eraobrigatórioqueosaparelhostivessemumbotão
menu,quequandopressionadoapresentavaumpainelcomnomáximoseisop ções
visíveis.Quandoexistiammaisdeseisop ções,eranecessárioselecionarumaop ção
“maisitens”paravisualizaroquerestava.Estetipodemenuéconhecidocomo op-
tions menu. Nosaparelhosmaisrecentesjánãoexistemaisobotão menuemuito
menosbotõesfísicos,excetoosdevolumeeparaligaroaparelho.
103

## Página 106

3.7. Menus CasadoCódigo
Menudeop ções
Geralmenteos options menusãoutilizadosparaapresentarop çõesquesãorele-
vantesparaa activityatualouparaaaplicaç ão. Criaremosentãoalgunsmenusde
opçãoparaalgumasdenossasatividades.
Podemoscome çarpela DashboardActivity,ondevamoscriarummenu
comaop çãodesairdaaplicaç ão. Emseguida,paraa ViagemActivitycriare-
mosummenucomaop çãoderegistrarumnovogastoeapagaraviagem.Jáparaa
GastoActivitycolocaremosummenucomaop çãoderemoverogasto.
Figura3.14:Menusdeop ções
OsmenussãodefinidosemarquivosXMLespecíficoscomoobjetivodeexterna-
lizaraestruturadomenudocódigodaaplicaç ão,alémdepermitirquesejamdefini-
dosdiferentesmenusparasuportardiferentesconfiguraçõesdeaparelhoseversões
doAndroid.Osarquivosdemenudevemficarnodiretório res/menu.Entãova-
moslá,vamoscriaromenuparao Dashboardnoarquivo dashbord_menu.xml,
comaseguintedefiniç ão:
1 <?xml version="1.0" encoding="utf-8"?>
2 <menu xmlns:android="http://schemas.android.com/apk/res/android">
3
4 <item
104

## Página 107

CasadoCódigo Capítulo3. DomineosprincipaiselementosdeInterfaceGráfica
5 android:id="@+id/sair"
6 android:icon="@android:drawable/ic_menu_close_clear_cancel"
7 android:title="@string/sair"/>
8
9 </menu>
OelementoraizdoXMLéo menuquepodeconterváriastags itemquerepre-
sentamasop çõesdomenu.Um itempodeterum
Os menus são efetivamente criados pelaactivity que está ativa quando
o botão menu é pressionado, e nesse momento, invoca-se o método
onCreateOptionsMenu. A própria activity também fornece um método
paratratarquandoumitemdomenuforselecionado,o onMenuItemSelected.
Vamoscome çarpelaimplementaçãodo onCreateOptionsMenu.
Ométodo onCreateOptionsMenurecebecomoparâmetroumobjetodotipo
Menu,noqualprecisamospopularasop çõesdeacordocomasinformaçõesdoXML
queacabamosdecriar,queseencontradentrode res/menus.Paraisso,épreciso
passarosdadosdoXMLparaoobjetorecebidocomoparâmetro,queéjustamente
opapeldeumaclassechamada MenuInflater.
Recuperamos uma instância dela através da chamada ao método
getMenuInflater para, em seguida, invocar seu métodoinflate, pas-
sandocomoparâmetroumareferênciaparaomenuatravésdaclasse Retambémo
objeto menu.Porfim,retornamos trueparaindicarqueomenudeveserexibido.
@Override
public boolean onCreateOptionsMenu(Menu menu) {
MenuInflater inflater = getMenuInflater();
inflater.inflate(R.menu.dashboard_menu, menu);
return true;
}
Como nosso menu só tem uma opção, que no caso é sair da aplicação,
não precisamos saber qual foi o item selecionado, então a implementação do
onMenuItemSelectedapenasinvocaométodo finishparaencerraraatividade
atual.Posteriormente,nestemétodotambémimplementaremoso logoffdousuário.
@Override
public boolean onMenuItemSelected(int featureId, MenuItem item) {
finish();
return true;
}
105

## Página 108

3.7. Menus CasadoCódigo
Paraa ViagemActivity,queéatelautilizadaparacriareeditarviagens,te-
remosum options menucomasop çõesderegistrarumnovogastoouremovera
viagem.Crieoarquivo viagem_menu.xmlcomadefiniçãoabaixo:
<?xml version="1.0" encoding="utf-8"?>
<menu xmlns:android="http://schemas.android.com/apk/res/android" >
<item
android:id="@+id/novo_gasto"
android:icon="@android:drawable/ic_menu_add"
android:title="@string/novo_gasto"/>
<item
android:id="@+id/remover"
android:icon="@android:drawable/ic_menu_delete"
android:title="@string/remover_viagem"/>
</menu>
Comonestemenutemosmaisdeumaop ção,éessencialdefiniridentificadores
paraosseusitensparaquesepossadeterminarqualfoioitemselecionado. Para
começar,faremosno onCreateOptionsMenuamesmatransformaçõesdosdados
doXMLparaoobjeto Menu.
@Override
public boolean onCreateOptionsMenu(Menu menu) {
MenuInflater inflater = getMenuInflater();
inflater.inflate(R.menu.viagem_menu, menu);
return true;
}
Nométodo onMenuItemSelectedcombaseno iddoitemselecionadode-
cidimosaaç ãoaserexecutada.Quandoaop çãoforreferenteaonovogasto,iremos
iniciaraatividade GastoActivityequandoforaderemover,iremosexcluiravi-
agematual.Casonãosejapossíveldeterminarqualitemfoiselecionado,invocamos
aimplementaçãopadrãodométodoqueretorna false.
@Override
public boolean onMenuItemSelected(int featureId, MenuItem item) {
switch (item.getItemId()) {
case R.id.novo_gasto:
startActivity(new Intent(this, GastoActivity.class));
106

## Página 109

CasadoCódigo Capítulo3. DomineosprincipaiselementosdeInterfaceGráfica
return true;
case R.id.remover:
//remover viagem do banco de dados
return true;
default:
return super.onMenuItemSelected(featureId, item);
}
}
Casoqueiraexercitar,crieporcontaprópriaummenucomaop çãoderemover
gastoparaa GastoActivity,aimplementaç ãoserásemelhanteàsrealizadasaté
omomento.
Nos options menus aindaháapossibilidadedeagruparitensatravésdatag
groupetambémdecriarsubmenus,aninhandoatag menu. Osgruposservem
parafacilitarocontroledeitensquesãorelacionados. Atravésdegruposépossí-
veldefiniravisibilidadedetodososseusitens,ouseestãoativosounão.Ocódigo
abaixoretiradodadocumentaç ãodoAndroidexemplificaousodegrupos:
<?xml version="1.0" encoding="utf-8"?>
<menu xmlns:android="http://schemas.android.com/apk/res/android">
<item android:id="@+id/menu_save"
android:icon="@drawable/menu_save"
android:title="@string/menu_save" />
<!-- menu group -->
<group android:id="@+id/group_delete">
<item android:id="@+id/menu_archive"
android:title="@string/menu_archive" />
<item android:id="@+id/menu_delete"
android:title="@string/menu_delete" />
</group>
</menu>
Ossubmenuspodemsercriadossimplesmenteincluindoumanovatag menu
comseusitensassociados. Issoéútilquandonossaaplicaç ãotemumconjunto
grandedeop çõesquepodemseragrupadasemassuntos.Porémtenhacuidadoao
utilizarmenuscommuitosníveisparanãoprejudicarausabilidadedaaplicaç ão.Um
exemplodesubmenuretiradotambémdadocumentaç ãodoAndroidéoseguinte:
1 <?xml version="1.0" encoding="utf-8"?>
2 <menu xmlns:android="http://schemas.android.com/apk/res/android">
107

## Página 110

3.7. Menus CasadoCódigo
3 <item android:id="@+id/file"
4 android:title="@string/file" >
5 <!-- "file" submenu -->
6 <menu>
7 <item android:id="@+id/create_new"
8 android:title="@string/create_new" />
9 <item android:id="@+id/open"
10 android:title="@string/open" />
11 </menu>
12 </item>
13 </menu>
MenusContextuais
EmaparelhosAndroid,quandoqueremosreenviarumamensagemSMSparaa
pessoacasoelanãotenharecebidooutenhahavidofalhanoenvio,nãoénecessário
terotrabalhoderedigitaressamensagemcompletamente.Opróprioaplicativode
mensagensdoAndroidnospermitereenviarumamensagemespecíficasegurando
sobreelaeescolhendoemummenuaop çãopararealizaroreenvio.Essemenuque
surgeeéespecíficoparaaquelamensageméoquechamamosde“MenudeContexto”,
vejaumexemplonaimagem 3.15.
108

## Página 111

CasadoCódigo Capítulo3. DomineosprincipaiselementosdeInterfaceGráfica
Figura3.15:Menudecontexto
Omenuscontextuaisoferecemaousuárioop çõesquesãorelevantesaocon-
teúdoqueestásendoapresentado. Porexemplo,aoselecionarumitemdeuma
ListView,podemosapresentarummenudecontextocomop çõesquefazemsen-
tidoparaaqueleitem,taiscomovisualizar,editar,compartilharetc.
Paraanossalistagemdegastos, criaremosummenucontextualquepermi-
tiráaousuárioremoverogastoselecionado. Acriaç ãodestetipodemenuési-
milar ao que já realizamos para o menu de opções. Devemos definir um ar-
quivoXMLcontendoasop çõesdomenu,construirasop çõesdomenusobrescre-
vendoométodo onCreateContextMenuetratarasele çãodousuárionométodo
onContextItemSelected.
Aúnicadiferen ça,alémdonomedosmétodos,éanecessidadederegistrar
a Viewqueiráapresentaromenudecontexto,quefazemosatravésdométodo
registerForContextMenu(View view). Então, nométodo onCreateda
GastoListActivity,vamosregistraromenudecontexto.
@Override
109

## Página 112

3.7. Menus CasadoCódigo
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
String[] de = { "data", "descricao", "valor", "categoria" };
int[] para = { R.id.data, R.id.descricao,
R.id.valor, R.id.categoria };
SimpleAdapter adapter = new SimpleAdapter(this, listarGastos(),
R.layout.lista_gasto, de, para);
setListAdapter(adapter);
getListView().setOnItemClickListener(this);
// registramos aqui o novo menu de contexto
registerForContextMenu(getListView());
}
Paraanossalistagemdegastos,comoaúnicaop çãodisponívelnomenude
contextoseráaderemover,criaremosumnovoXMLdelayoutcomonomede
gasto_menu.xml:
<?xml version="1.0" encoding="utf-8"?>
<menu xmlns:android="http://schemas.android.com/apk/res/android" >
<item
android:id="@+id/remover"
android:icon="@android:drawable/ic_menu_delete"
android:title="@string/remover"/>
</menu>
Fazemosométodo onCreateContextMenuparalerasop çõesdoXMLe
transformá-lasemumobjetodotipo ContextMenu:
@Override
public void onCreateContextMenu(ContextMenu menu , View v,
ContextMenuInfo menuInfo) {
MenuInflater inflater = getMenuInflater();
inflater.inflate(R.menu.gasto_menu, menu);
}
Emseguida,precisamosreescreverométodo onContextItemSelected,que
recebeoitemdomenuquefoiselecionado,pararealizarmosaaç ãoadequada,no
caso,fazeraremo ção.
110

## Página 113

CasadoCódigo Capítulo3. DomineosprincipaiselementosdeInterfaceGráfica
Pararecuperarinformaçõessobreoitemdomenuquefoiselecionado, uti-
lizamos o método item.getMenuInfo() que retorna um objeto do tipo
AdapterContextMenuInfo,queforneceo iddalinhaquefoiselecionada,apo-
siçãodoitemno adapterea viewquefoiselecionada.
Comisso,utilizamosainformaç ãodaposiç ãopararemoveroitemdalistade
gastos. Noentanto,essaoperaçãonãoérefletidaautomaticamentena ListView
quejárenderizouaslinhasnatela.Énecessáriofazercomquea ListViewdesenhe
aslinhasnovamentecombaseno adapterqueagoratemumitemamenos. Istoé
feitoinvocandoométodo invalidateViews().
@Override
public boolean onContextItemSelected(MenuItem item) {
if (item.getItemId() == R.id.remover) {
AdapterContextMenuInfo info = (AdapterContextMenuInfo) item
.getMenuInfo();
gastos.remove(info.position);
getListView().invalidateViews();
dataAnterior = "";
// remover do banco de dados
return true;
}
return super.onContextItemSelected(item);
}
Pronto,agoratemosanossaaplicaç ãocomomenudecontextosfuncionando.
Embreve,integraremoscomobancodedadosdeverdade.
3.8 AlertD ialog
Alémdosmenus,podemosapresentarop çõesparaousuárioatravésdecaixasde
diálogoquesãoutilizadasgeralmenteparainteragircomousuário,apresentando
algumtipodeinformaç ãoesolicitandoqueeledecidaoquedeveserfeito.
Podemosutilizar,porexemplo,umacaixadediálogosolicitandoaousuárioa
confirmaçãodaexclusãodeumainformaç ãoouexibirumamensagemdequede-
terminadaaçãofoirealizada.Os AlertDialogspodemconteratétrêsbotõesou
aindaumalistadeitensselecionáveisatravésde checkboxesou radio buttons,tor-
nandovariadasasformasdeinteraç ãocomousuário.Aimagem 3.16exemplificao
usodeumacaixadediálogoparaconfirmaraexclusãodeumafoto.
111

## Página 114

3.8. AlertDialog CasadoCódigo
Figura3.16:AlertDialog
Nanossaaplicaç ão,quandoousuárioselecionarumaviagemnalistagem“Mi-
nhasViagens”,queremosapresentarasopçõesdeeditar,registrarumnovogasto,
visualizarosgastosjárealizadoseremoveraviagemselecionada. Comojávimos
anteriormente,poderíamoscriarummenudecontextopararesolveressaquestão.
Noentanto,paraabriromenudecontextoousuárioprecisaselecionarumitem
emantê-lopressionadoatéaexibiçãodasop ções,oquetornaainteraç ãomaislenta
e,emsetratandodefuncionalidadesqueserãomuitoutilizadas,podeacabarpreju-
dicandoausabilidade. Seriamelhorse,aoselecionarumitemdalista,omenude
opçõesfosseimediatamenteapresentado.Estecomportamentoéobtidoimplemen-
tandoomenucomasop çõescomoumacaixadediálogo.
O AlertDialogécriadoatravésdeum AlertDialog.Builder,noqual
informaremosotítulodacaixadediálogoeosseusitens. Tambéménecessário
fornecerum OnClickListenerparatratardaop çãoescolhidapelousuário.Nossa
ViagemListActivityjáimplementaainterface OnItemClickListenerpara
capturarocliquedeumitemna ListVieweagoradeveráimplementarainterface
112

## Página 115

CasadoCódigo Capítulo3. DomineosprincipaiselementosdeInterfaceGráfica
OnClickListenereseumétodo onClickparatrataraop çãoselecionadapelo
usuárionacaixadediálogo.
public class ViagemListActivity extends ListActivity
implements OnItemClickListener, OnClickListener {
@Override
public void onClick(DialogInterface dialog, int item) {
// Vamos implementar esse método
}
}
Agoravamoscriarummétodochamado criaAlertDialog,ondedefinire-
mosum Arraycomasop çõesqueserãoexibidasnacaixadediálogo.Essemétodo
retornaráo AlertDialogconstruídocomasop ções.
private AlertDialog criaAlertDialog() {
final CharSequence[] items = {
getString(R.string.editar),
getString(R.string.novo_gasto),
getString(R.string.gastos_realizados),
getString(R.string.remover) };
AlertDialog.Builder builder = new AlertDialog.Builder(this);
builder.setTitle(R.string.opcoes);
builder.setItems(items, this);
return builder.create();
}
Agora,quandoa ViagemListActivity%forcriada,éprecisoadicionaro
AlertDialogtambém,assim,poderemosusá-loquandofornecessário.Paraisso,
vamosacrescentarumachamadaao criaAlertDialogno onCreateda activity:
protected void onCreate(Bundle savedInstanceState) {
// Realiza as outras ações
this.alertDialog = criaAlertDialog();
}
Guardamosa referênciapara odialog criado, numatributo deinstância da
ViagemListActivityquechamamosde alertDialog.
113

## Página 116

3.8. AlertDialog CasadoCódigo
public class ViagemListActivity extends ListActivity
implements OnItemClickListener, OnClickListener {
private AlertDialog alertDialog;
// outros atributos e métodos
}
Nométodosobrescrito onClick,utilizaremosoíndicedo Arraydositensdo
AlertDialogparadeterminarqualop çãofoiselecionadaeexecutaremosaaç ão
apropriada. Paraqueo AlertDialogfuncionedeformasimilaraummenude
contextoetambémtenhaaop çãopararealizaraexclusãodaviagem,precisaremos
manterumareferênciaparaoitemda ListViewquefoiselecionado.Issoéfeito
nométodosobrescrito onItemClick,quearmazenaaposiç ãodoitemselecionado
esóentãoabreacaixadediálogoinvocando alertDialog.show(). Quandoa
opção“remover”dacaixadediálogoéselecionada,utilizamosaposiçãopreviamente
armazenadapararemoveraviagemda ListView.
1 @Override
2 public void onClick(DialogInterface dialog, int item) {
3 switch (item) {
4 case 0:
5 startActivity(new Intent(this, ViagemActivity.class));
6 break;
7 case 1:
8 startActivity(new Intent(this, GastoActivity.class));
9 break;
10 case 2:
11 startActivity(new Intent(this, GastoListActivity.class));
12 break;
13 case 3:
14 viagens.remove(this.viagemSelecionada);
15 getListView().invalidateViews();
16 break;
17 }
18 }
19
20 @Override
21 public void onItemClick(AdapterView<?> parent,
22 View view, int position,
23 long id) {
114

## Página 117

CasadoCódigo Capítulo3. DomineosprincipaiselementosdeInterfaceGráfica
24 this.viagemSelecionada = position;
25 alertDialog.show();
26 }
Notequeprecisamosterumnovoatributona ViagemListActivitypara
guardaraviagemselecionada.
private int viagemSelecionada;
Pronto.Agoratemosumaversãodemenudecontextomuitomaisresponsiva.
Executeaaplicaçãoeconfira!
Figura3.17:MenuutilizandoAlertDialog
AlertDialogscomconfirmações
Geralmenteoperaçõescríticasdaaplicaç ãorequeremaconfirmaç ãodousuá-
rio.Éocasoporexemplodaexclusãodeumaviagemoudeumgastorealizado.As
caixasdediálogodeconfirmaç ão,combotões“sim/não”,sãoimplementadasutili-
zando AlertDialogs.Vamosalterarnossocódigoparasolicitaraconfirmaç ãodo
usuáriopararemoverumaviagem. Sóapósestaconfirmaç ãoéqueaviagemserá
removida.
Seránecessáriocriarumnovodiálogoqueincluaosbotõesparaaconfirmaç ão
ourejeiçãoepassarum listenerparatratarqualbotãofoiescolhido. Comonossa
115

## Página 118

3.8. AlertDialog CasadoCódigo
atividadejáimplementa onClickListenerutilizaremosométodojáexistente
como listenerdodiálogodeconfirmação.
Vamosfazerométodo criaDialogConfirmacao,queirácriaronovo dialog
comasop çõesdeconfirmaç ãoenegaç ão.
private AlertDialog criaDialogConfirmacao() {
AlertDialog.Builder builder = new AlertDialog.Builder(this);
builder.setMessage(R.string.confirmacao_exclusao_viagem);
builder.setPositiveButton(getString(R.string.sim), this);
builder.setNegativeButton(getString(R.string.nao), this);
return builder.create();
}
Repare na invocaç ão dos métodos setPositiveButton e
setNegativeButton que fazem os botões “Sim” e “Não”, respectivamente e
querecebema stringquedeveserexibidaparacadabotão.
Opróximopassoéinvocaro criaDialogConfirmacaono onCreateda
activityeguardarumareferênciaparaonovo AlertDialogemumatributode
instância:
// Novo atributo de instância
private AlertDialog dialogConfirmacao;
protected void onCreate(Bundle savedInstanceState) {
// Realiza as outras ações
this.alertDialog = criaAlertDialog();
this.dialogConfirmacao = criaDialogConfirmacao();
}
Nométodo onClick,quandoaop ção“remover”forselecionada,o::dialog:de
confirmaçãoseráexibidoeadicionamosasverificaçõesparadeterminarseobotão
pressionadofoireferenteao“sim”ouao“não”. Casoaescolhatenhasido“não”,a
remoçãonãoéconfirmadaenadadeveserfeito,excetofecharacaixadediálogo,o
quepodeserrealizadoatravésdométodo dismiss()dopróprio AlertDialog.
1 @Override
2 public void onClick(DialogInterface dialog, int item) {
3 switch (item) {
116

## Página 119

CasadoCódigo Capítulo3. DomineosprincipaiselementosdeInterfaceGráfica
4 case 0:
5 startActivity(new Intent(this, ViagemActivity.class));
6 break;
7 case 1:
8 startActivity(new Intent(this, GastoActivity.class));
9 break;
10 case 2:
11 startActivity(new Intent(this, GastoListActivity.class));
12 break;
13 case 3:
14 dialogConfirmacao.show();
15 break;
16 case DialogInterface.BUTTON_POSITIVE:
17 viagens.remove(viagemSelecionada);
18 getListView().invalidateViews();
19 break;
20 case DialogInterface.BUTTON_NEGATIVE:
21 dialogConfirmacao.dismiss();
22 break;
23 }
24 }
O AlertDialogcriadoficaráassim:
117

## Página 120

3.9. ProgressDialogeProgressBar CasadoCódigo
Figura3.18:AlertDialogcomconfirmaç ão
3.9 ProgressD ialog eProgressB ar
Semprequeumoperaç ãoquepodedemorarforexecutada,comofazerdownloadde
informaçõesdaInternet,éimportantemanterousuárioinformadosobreoqueestá
acontecendoequeaaplicaç ãocontinuafuncionando. Nessassituações,podemos
utilizarum ProgressDialogqueéumaextensãodo AlertDialog,eapresen-
taraousuárioumaanimaç ãorepresentandooprogressodaoperaç ão. Tambémé
possívelinformarumtítuloeumamensagemparaexibiç ão,alémdebotõespara
controlaraoperação,senecessário.
O ProgressDialogpodeterumaduraç ãoindeterminadaquandonãohápre-
visãodetérmino,oudeterminadaquandoaduraç ãotemumvalorconhecido.
Noprimeirocaso,éapresentadoaousuárioumaanimaç ãoemformatodecír-
culo.
Quandoo ProgressDialogtemduraçãodeterminada,umabarradepro-
gressoéapresentadaeépossívelacompanharoandamentodatarefaatravésdevalor
ouporcentagem.Confiranaimagemabaixoalgunsexemplosdeuso:
118

## Página 121

CasadoCódigo Capítulo3. DomineosprincipaiselementosdeInterfaceGráfica
Figura3.19:ExemplosdeProgressDialog
Ocódigoaseguirexemplificacomoexibirum ProgressDialogcomduração
indeterminadaequepodesercanceladopelousuárioquandoobotão“Voltar”do
aparelhoforpressionado:
boolean podeCancelar = true;
boolean indeterminado = true;
String titulo = "Operação demorada";
String mensagem = "Aguarde...";
ProgessDialog dialog = ProgressDialog.show(this, titulo, mensagem,
indeterminado, podeCancelar);
Quandoprecisamosindicaroprogressodaoperaç ãoparaousuário,aformade
criaro ProgressDialogéumpoucodiferente.
Utilizamosoconstrutor ProgressDialog(Context)edefinimosotítuloea
mensagematravésde setters.Énecessáriodefinirumestiloparaabarradeprogresso,
porexemplo ProgressDialog.STYLE_HORIZONTAL.Tambémpodemosdefinir
ovalormáximodabarradeprogressoque,aoseralcan çado,provocaofechamento
dacaixadediálogo.Atualizaçãodoprogressopodeserrealizadaatravésdosmétodos
setProgress(int)ou incrementProgressBy(int).
Vejaumcódigodeexemploquetambémincluibotões:
ProgressDialog dialog = new ProgressDialog(this);
dialog.setProgressStyle(ProgressDialog.STYLE_HORIZONTAL);
119

## Página 122

3.9. ProgressDialogeProgressBar CasadoCódigo
dialog.setTitle(titulo);
dialog.setMessage(mensagem);
dialog.setCancelable(true);
dialog.setMax(800);
dialog.setButton(Dialog.BUTTON_NEGATIVE,
getString(R.string.abortar), this);
dialog.setButton(Dialog.BUTTON_NEUTRAL,
getString(R.string.pausar), this);
dialog.setButton(Dialog.BUTTON_POSITIVE,
getString(R.string.continuar), this);
dialog.show();
Emalgumassituações,háapossibilidadedenãotermosumaoperaç ãoemanda-
mento,porémqueremosindicarparaousuáriooquãopróximoeleestádealcan çar
determinadovalorlimite.Nanossaaplicaç ãopodemos,porexemplo,utilizaruma
ProgressBarparaexibirototaldegastosrealizadosemrelaç ãoaoor çamentoes-
tipuladoparaaviagem.
Incluiremosessafuncionalidadenalistagemdeviagenseconsideraremosque
existeumvalorlimiteconfiguradoparaosgastosquepodesermaioroumenordo
queovalordoor çamento.Posteriormentecriaremosessaconfiguraç ãoenotificare-
mosousuárioquandoestevalorlimiteforalcan çado.
A ProgressBarpossuidoisvaloresdeprogresso,umprincipaleooutrose-
cundário. Utilizaremosoprincipalparaexibirosvalortotaldosgastosrealizados
eosecundárioparamarcarovalorlimite,seesteformenordoqueoor çamento.
Incluanolayout lista_viagem.xmladefiniçãodabarradeprogressoabaixodo
TextViewqueexibeovalordosgastosrealizados:
<ProgressBar android:id="@+id/barraProgresso"
android:layout_width="fill_parent"
android:layout_height="wrap_content"
style="?android:attr/progressBarStyleHorizontal"/>
Depois, precisaremos alterar aViagemListActivity para implementar
ViewBinderpoisagoratemosuma ProgressBarna ListView. Parapreen-
cherosvaloresdabarradeprogresso,passaremosum arraycomosvaloresde-
finidosparaoor çamento,olimiteeovalordosgastos,paraomapautilizadopelo
SimpleAdapter.
Oprimeiropasso,nométodo onCreateéadicionarumnovoitemnosArrays
dee para,quereferenciarãoabarradeprogressoqueacabamosdedefinirnolayout.
120

## Página 123

CasadoCódigo Capítulo3. DomineosprincipaiselementosdeInterfaceGráfica
@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
String[] de = { "imagem", "destino", "data",
"total", "barraProgresso" };
int[] para = { R.id.tipoViagem, R.id.destino,
R.id.data, R.id.valor, R.id.barraProgresso };
// restante da implementação
}
Emseguida,nométodo listarViagens,quedevolveasinforma çõesdasvi-
agensrealizadas,vamosdevolverasinformaçõesnecessáriasparaabarra,adicio-
nandoao Mapumanovainformação:
private List<Map<String, Object>> listarViagens() {
viagens = new ArrayList<Map<String, Object>>();
Map<String, Object> item = new HashMap<String, Object>();
item.put("imagem", R.drawable.negocios);
item.put("destino", "São Paulo");
item.put("data", "02/02/2012 a 04/02/2012");
item.put("total", "Gasto total R$ 314,98" );
item.put("barraProgresso", new Double[]{ 500.0, 450.0, 314.98});
viagens.add(item);
// adiciona mais informações se preferir
return viagens;
}
Porfim,temosquesobrescreverométodo setViewValue,noqualsãoatribuí-
dososvaloresdeprogressoprincipalesecundárioalémdovalormáximodabarra
deprogresso,representadoaquipelovalordefinidocomooor çamentodisponível
paraarealizaç ãodaviagem.
@Override
public boolean setViewValue(View view, Object data,
String textRepresentation) {
121

## Página 124

3.9. ProgressDialogeProgressBar CasadoCódigo
if (view.getId() == R.id.barraProgresso) {
Double valores[] = (Double[]) data;
ProgressBar progressBar = (ProgressBar) view;
progressBar.setMax(valores[0].intValue());
progressBar.setSecondaryProgress(valores[1].intValue());
progressBar.setProgress(valores[2].intValue());
return true;
}
return false;
}
Anovalistagemdeviagensexibindoa ProgressBarficaráassim:
Figura3.20:ListagemdeviagenscomProgressBar
122

## Página 125

CasadoCódigo Capítulo3. DomineosprincipaiselementosdeInterfaceGráfica
3.10 Preferências
Muitasvezeséinteressantequeousuárioconfigureocomportamentodoaplicativo
deacordocomasuapreferência.Issotornaoaplicativomuitomaisatrativoeperso-
nalizado.Maséclaroqueoesfor çoparadesenvolverumaplicativoaltamentecusto-
mizáveléenorme.Énecessárioparcimôniaeofereceraousuárioalgumasop ções-
chave. OAndroidoferecesuporteparaagravaç ãoearmazenamentodessasprefe-
rênciasbemcomouma PreferenceActivityparapermitirasuaediç ão.
Aspreferênciassãoarmazenadasemparescomumelementorepresentandoa
chave,queserviráparaasuaobten çãoposterior,eooutrorepresentandoovalor
dapreferência. Podemosutilizaressetipodearmazenamentonãosóparaaspre-
ferênciasdousuáriomastambémparaqualqueroutrotipodedadobásicoquea
aplicaçãopossanecessitar,comoporexemplooendere çodeumserviçoremotoou
informaçõescarregadasdaInternet.
Existeumarquivodepreferênciaspadrãoquepodeserutilizadopelaaplicaç ão,
equandonecessário,épossívelcriarváriosarquivosdepreferênciasparaarmazenar
informaçõesdistintas.Elestambémpodemsercriadospor Activity.
Nanossaaplicação,disponibilizaremosduasop çõesdepreferênciaparaousuá-
rio.Umaparaqueeleinformeumvalorpercentualdoor çamentodasviagens,que
quandoultrapassadopelototaldegastosrealizadosprovocaráumanotificaç ão,ea
outraqueconfiguraoaplicativoemum“ModoViagem”.Apropostaéquequando
estemodoestiverselecionadoeousuárioforregistrarumnovogasto,oaplicativose-
lecioneautomaticamente,combasenadataatual,aviagemdaqualogastoserefere,
emvezdeapresentarumalistagemparaqueousuárioselecioneaviagemcorreta.
ComooAndroidjáfacilitaaimplementaç ãodetelasdepreferências,disponibi-
lizandoelementosquejátratamdaapresentaç ãoegravaç ãodositens,criaremosum
arquivoXMLdiferentedosarquivosdelayoutcriadosatéomomento.Porquestões
deorganização,manteremosoarquivoXMLdaspreferênciasnodiretório res/xml.
Crienestapastaoarquivo preferencias.xml,comaseguintedefiniç ão:
<?xml version="1.0" encoding="utf-8"?>
<PreferenceScreen
xmlns:android="http://schemas.android.com/apk/res/android" >
<PreferenceCategory android:title="@string/preferencias" >
<CheckBoxPreference
android:key="modo_viagem"
android:summary="@string/modo_viagem_sumario"
123

## Página 126

3.10. Preferências CasadoCódigo
android:title="@string/modo_viagem" />
<EditTextPreference
android:dialogTitle="@string/informe_valor_limite"
android:key="valor_limite"
android:defaultValue="80"
android:summary="@string/valor_limite_sumario"
android:title="@string/valor_limite"/>
</PreferenceCategory>
</PreferenceScreen>
Reparequenãohánenhumlayoutdeclaradooualgum widget,sendooelemento
raizo <PreferenceScreen>. Oselementosquecompõemateladepreferên-
ciassãoespecíficos.Aspreferênciaspodemseragrupadasemcategorias,atravésdo
elemento <PreferenceCategory>paraquesejamapresentadasvisualmenteno
mesmogrupo. Emseguida,definimosumapreferênciaquefazusodeum check-
box,atravésdo CheckBoxPreference,paraconfiguraroaplicativoem“Modo
Viagem”. Jáparaadefiniçãodovalorlimitedegastosutilizamosumapreferência
associadaaum EditText,cujovalorpadrãoé80.
Ovalorinformadonoatributo keyseráoidentificadordachaveondeseráar-
mazenadaapreferênciaequeseráutilizadaposteriormenteparaarecuperaç ãodo
valorgravado. Paraosatributos title, summarye dialogTitledefinimos
mensagensqueserãoapresentadasparaousuáriocomadescriç ãodapreferência
queestásendoconfigurada.Agoraprecisamoscriaruma activityqueestendeaclasse
PreferenceActivity,ecarregaroXMLquedefineasop ções. Crieumaclasse
chamada ConfiguracoesActivitycomoseguintecódigo:
1 public class ConfiguracoesActivity extends PreferenceActivity {
2 @Override
3 protected void onCreate(Bundle savedInstanceState) {
4 super.onCreate(savedInstanceState);
5 addPreferencesFromResource(R.xml.preferencias);
6 }
7 }
Nométodo onCreate,invocamoso addPreferencesFromResourcedis-
ponívelna PreferenceActivityparacarregaroarquivoXMLdepreferências
econstruiratela.Quandoaop ção“Configurações”daDashboardActivityfor
escolhida,ateladepreferênciascriadadeveráserexibida.
124

## Página 127

CasadoCódigo Capítulo3. DomineosprincipaiselementosdeInterfaceGráfica
Façaasalteraçõesnecessáriasnométodo selecionarOpcaoparaabriratela
depreferências( ConfiguracoesActivity)econfiracomoficouateladeprefe-
rências:
public void selecionarOpcao(View view) {
switch (view.getId()) {
//códigos existentes
case R.id.configuracoes:
startActivity(new Intent(this, ConfiguracoesActivity.class));
break;
}
}
Figura3.21:Telasdepreferênciasdoaplicativo
Nestemomentonãoimplementaremosasfuncionalidadesqueirãoutilizarestas
preferênciasqueacabamosdearmazenarpoisdependemosdeitensqueaindanão
estãoprontos.Noentanto,paraexercitarousodepreferências,vamosimplementar
outrafuncionalidade,queéincluirnanossaaplicaç ãoumaop çãoparaousuário
125

## Página 128

3.10. Preferências CasadoCódigo
manter-selogadonoaplicativo.Issoutilizaráaclasse SharedPreferencespara
acessaregravardadosemumarquivodepreferênciadeuma Activity.
Nateladelogin,incluiremosum checkboxparaindicaraop çãodousuárioe
gravaremosessainformaçãonoarquivodepreferênciasdaatividade.
<CheckBox
android:id="@+id/manterConectado"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:text="@string/manter_conectado" />
Quandooaplicativoforiniciado,apreferênciaseráconsultadaparadeterminar
seateladelogindeveserapresentadaouse dashboarddeveserexibida. Altereo
login.xmlparaincluiruma checkboxdaseguinteformaeverifiquecomoficouo
códigoda BoaViagemActivity:
Precisamos obter uma instância deSharedPreferences no modo pri-
vado, oquepermitealteraçõesnoarquivodepreferênciaapenaspelaaplicaç ão
que a criou, e em seguida tentar recuperar algum valor gravado para a chave
manter_conectado. Casonenhumvalorsejaencontrado,ovalor falsedeve
serretornado. Casoovalorrecuperadoseja true,emvezdeapresentaratelade
login,a DashboardActivityéiniciada.
public class BoaViagemActivity extends Activity {
private static final String MANTER_CONECTADO = "manter_conectado";
private EditText usuario;
private EditText senha;
private CheckBox manterConectado;
@Override
public void onCreate(Bundle savedInstanceState ) {
super.onCreate(savedInstanceState);
setContentView(R.layout.login);
usuario = (EditText) findViewById(R.id.usuario);
senha = (EditText) findViewById(R.id.senha);
manterConectado = (CheckBox) findViewById(R.id.manterConectado);
SharedPreferences preferencias = getPreferences(MODE_PRIVATE);
boolean conectado =
preferencias.getBoolean(MANTER_CONECTADO, false);
126

## Página 129

CasadoCódigo Capítulo3. DomineosprincipaiselementosdeInterfaceGráfica
if(conectado){
startActivity(new Intent(this, DashboardActivity.class));
}
}
}
Nométodo entrarOnClicktratamosdaescolhadousuárioemsemanterou
nãoconectado.
Apósaautenticaçãobemsucedida,podemosrecuperarum Editorparafazeras
alteraçõesdesejadasnoarquivodepreferênciaseoutilizamosparaincluirnachave
manter_conectadoovalorbooleanoobtidoda checkbox.Paraefetivarasaltera-
çõesénecessárioinvocarométodo editor.commit().Emseguida,iniciamosa
dashboard.Executeaaplicaç ãoeexperimenteestanovafuncionalidade!
public void entrarOnClick(View v) {
String usuarioInformado = usuario.getText().toString();
String senhaInformada = senha.getText().toString();
if("leitor".equals(usuarioInformado) &&
"123".equals(senhaInformada)) {
SharedPreferences preferencias =
getPreferences(MODE_PRIVATE);
Editor editor = preferencias.edit();
editor.putBoolean(MANTER_CONECTADO,
manterConectado.isChecked());
editor.commit();
startActivity(new Intent(this,DashboardActivity.class));
}
else{
String mensagemErro = getString(R.string.erro_autenticacao);
Toast toast = Toast.makeText(this, mensagemErro,
Toast.LENGTH_SHORT);
toast.show();
}
}
}
127

## Página 130

3.11. Conclusão CasadoCódigo
Paradefiniroutrosarquivosdepreferênciasouterumarquivodepreferênciaque
seráacessadopormaisatividadesapartirdeumdeterminadonome,bastarecuperar
uma SharedPreferencesdestaforma:
String NOME_PREFERENCIAS = "PREFERENCIAS_BOAVIAGEM";
SharedPreferences preferencias =
getSharedPreferences(NOME_PREFERENCIAS, 0);
Quandoutilizamosasfacilidadesda PreferenceActivity,oarquivodepre-
ferênciascriadoporeladeveseracessadoatravésdo PreferenceManager,infor-
mandoocontexto(aatividadequeiráutilizaroarquivo)daseguinteforma:
SharedPreferences preferencias = PreferenceManager
.getDefaultSharedPreferences(contexto);
3.11 Conclusão
Chegamosaofinaldemaisumcapítulo!Aquiaprendemosnapráticacomoutilizar
osprincipaislayoutsdisponíveisnaplataformaAndroid,bemcomofazerusodos
widgetsfundamentaisparaaentradadedados.Tambémcriamos ListViewsper-
sonalizadasparaexibirlistagenseacrescentamosfuncionalidadescomomenusde
opçãoedecontexto.Empregamos AlertDialogsparaaaplicaç ãosecomunicar
comousuário,alémdesalvarassuaspreferências.Aprimeiraversãodanossaapli-
caçãoBoaViagemestáquasepronta! Vamosprosseguirparaocapítuloseguintee
descobrircomopersistirerecuperarosdadosutilizandooSQLite.
128

## Página 131

Capítulo4
PersistênciadedadosnoAndroid
comSQLite
ParaonossoaplicativoBoaViagemasinteraçõescomousuáriojáestãopraticamente
prontas,noentanto,aindanãoestamospersistindoosdadosdasviagensedosgastos
realizados.Oobjetivodestecapítuloéarmazenarerecuperardadosdanossaapli-
caçãoutilizandooSQLite,disponívelnaplataformaAndroid,que,aocontrárioda
maioriadosbancosdedadosSQL,nãonecessitadeumprocessoservidor.
OSQLitearmazenaastabelas, views,índicese triggersemapenasumarquivoem
disco,noqualsãorealizadasasoperaçõesdeleituraeescrita.NoAndroid,obanco
dedadoséacessívelporqualquerclassedaaplicaç ãoqueocriou,masnãopodeser
acessadoporoutra.
Quandoaaplicaç ãoquecontémobancodedadosédesinstalada,osdadosar-
mazenadostambémsãoremovidos.

## Página 132

4.1. Oprocessodecriaçãodobancodedados CasadoCódigo
4.1 O processo de criação do banco de dados
ParautilizaroSQLiteemnossaaplicaç ão,precisamosusarumaAPIquejápossua
todootrabalhodesecomunicarcomobancodedadosencapsuladodentrodela.É
justamenteesseopapeldaclasse SQLiteOpenHelper,quedevemosherdar.
Estaclassefacilitaacriaç ão,versionamentoeacessoaobancodedados.Então
vamoscome çar!Crieumanovaclassecomonomede DatabaseHelperherdando
de SQLiteOpenHelper.
public class DatabaseHelper extends SQLiteOpenHelper{
...
}
Ao herdar desta classe, devemos implementar os métodosonCreate e
onUpgradeparacriarastabelaseincluirosdadosiniciais,casonecessário.Além
disso,éprecisotratardasregrasdeatualizaç ãodedadosedeestruturadobanco
quandonecessário.
Também precisaremos chamar o construtor doSQLiteOpenHelper in-
formando o contexto, o nome do banco de dados e sua versão atual e um
CursorFactorysenecessário:
public class DatabaseHelper extends SQLiteOpenHelper{
private static final String BANCO_DADOS = "BoaViagem";
private static int VERSAO = 1;
public DatabaseHelper(Context context) {
super(context, BANCO_DADOS, null, VERSAO);
}
@Override
public void onCreate(SQLiteDatabase db) {}
@Override
public void onUpgrade(SQLiteDatabase db, int oldVersion,
int newVersion) {}
}
Teremosduastabelasnobancodedados,umaparaarmazenarosdadosdasvia-
genseoutraparaosgastosrealizados.Acriaç ãodastabelasdeveserfeitanométodo
130

## Página 133

CasadoCódigo Capítulo4. PersistênciadedadosnoAndroidcomSQLite
onCreate,queéinvocadoquandotentamosacessarobancodedadospelaprimeira
vezeomesmoaindanãoestácriado.
Para criar as tabelas, executamos uma instrução SQL usando o método
execSQL,daclasse SQLiteDatabase,quenãopossuiretorno.Dessaforma,po-
demosutilizá-losomenteparainstruçõescujoresultadonãoprecisaseravaliado.Já
ométodo onUpgrade,deveimplementarasregrasparaatualizaç ãodaestruturado
bancoetambémdosdadosquandoumanovaversãofordisponibilizada.
@Override
public void onCreate(SQLiteDatabase db) {
db.execSQL("CREATE TABLE viagem (_id INTEGER PRIMARY KEY," +
" destino TEXT, tipo_viagem INTEGER, data_chegada DATE," +
" data_saida DATE, orcamento DOUBLE," +
" quantidade_pessoas INTEGER);");
db.execSQL("CREATE TABLE gasto (_id INTEGER PRIMARY KEY," +
" categoria TEXT, data DATE, valor DOUBLE," +
" descricao TEXT, local TEXT, viagem_id INTEGER," +
" FOREIGN KEY(viagem_id) REFERENCES viagem(_id));");
}
Quandoumanovaversãodoaplicativoedobancodedadosforlan çada,oAn-
droidverificaráqualversãodobancodedadosousuáriopossui,eseestaforme-
nordoqueaatual,entãoométodo onUpgradeseráinvocado. Comoporen-
quantoaindaestamosnaprimeiraversão,nãoimplementaremosnadanométodo
onUpgrade.
Casosejanecessário,porexemplo,emumanovaversãodoaplicativo,acres-
centarumanovacolunanatabela gastoparaarmazenaronomedapessoaqueo
realizou,poderíamosimplementarométodo onUpgradedessaforma:
@Override
public void onUpgrade(SQLiteDatabase db,
int oldVersion, int newVersion) {
db.execSQL("ALTER TABLE gasto ADD COLUMN pessoa TEXT");
}
Tanto a criação do banco quanto a sua atualização só acontecem de fato
quandoobtemosumainstânciade SQLiteDatabaseenãoquandoinstanciamos
o DatabaseHelper.Veremosessesdetalhesmaisadiante.
131

## Página 134

4.2. Gravaçãodasviagensnobancodedados CasadoCódigo
Convenção para a coluna id
Umdetalheimportanteéqueascolunasquesãochavesprimárias
possuemonomede _id.Estaéumaconven çãoutilizadanoAndroid
paraqueosresultadosdeconsultasrealizadasnessastabelaspossamser
utilizadasem CursorAdapters,quedependemdeumacolunacom
estenome.
4.2 Grav ação das viagens no banco de dados
Comobancodedadosjápreparado,vamoscome çaraarmazenarosdadosdas
viagens. Nestemomento,iremosfocaremcomorealizarasoperaçõesnobanco
de dados. No métodoonCreate, da ViagemActivity, instanciaremos o
DatabaseHelperetambémcriaremosreferênciasparatodasas viewsquecon-
témosdadosinformadospelousuário,poisteremosqueosgravar.Ocódigoficará
assim:
// novos atributos
private DatabaseHelper helper;
private EditText destino, quantidadePessoas, orcamento;
private RadioGroup radioGroup;
@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.viagem);
Calendar calendar = Calendar.getInstance();
ano = calendar.get(Calendar.YEAR);
mes = calendar.get(Calendar.MONTH);
dia = calendar.get(Calendar.DAY_OF_MONTH);
dataChegadaButton = (Button) findViewById(R.id.dataChegada);
dataSaidaButton = (Button) findViewById(R.id.dataSaida);
// recuperando novas views
destino = ( EditText) findViewById(R.id.destino);
quantidadePessoas = (EditText) findViewById(R.id.quantidadePessoas);
132

## Página 135

CasadoCódigo Capítulo4. PersistênciadedadosnoAndroidcomSQLite
orcamento = (EditText) findViewById(R.id.orcamento);
radioGroup = (RadioGroup) findViewById(R.id.tipoViagem);
// prepara acesso ao banco de dados
helper = new DatabaseHelper(this);
}
Agora precisaremos implementar de fato a inserção dos dados informados
pelo usuário. Isto será feito no métodosalvarViagem, que é disparado
quandoousuáriopressionaobotão“Salvar”. Pararealizaroperaçõesdeescrita
nobancodedados, devemosrecuperarum SQLiteDatabaseatravésmétodo
getWritableDatabase(),definidonaclasse SQLiteOpenHelperedisponível
pormeiodeheran çananossaclasse DatabaseHelper.
1 public void salvarViagem(View view){
2 SQLiteDatabase db = helper.getWritableDatabase();
3 }
Parainserirosdados,podemosmontarmanualmenteumainstruç ãoSQLde
insertouutilizaro ContentValuesinformandoumconjuntodedadosnofor-
matochave-valor,noqualachaveéacolunadobancodedadoseovaloréodadoa
serarmazenado.
Porsimplificação, nãorealizaremosnenhumavalidaç ãodosdados, simples-
menterecuperaremososdadosinformadospelousuárioatravésdas viewseco-
locaremosemum ContentValues:
public void salvarViagem(View view) {
SQLiteDatabase db = helper.getWritableDatabase();
ContentValues values = new ContentValues();
values.put("destino", destino.getText().toString());
values.put("data_chegada", dataChegada.getTime());
values.put("data_saida", dataSaida.getTime());
values.put("orcamento", orcamento.getText().toString());
values.put("quantidade_pessoas",
quantidadePessoas.getText().toString());
int tipo = radioGroup.getCheckedRadioButtonId();
if(tipo == R.id.lazer) {
133

## Página 136

4.2. Gravaçãodasviagensnobancodedados CasadoCódigo
values.put("tipo_viagem", Constantes.VIAGEM_LAZER);
} else {
values.put("tipo_viagem", Constantes.VIAGEM_NEGOCIOS);
}
}
Agoraquetemoso ContentValuespreparado,podemosinvocarométodo
insertdo SQLiteDatabase,quereceberá3parâmetros.Oprimeiroinformando
atabela,eoterceiroreceberáo ContentValues.Osegundoparâmetro,emque
informaremos null,representaonomedaschavesdo ContentValuesquedevem
terseuvalorinseridocomo null. Nonossocaso,nãodesejamosquenenhuma
colunatenhaseuvaloranulado,porissonãopassamosnada.
Porfim,casooregistrosejainseridocomsucesso,ométodo insertretorna
oidentificadordonovoregistroeemcasodefalharetorna -1emostramosuma
mensagemnateladeacordocomesseresultado.
public void salvarViagem(View view) {
// prepara o ContentValues
long resultado = db.insert("viagem", null, values);
if(resultado != -1 ){
Toast.makeText(this, getString(R.string.registro_salvo),
Toast.LENGTH_SHORT).show();
}else{
Toast.makeText(this, getString(R.string.erro_salvar),
Toast.LENGTH_SHORT).show();
}
}
Acoluna tipo_viagemédotipo INTEGEReparaevitarousodiretodenúme-
rosnocódigo,podemoscriarconstantespararepresentarosseuspossíveisvalores.
Comoistoérecorrente,criamosumaclassechamada Constantesquevaicentra-
lizartodasasconstantesutilizadasnaaplicaç ão.
Inicialmenteestaclasseteráapenasostiposdeviagem,masnofuturoadiciona-
remosnovasinformações.Ocódigodelaéoseguinte
public class Constantes {
public static final int VIAGEM_LAZER = 1;
public static final int VIAGEM_NEGOCIOS = 2;
}
134

## Página 137

CasadoCódigo Capítulo4. PersistênciadedadosnoAndroidcomSQLite
O leitor mais atento deve ter percebido que, ao incluir os valores no
ContentValuesparasereminseridosnobancodedados,otipododadonãoé
omesmodaqueledeterminadonacriaç ãodatabelacorrespondente.Porexemplo,
acoluna data_chegadaédotipo%DATE%,porématribuímosaelaumvalordo
tipo long.
Nãoháproblema!OSQLitetrabalhacomtiposdinâmicosesabeconverterosda-
dosadequadamenteparaoformatodesejado.Valeressaltarqueparaostipos DATE
éinteressantearmazená-losinformandooseuvalorcomo longparaquepossamos
posteriormenteconstruirmaisfacilmenteumobjetodotipo java.util.Date.
Umdetalheimportanteéanecessidadedefecharobancodedadosquando
seu uso não for mais necessário. Podemos fazer isso chamando o método
helper.close().Nemsempreéfácildeterminaromelhormomentoparafechar
obancodedados,porissoécomumofazerquandoa activityforfinalizadaedes-
truída,sobrescrevendoométodo onDestroy.Lembre-sedefazerissosempreque
utilizarumbancodedados.
@Override
protected void onDestroy() {
helper.close();
super.onDestroy();
}
Comessasalterações,finalizamosainser çãodasinformaçõesdeviagens! Os
dadosdaviagemagorajásãoarmazenadosnobancodedados.Fácilnãoémesmo?
Agoraprecisamossaberquaisdadostemosgravados.
4.3 Listando as viagens direto do SQLite
Umavezqueasinformaçõesdasviagensjáestãoarmazenadosnobancodeda-
dos,precisaremosrecuperá-lasparaaexibiç ãonalistadeviagens,quenomomento
contaapenascomumaimplementaç ãotemporáriaedadosestáticos. Naclasse
ViagemListActivityvamosreaproveitaroscódigosquetratamda ListView
ealteraraimplementaç ãodométodo listarViagens()parabuscarasinforma-
çõesdasviagensnobancodedados.
Parainiciarestaimplementaç ão,devemosinstanciarum DatabaseHelpere
tambémrecuperarovalorlimitedegastosdaspreferênciasdousuário. Podemos
aproveitarecriarum SimpleDateFormatparaformatarasdatasrecuperadasdo
bancodedados,tudoissonométodo onCreate:
135

## Página 138

4.3. ListandoasviagensdiretodoSQLite CasadoCódigo
private DatabaseHelper helper;
private SimpleDateFormat dateFormat;
private Double valorLimite;
@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
helper = new DatabaseHelper(this);
dateFormat = new SimpleDateFormat("dd/MM/yyyy");
SharedPreferences preferencias =
PreferenceManager.getDefaultSharedPreferences(this);
String valor = preferencias.getString("valor_limite", "-1");
valorLimite = Double.valueOf(valor);
//códigos existentes
}
Nométodo listarViagens()faremosumaconsultanobancodedadospara
obtertodasasviagenscadastradas. Aocontráriodoquefoifeitoparasalvarum
registro,queéumaoperaç ãodeescrita,agorautilizaremosumainstânciadeleitura
do SQLiteDatabase,atravésdométodo getReadableDatabase.Apartirdela,
faremosumaconsultaeobteremosum Cursorparanavegarpelosresultados:
1 private List<Map<String, Object>> listarViagens() {
2
3 SQLiteDatabase db = helper.getReadableDatabase();
4 Cursor cursor =
5 db.rawQuery("SELECT _id, tipo_viagem, destino, " +
6 "data_chegada, data_saida, orcamento FROM viagem",
7 null);
8 //códigos existentes
9 }
Nestaimplementação,utilizamosométodo rawQueryqueexecutaumSQL
diretamente.O Cursorretornadoestásempreposicionadoantesdoprimeirore-
sultado.Parainiciarmosaiteraç ãosobreosdados,precisamosapontá-loparaopri-
meiroregistroetambémsaberaquantidadedelinhasretornadas.Alémdisso,tam-
bémutilizaremosummétodoparaavan çarparaopróximoregistroeparafecharo
136

## Página 139

CasadoCódigo Capítulo4. PersistênciadedadosnoAndroidcomSQLite
cursorquandofinalizarmosaiteraç ão. Osmétodosdisponíveisparaissosãoos
seguintes:
// move o cursor para o primeiro registro
cursor.moveToFirst();
// retorna a quantidade de linhas
cursor.getCount();
// avança para o próximo registro
cursor.moveToNext();
// fecha o cursor
cursor.close();
Paraobterosdadosdo Cursor,devemosinvocarum gettercomotipododado,
informandooíndicedacolunadesejada. Porexemplo,pararecuperarovalorda
coluna“_id”,queédotipoINTEGER,chamamosométodo cursor.getInt(0),
onde 0éoíndicedacoluna.Osoutros gettersdisponíveissão:
cursor.getInt(columnIndex);
cursor.getFloat(columnIndex);
cursor.getLong(columnIndex);
cursor.getShort(columnIndex);
cursor.getString(columnIndex);
cursor.getBlob(columnIndex);
Quandonãosabemosaocertooíndicedacoluna,massabemososeunome,
podemosutilizarométodo getColumnIndex(columnName)pararecuperarsua
posição.
Agora que realizamos a consulta e recuperamos oCursor, precisamos
posicioná-lonoprimeiroregistro,atravésdométodo moveToFirst:
SQLiteDatabase db = helper.getReadableDatabase();
Cursor cursor =
db.rawQuery("SELECT _id, tipo_viagem, destino, " +
"data_chegada, data_saida, orcamento FROM viagem",
null);
cursor.moveToFirst();
Opróximopassoéguardaremummapaosdadosdecadaregistro.Nessemapa,
achaveconteráonomedainformaç ãoeovalorseráainformaç ãoquefoirecupe-
radadobancodedados. Teremosquefazerissoparao id, tipo de viagem,
137

## Página 140

4.3. ListandoasviagensdiretodoSQLite CasadoCódigo
destino, data de chegada, data de saída e orcamento,fazendoconver-
sõesondenecessário,comoporexemplo,de longpara Date.Todososregistros
serãoguardadosemum ArrayList,contendoasviagens:
private List<Map<String, Object>> listarViagens() {
SQLiteDatabase db = helper.getReadableDatabase();
Cursor cursor =
db.rawQuery("SELECT _id, tipo_viagem, destino, " +
"data_chegada, data_saida, orcamento FROM viagem",
null);
cursor.moveToFirst();
viagens = new ArrayList<Map<String, Object>>();
for (int i = 0; i < cursor.getCount(); i++) {
Map<String, Object> item = new HashMap<String, Object>();
String id = cursor.getString(0);
int tipoViagem = cursor.getInt(1);
String destino = cursor.getString(2);
long dataChegada = cursor.getLong(3);
long dataSaida = cursor.getLong(4);
double orcamento = cursor.getDouble(5);
item.put("id", id);
if (tipoViagem == Constantes.VIAGEM_LAZER) {
item.put("imagem", R.drawable.lazer);
} else {
item.put("imagem", R.drawable.negocios);
}
item.put("destino", destino);
Date dataChegadaDate = new Date(dataChegada);
Date dataSaidaDate = new Date(dataSaida);
String periodo = dateFormat.format(dataChegadaDate) + " a "
138

## Página 141

CasadoCódigo Capítulo4. PersistênciadedadosnoAndroidcomSQLite
+ dateFormat.format(dataSaidaDate);
item.put("data", periodo);
double totalGasto = calcularTotalGasto(db, id);
item.put("total", "Gasto total R$ " + totalGasto);
double alerta = orcamento * valorLimite / 100;
Double [] valores =
new Double[] { orcamento, alerta, totalGasto };
item.put("barraProgresso", valores);
viagens.add(item);
cursor.moveToNext();
}
cursor.close();
return viagens;
}
Paracadaviagemdalista,tambémdeveserapresentadoovalortotalgastona-
quelaviagem. Faremosestaimplementaçãonométodo calcularTotalGasto,
querealizaráumaconsultaquesomaovalordosgastosrealizadoscomo idinfor-
madocomoparâmetro.Ocódigodessemétodoficarádaseguintemaneira:
private double calcularTotalGasto(SQLiteDatabase db, String id) {
Cursor cursor = db.rawQuery(
"SELECT SUM(valor) FROM gasto WHERE viagem_id = ?",
new String[]{ id });
cursor.moveToFirst();
double total = cursor.getDouble(0);
cursor.close();
return total;
}
Osegundoparâmetrodométodo rawQueryesperaum Arrayde String,e
serveparainformarosvaloresqueserãoutilizadosnacláusula WHEREdaconsulta.
Nestecaso,queremosrestringirasomadosvaloresgastosapenasparaaviagemcujo
idforigualaoinformado.
139

## Página 142

4.4. AtualizaçãodeviagenseoupdatenoSQLite CasadoCódigo
Pronto! Agoratemosnossalistadeviagenstotalmentedinâmica,obtendoas
informaçõesdiretamentedobancodedados.
Existem ainda duas outras formas de realizar consultas em um banco SQ-
LitenoAndroid. Umadelaséatravésdosmétodos querydisponíveisnaclasse
SQLDatabase.Comela,devemosinformarcadatrechodanossaconsultaatravés
deumparâmetro,ouseja,precisa-seinformaroscamposdevolvidosno select,
o groupBy,o havingeassimpordiante.Vejaanossaprimeiraconsultareescrita
utilizandoessaforma:
String tabela = "viagem";
String[] colunas = new String[]{"_id", "tipo_viagem", "destino",
"data_chegada","data_saida",
"orcamento"};
String selecao = null;
String[] selecaoArgs = null;
String groupBy = null;
String having = null;
String orderBy = null;
Cursor cursor = db.query(tabela, colunas, selecao, selecaoArgs,
groupBy, having, orderBy);
Aoutramaneiraderealizarconsultaséutilizandoum SQLiteQueryBuilder.
Atravésdessaclasseépossívelconstruirprogramaticamenteconsultascomplexas,
incluindováriastabelas. Aseguirvejaanossaconsultaconstruídautilizandoesta
abordagem:
SQLiteQueryBuilder builder = new SQLiteQueryBuilder();
builder.setTables("viagem");
Cursor cursor = builder.query(db, colunas, selecao,
selecaoArgs, groupBy,
having, orderBy);
4.4 Atualização de viagens e o update no SQLite
Apróximaimplementaç ãoquefaremosemnossoaplicativoéaatualizaç ãodasin-
formaçõesdeumadeterminadaviagem.Quandoalistadeviagenséapresentadae
ousuárioselecionaalgumadelas,um AlertDialogcomop çõeséexibido,sendo
140

## Página 143

CasadoCódigo Capítulo4. PersistênciadedadosnoAndroidcomSQLite
queumadelasdizrespeitoàediç ãodaviagemselecionada.Implementaremosesta
funcionalidadeagora.
Aideiaéquequandoousuárioselecionaraop ção“editar”,oiddaviagemse-
lecionadasejarecuperadodomapaecolocadocomoum extrana intentqueirá
abrira ViagemActivity.Depois,no onCreateda ViagemActivityrecupe-
raremosessevalorparasaberseestamoscriandoumanovaviagemoueditandouma
existente.
Nométodo salvarViagem,verificaremoseste idparaexecutarumaope-
raçãode insertoude update. Vejaocódigodométodo onClickdaclasse
ViagemListActivityparatrataraediç ão:
@Override
public void onClick(DialogInterface dialog, int item) {
Intent intent;
String id = (String) viagens.get(viagemSelecionada).get("id");
switch (item) {
case 0: // editar viagem
intent = new Intent(this, ViagemActivity.class);
intent.putExtra(Constantes.VIAGEM_ID, id);
startActivity(intent);
break;
// códigos existentes
...
}
}
Primeirorecuperamoso iddaviagemqueousuáriodesejaeditareocolocamos
comoinformaçãoextrana intentqueabriráa ViagemActivity. Agorano
método onCreateda ViagemActivity,obtemosestevalore,casosejaválido,
carregaremosasinformaçõesdaviagemcomo idinformadoapartirdobancode
dadosparaexibiraousuário.Asalteraçõesdecódigosãoasseguintes:
// demais atributos
private String id;
@Override
protected void onCreate(Bundle savedInstanceState) {
//códigos existentes
141

## Página 144

4.4. AtualizaçãodeviagenseoupdatenoSQLite CasadoCódigo
...
id = getIntent().getStringExtra(Constantes.VIAGEM_ID);
if(id != null){
prepararEdicao();
}
}
Nométodo prepararEdicaobuscaremosaviagemcomo idinformadoe
atribuiremososvaloresobtidosaos widgetsdatela.
private void prepararEdicao() {
SQLiteDatabase db = helper.getReadableDatabase();
Cursor cursor =
db.rawQuery("SELECT tipo_viagem, destino, data_chegada, " +
"data_saida, quantidade_pessoas, orcamento " +
"FROM viagem WHERE _id = ?", new String[]{ id });
cursor.moveToFirst();
SimpleDateFormat dateFormat = new SimpleDateFormat("dd/MM/yyyy");
if(cursor.getInt(0) == Constantes.VIAGEM_LAZER){
radioGroup.check(R.id.lazer);
} else {
radioGroup.check(R.id.negocios);
}
destino.setText(cursor.getString(1));
dataChegada = new Date(cursor.getLong(2));
dataSaida = new Date(cursor.getLong(3));
dataChegadaButton.setText(dateFormat.format(dataChegada));
dataSaidaButton.setText(dateFormat.format(dataSaida));
quantidadePessoas.setText(cursor.getString(4));
orcamento.setText(cursor.getString(5));
cursor.close();
}
Oúltimopassoéalterarométodo salvarViagemparadecidirsevamosreali-
zarumaoperaç ãode insertoude updatecombasenoatributo idrecuperado
142

## Página 145

CasadoCódigo Capítulo4. PersistênciadedadosnoAndroidcomSQLite
da intent.Seo idforiguala null,entãonadafoiinformadona intentetrata-
sedeumnovoregistrodeviagem.Casocontrário,utilizaremosométodo update
quemtemumaassinaturasimilaràdométodo insert,recebendodoisparâmetros
amaisparaindicaroscritériosderestriç ão. Informaremosnestesparâmetrosque
aatualizaçãodeveserrealizadaparaoregistrocom _idigualaoinformado. As
alteraçõesnocódigodo salvarViagemficarãoassim:
public void salvarViagem(View view) {
// códigos existentes
...
if(id == null){
resultado = db.insert("viagem", null, values);
} else {
resultado = db.update("viagem", values, "_id = ?",
new String[]{ id });
}
...
// códigos existentes
Aoperaçãode updateretornaaquantidadederegistrosafetadospelocomando
epodemosutilizarestainformaç ãoparasaberseaatualizaç ãodeucerto. Eéisso,
maisumafuncionalidadepronta! Jápodemostestaraatualizaç ãodeumaviagem
existente.Agorasónosrestapoderexcluirasinformaçõesquenãoqueremosmais.
4.5 Como apagar uma viagem com o SQLite e oAn-
droid
Oqueprecisamosagoraéimplementaraexclusãodeumaviagemedeseusrespec-
tivosgastosquandoaop ção“Remover”forescolhidanaViagemListActivity
etambémapartirdamesmaop çãoexistentenomenuda ViagemActivity.As-
simcomonasoperaçõesde inserte update,paraaexclusãoderegistrotemoso
método deletedisponívelno SQLiteDatabase.
No onClickda ViagemListActivityiremosincluirachamadaparaum
métodoqueexecutaráaexclusãodosregistros.Ométododeexclusãosópoderáser
chamadoseousuárioconfirmaraoperaç ão.Vamosalterarocódigoparaquechame
ométodoadequado:
143

## Página 146

4.6. DicaseboaspráticasaotrabalharcombancodedadosnoAndroid CasadoCódigo
@Override
public void onClick(DialogInterface dialog, int item) {
// códigos existentes
...
switch (item) {
...
case DialogInterface.BUTTON_POSITIVE: // exclusão
viagens.remove(viagemSelecionada);
removerViagem(id);
getListView().invalidateViews();
break;
...
}
O iddaviagemaserexcluídaserápassadacomoparâmetroparaométodo
removerViagem,noqualprimeiramenteexcluímostodososgastosassociadose
depoisremovemosaviagempropriamentedita.
1 private void removerViagem(String id) {
2 SQLiteDatabase db = helper.getWritableDatabase();
3 String where [] = new String[]{ id };
4 db.delete("gasto", "viagem_id = ?", where);
5 db.delete("viagem", "_id = ?", where);
6 }
Pronto,agorajáconseguimosrealizarasprincipaisoperaçõesdebancodedados
comoSQLiteeoAndroid!
4.6 D icas e boas práticas ao trabalhar com banco
de dados noAndroid
Parasermaisdidáticoetambémfocarnasoperaçõescomobancodedados,não
tivemosnenhumapreocupaç ãoemescreverumcódigobomefácildemanter.No
entanto,umavezquejáaprendemosautilizaroSQLiteecompreendercomoele
funcionachegouomomentodeaprimorarocódigodanossaaplicaç ão.
Basicamenteexistemtrêsproblemasnoscódigosqueescrevemos. Oprimeiro
deleséquenãoestamosutilizandonenhumaclassepararepresentarodomínioda
nossaaplicação. Poderíamoscriarasclasses Viageme Gastopararepresentar
essesobjetos,obtendoassimumcódigomaisorganizadoedefácilmanipulaç ão,
semcontaréclarocomosdemaisbenefíciosdo designorientadoaobjetos.
144

## Página 147

CasadoCódigo Capítulo4. PersistênciadedadosnoAndroidcomSQLite
Como parte do processo de refatoraç ão, podemos criar es-
tas duas novas classes, Viagem, em um novo pacote chamado
br.com.casadocodigo.boaviagem.domain:
public class Viagem {
private Long id;
private String destino;
private Integer tipoViagem;
private Date dataChegada;
private Date dataSaida;
private Double orcamento;
private Integer quantidadePessoas;
public Viagem(){}
public Viagem(Long id, String destino, Integer tipoViagem,
Date dataChegada, Date dataSaida, Double orcamento,
Integer quantidadePessoas) {
this.id = id;
this.destino = destino;
this.tipoViagem = tipoViagem;
this.dataChegada = dataChegada;
this.dataSaida = dataSaida;
this.orcamento = orcamento;
this.quantidadePessoas = quantidadePessoas;
}
// getters e setters
}
Etambémaclasse Gasto:
public class Gasto {
private Long id;
private Date data;
private String categoria;
private String descricao;
private Double valor;
private String local;
private Integer viagemId;
145

## Página 148

4.6. DicaseboaspráticasaotrabalharcombancodedadosnoAndroid CasadoCódigo
public Gasto(){}
public Gasto(Long id, Date data, String categoria, String descricao,
Double valor, String local, Integer viagemId) {
this.id = id;
this.data = data;
this.categoria = categoria;
this.descricao = descricao;
this.valor = valor;
this.local = local;
this.viagemId = viagemId;
}
//getters e setters
}
Outroproblemaéqueestamosdiretamentemanipulandodiversas String,que
representamastabelasesuasrespectivascolunas.Sealgumadelasmudar,teremos
quevarrerocódigoealterarcadaocorrênciadessa String.
Alémdisso,oscódigosquesereferemaoacessoaosdadosestãomisturadoscom
códigosda Activityquedeveriamessencialmentetratarapenasdainteraç ãocom
ousuário.Novamente,qualqueralteraçãonaestruturadobancodedadosinfluenci-
ariatodoorestantedocódigodaaplicaç ão.Precisamossepararasresponsabilidades.
Resolveremosessesproblemasutilizandoumobjetodeacessoadados,o DAO-
Data Access Object,queéumpadrãoparaimplementaraseparaç ãodalógicadene-
góciodasregrasdeacessoabancodedados.Podemoscriaraclasse BoaViagemDAO
nopacote br.com.casadocodigo.boaviagem.daoqueinicialmenteteráose-
guintecódigo:
public class BoaViagemDAO {
private DatabaseHelper helper;
private SQLiteDatabase db;
public BoaViagemDAO(Context context){
helper = new DatabaseHelper(context);
}
private SQLiteDatabase getDb() {
if (db == null) {
146

## Página 149

CasadoCódigo Capítulo4. PersistênciadedadosnoAndroidcomSQLite
db = helper.getWritableDatabase();
}
return db;
}
public void close(){
helper.close();
}
}
OBoaViagemDAOdefineumconstrutorquerecebeocontextodaaplicaç ãoe
instanciaum DatabaseHelper.Tambémdefinimosummétodoqueretornauma
instânciade SQLiteDatabase,criando-asenecessário.Utilizaremossempreeste
métodoparaobterumainstânciade SQLiteDatabasee,apartirdela,executaras
operaçõescomobancodedados.
Vocêpodeestarseperguntandoporquefizemosissoemvezdeinicializar
logoavariável dbnoconstrutor. OmotivoéqueoAndroidexecutaasope-
rações de criação e atualização do banco apenas quando solicitamos uma ins-
tânciade SQLiteDatabase,atravésdosmétodos getWritableDatabaseou
getReadableDatabase.
Comoessasoperaçõespodemserdemoradas,recomenda-senãoinvocaresses
métodosemconstrutoresemétodosdeinicializaç ão,comono onCreatedeuma
Activity. Portanto,devemospostergarainvocaç ãodessesmétodosatéquere-
almentesejanecessárioexecutarumaoperaç ãocomobancodedados. Nonosso
DAO,tambémdisponibilizamosométodo closequeinvocaométododemesmo
nomedo DatabaseHelperparafecharobancodedadosaberto.
Antesdeimplementarosmétodosdeacessoadadosquesãopertinentespara
anossaaplicaç ão,vamosincluiralgumasconstantespararepresentarastabelase
colunasexistentesnobancodedados.Comoasinstruçõesdecriaç ãodobancoficam
naclasse DatabaseHelper,podemosdefiniressasconstanteslá.Vejacomoficou:
public class DatabaseHelper extends SQLiteOpenHelper{
//constantes já existentes
public static class Viagem {
public static final String TABELA = "viagem";
public static final String _ID = "_id";
public static final String DESTINO = "destino";
147

## Página 150

4.6. DicaseboaspráticasaotrabalharcombancodedadosnoAndroid CasadoCódigo
public static final String DATA_CHEGADA = "data_chegada";
public static final String DATA_SAIDA = "data_saida";
public static final String ORCAMENTO = "orcamento";
public static final String QUANTIDADE_PESSOAS =
"quantidade_pessoas";
public static final String TIPO_VIAGEM = "tipo_viagem";
public static final String[] COLUNAS = new String[]{
_ID, DESTINO, DATA_CHEGADA, DATA_SAIDA,
TIPO_VIAGEM, ORCAMENTO, QUANTIDADE_PESSOAS };
}
public static class Gasto{
public static final String TABELA = "gasto";
public static final String _ID = "_id";
public static final String VIAGEM_ID = "viagem_id";
public static final String CATEGORIA = "categoria";
public static final String DATA = "data";
public static final String DESCRICAO = "descricao";
public static final String VALOR = "valor";
public static final String LOCAL = "local";
public static final String[] COLUNAS = new String[]{
_ID, VIAGEM_ID, CATEGORIA, DATA, DESCRICAO, VALOR, LOCAL
};
}
// demais códigos existentes
}
O BoaViagemDAOterámétodosquefazemexatamenteoquejáimplementamos
diretamentena Activity,comadiferen çadeque,emvezderetornarobjetosdo
tipo Cursor,iráretornarlistasdeobjetosdedomínioetambémreceberáobjetos
dotipo Viageme Gastoparasereminseridos.Alémdisso,todasasreferênciasa
tabelasecolunasserãofeitasutilizandoasconstantesdefinidasanteriormente.Um
exemplodemétodoqueteráno DAOéo listarViagens:
public List<Viagem> listarViagens(){
Cursor cursor = getDb().query(DatabaseHelper.Viagem.TABELA,
DatabaseHelper.Viagem.COLUNAS,
null, null, null, null, null);
List<Viagem> viagens = new ArrayList<Viagem>();
148

## Página 151

CasadoCódigo Capítulo4. PersistênciadedadosnoAndroidcomSQLite
while(cursor.moveToNext()){
Viagem viagem = criarViagem(cursor);
viagens.add(viagem);
}
cursor.close();
return viagens;
}
Vocêpodeconsultarocódigocompletodesse DAOnorepositóriodoprojetodo
livro,emhttps://github.com/joaobmonteiro/livro-android.
4.7 Conclusão
Nestecapítulo,apresentamosospassosnecessáriosparacriarumbancodedados
SQLitenoAndroidetambémaprendemoscomorealizarasprincipaisoperações
como insert, update, deletee query.
TambémvimoscomoexecutarinstruçõesSQLarbitráriascomo execSQLe
tambémconsultascomo rawQuery. Alémdisso,utilizamosopadrãoDAOpara
organizarmelhornossocódigoefizemosalgumasrefatoraçõesparamelhorá-lo.
Asfuncionalidadesimplementadassãoparaapersistênciadasinformaçõesde
viagens. Agoraficacomodeverdecasaimplementarasmesmasfuncionalidades
paraosgastos,jáutilizandooDAOapresentado.Casotenhadúvidasouqueiracom-
pararsuaimplementaç ão,consulteocódigo-fontedaaplicaç ãodisponibilizadoem
http://github.com/joaobmonteiro/livro-android.
149

## Página 153

Capítulo5
Compartilhedadosentreaplicações
comosContentProviders
Osprovedoresdeconteúdo(content providers)sãocomponentesdaplataformaAn-
droidutilizadosparaocompartilhamentodedadosentreaplicações,quepodem
estararmazenadosemumbancodedadosSQLitelocal,emarquivosarmazenados
noprópriodispositivooumesmonaweb.
O content providerseresponsabilizaporoferecerumaformasimplesesegura
paraacessaremodificaressesdados,independentementedeondeestejamarmaze-
nados.
Geralmente,osprovedoresdeconteúdodisponibilizamalgumtipodeinterface
gráficaparamanipularosdados,comoéocasodo providerdecontatosdotelefone.
Nestecapítuloveremoscomoutilizarosprovedoresdeconteúdoetambémcria-
remosum content providerparacompartilharnossasinformaçõesdeviagens,arma-
zenadasnoaplicativoBoaViagem.

## Página 154

5.1. ComofuncionaumContentProvider CasadoCódigo
5.1 Como funciona um Content Provider
O ContentProviderexpõeosdadosparaasoutrasaplicaçõesemumaestrutura
tabular,semelhanteàstabelasdosbancosdedadosrelacionais.Cadalinharepresenta
umainstânciadodadoobtidopelo providereascolunasrepresentamasinformações
referentesàquelainstância.
Para acessar um provedor de conteúdo, utilizamos um objeto do tipo
ContentResolverquesecomunicacomo ContentProvidereeste,porsua
vez,recebeasolicitaç ão,executaaaç ãodesejadaeretornaosresultadosobtidos.As
operaçõespossíveisdeum ContentProvidersãoasdecriar,recuperar,atualizar
eremoverdados.
Existemtrêselementosimportantesemum ContentProvider:suas Uris,
ascolunasexistenteseaspermissõesnecessáriasparaacessá-lo.
Uma Urideconteúdoéuma Stringformadaporumnomesimbólicoque
identificaoprovedor(aautoridade)eporumcaminho(o path)queindicaemqual
tabelaosdadosestão. Geralmente,os ContentProvidersdisponibilizamem
formadeconstantesuma Uridiferenteparacadatabelaqueeleexpõe.
Vejaumexemplode Uri,onde com.android.contactséaautoridadedo
providere contactséo path:
content://com.android.contacts/contacts
Essa Uri, além de indicar de onde os dados devem ser obtidos, também
pode conter informações sobre o dado propriamente dito. Por exemplo, um
ContentProviderpodedefinirquealgunssegmentosda Urisãonaverdadepa-
râmetrosdaoperaç ãoqueseráexecutada. Istoébastantecomumem Urisutili-
zadaspararecuperarumdadoapartirdeum idouparaexecutarumaconsulta
informandoumfiltroquesejaaplicadoaváriascolunas. Veremosexemplosassim
maisadiante.
Umavezdeterminadaqualéa Urideacesso,énecessáriosaberemquaisco-
lunasasinformaçõesestão,paraquesepossamobterosdados. Osprovedoresde
conteúdodisponibilizamonomedascolunasexistentestambémnaformadecons-
tantes.Oprovedordecontatos,porexemplo,agrupatodasassuasinformaçõesde
Urisecolunassuportadas,naclasse ContactsContract.
O ContentProvidertambémdefinepermissõesparaquepossaserutilizado.
Issoéespecialmenteimportante,poisgeralmenteosprovedoresdeconteúdosão
utilizadosparapermitirqueoutrasaplicaçõesacessemealteremdadosdeoutra.
152

## Página 155

CasadoCódigo Capítulo5. CompartilhedadosentreaplicaçõescomosContentProviders
Parautilizarmosum ContentProvideremnossaaplicaçãoprecisamosincluiras
permissõesadequadas.
Umaaplicaçãoquepretende,porexemplo,lerealterardadosdecontatosdeve
declararasseguintespermissõesno AndroidManifest.xml:
<uses-permission android:name="android.permission.READ_CONTACTS" />
<uses-permission android:name="android.permission.WRITE_CONTACTS" />
Agoraquejátemospermissõesadequadas,conhecemosa Urieascolunasque
compõemainformaç ãodesejada,precisamosobterum ContentResolverpara
secomunicarcomo ContentProvider.Asclassesqueestendem Context,tais
como Activitye Service,possuemummétodo getContentResolver()
queretornamumainstânciadestetipo.
Apartirdo ContentResolver,podemosexecutarconsultas,inclusão,alte-
raçãoeexclusãodedados,setivermosaspermissõescorretaseaoperaç ãoforsu-
portadapeloprovedor.Osresultadosrecuperadosdeum ContentProvidersão
retornadosemum Cursor.
5.2 Acesse os contatos do telefone
OAndroiddisponibilizaum ContentProviderbastantecompletoparacompar-
tilharosdadosdoscontatosarmazenadosnotelefone,cujasinformaçõesestãoloca-
lizadosemtrêstabelasprincipais.
Natabela ContactsContract.Contactstemosasinformaçõesbásicasde
umadeterminadapessoacomonome(coluna DISPLAY_NAME),seelapossuitele-
fone(coluna HAS_PHONE_NUMBER)eum _IDquepodeserutilizadopararecuperar
osdadosdestapessoasnasdemaistabelas.Elafuncionacomoumagrupadorjáque
umapessoapodeterdiversoscontatos.
Atabela ContactsContract.RawContactsrelacionaoscontatosdeuma
determinadapessoa,quepodemtervindodeserviçosdesincronizaç ãodiferentes
(Google,Twitterououtros).Nestatabelatemosduasinformaçõesimportantesque
sãoonome( ACCOUNT_NAME)eotipo( ACCOUNT_TYPE)dacontadoserviçode
sincronização.
Os dados dos contatos são efetivamente armazenados na tabela
ContactsContract.Data. As demais tabelas existentes são auxiliares e
ajudamnapesquisa.
Paraexecutarumaconsultaemum ContentProviderdevemosforneceruma
Uriqueindiquedeondeosdadosserãoobtidos,umaproje çãoquerepresentaquais
153

## Página 156

5.2. Acesseoscontatosdotelefone CasadoCódigo
informaçõesdevemserrecuperadas,oscritériosdefiltroetambémaordenaç ãode-
sejada,deformabastantesemelhanteaumaconsultanoSQLite.
Paraconseguirmosum Cursorcomasinformaçõesdatabela Contacts,pri-
meiroprecisamosconseguiro ContentResolver,atravésdocontexto,invocando
ométodo getContentResolver(),eemseguidadefinimosa Uriquedevemos
utilizarparao providerdecontatos:
ContentResolver contentResolver = getContentResolver();
Uri uri = Contacts.CONTENT_URI;
Opróximopassoédeclararmosum arrayquerepresentaascolunasquedevem
serretornadas.Nestecaso,escolhemosapenasonomedeexibiç ãodocontato.Não
definimosnenhumcritériodefiltroenemdeordenaç ão.
// Recupera o ContentResolver e define a URI
String[] projection = new String[] { Contacts.DISPLAY_NAME };
String selection = null;
String[] selectionArgs = null;
String sortOrder = null;
Porúltimo,invocamosométodoqueexecutaaconsulta.Comoresultadotemos
um Cursor.
// Recupera o ContentResolver e define a URI
// Monta as informações para a consulta
Cursor cursor = contentResolver.query(uri, projection,
selection, selectionArgs, sortOrder);
Outraoperaçãocomumérealizarumabuscaparcial,combasenonomedocon-
tato.Paraestetipodeconsultaexisteuma Uriespecífica,querealizaabuscapar-
cialnoscamposqueidentificamocontatotaiscomonome,sobrenome,apelidoetc.
Nestecaso,utilizaremosuma Uridefiltronaqualadicionamosocritériodesejado
aofinalda Uri,comosendooseuúltimosegmento.
Paraconseguirfiltrartodososcontatosquepossuemaletra“A”emalgumaparte
donomeeordenarosresultadosdeformaascendente,vamosincluirocritériode
filtrona ContactsContract.Contacts.CONTENT_FILTER_URIutilizandoo
método Uri.withAppendedPathparaconstruira Urinecessária.
154

## Página 157

CasadoCódigo Capítulo5. CompartilhedadosentreaplicaçõescomosContentProviders
ContentResolver contentResolver = getContentResolver();
Uri uri = Uri.withAppendedPath(Contacts.CONTENT_FILTER_URI, "A");
O resultado dessa operação é uma Uri com o seguinte conteúdo:
content://com.android.contacts/contacts/filter/A. Repare que
nestecasonãoprecisamosutilizarosparâmetros selectione selectionArgs
paraexecutaraconsultavistoqueoprovedordecontatosjádisponibilizauma
formaespecíficadefazê-la.
String[] projection = new String[] { Contacts.DISPLAY_NAME };
String selection = null;
String[] selectionArgs = null;
String sortOrder = Contacts.DISPLAY_NAME + " ASC";
Cursor cursor = contentResolver.query(uri, projection,
selection, selectionArgs, sortOrder);
Pronto,játemosaconsultapronta. Porfim,valeressaltarqueéobrigatório
adicionarocritériodefiltrona Uriecasoomesmonãosejainformado, este
ContentProviderlançaráumaexceção.
Afimdefacilitarasconsultas,oprovedordecontatosdisponibilizaentidades,
como Phonee Email,quepodemserentendidascomotabelasgeradasapartir
de joinsentreastrêstabelasprincipais.Nopróximocódigo,utilizaremosaentidade
Phonepararecuperarostelefonesdocontatoquepossuio _IDiguala10:
ContentResolver contentResolver = getContentResolver();
Uri uri = Phone.CONTENT_URI;
String[] projection = new String[] { Phone.NUMBER,
Phone.TYPE };
String selection = Phone.CONTACT_ID + " = ?";
String[] selectionArgs = new String[]{ "10" };
String sortOrder = null;
Cursor cursor = contentResolver.query(uri, projection,
selection, selectionArgs, sortOrder);
Ocódigoébasicamenteomesmoutilizadoanteriormenteparalistarosconta-
tos,modificamosapenasa Urieascolunasqueagorapertencemàentidade Phone.
Tantoaentidade Phonequantoa Emailpossuemumacoluna TYPEqueindicao
155

## Página 158

5.3. CrieumContentProviderparaoseuaplicativo CasadoCódigo
seurespectivotipo.Parasabermaissobreo ContentProviderdecontatoscon-
sulteadocumentaç ão
5.3 Crie um Content Provider para o seu aplicativo
O ContentProvideréumimportantecomponentedaplataformaAndroidque
essencialmentepermiteocompartilhamentodedadosentreasaplicações,disponi-
bilizandooperaçõesdeleituraeescrita.Porquestõesdeseguran ça,porpadrão,não
épossívelacessarqualquertipodedadoqueperten çaaoutraaplicaç ão,sejaeleum
arquivo(deimagem,vídeo,textoetc.)ouumbancodedadosSQLite.Nãoháneces-
sidadedeimplementarumprovedordeconteúdosenãofornecessáriocompartilhar
dadoscomoutrosaplicativos.
Noentanto,podehavernecessidadedequenossoaplicativopossatransferirou
receberdadosdeoutro. Jávimosqueépossívelpassaralgunstiposdedadosvia
Intentsmasquandoovolumedeinformaçõesémaioresãomaisestruturadas,
issonãoésuficiente.Asaídaexistenteéimplementarum ContentProviderpara
tomarcontadessacomunicaç ãoentreaplicativos.
Comoexemplo, suponhaqueprecisamoscompartilhar, sejapornecessidade
oupordiferencial,asinformaçõesdeviagensegastoscomqualqueroutraaplica-
ção.Paraisto,criaremosumprovedordeconteúdoparaoBoaViagemqueconsiste
emestenderaclasse ContentProvidereimplementaralgunsdeseusmétodos.
Alémdissodefiniremosas Uriseaspermissõesnecessáriasparaacessaro provider.
Porquestõesdeorganizaç ão,vamoscriartodasasclassesrelacionadasao provider
deconteúdonopacote br.com.casadocodigo.boaviagem.provider. Crie
nestepacoteumanovaclassechamadade BoaViagemProviderefaçacomque
elaestenda ContentProvider.Aseguirestáocódigodaclassecomosmétodos
aindasemimplementação.Discutiremoscadaumdeleslogoemseguida.
public class BoaViagemProvider extends ContentProvider{
@Override
public boolean onCreate() {
return false;
}
@Override
public Cursor query(Uri uri, String[] projection, String selection,
String[] selectionArgs, String sortOrder) {
156

## Página 159

CasadoCódigo Capítulo5. CompartilhedadosentreaplicaçõescomosContentProviders
return null;
}
@Override
public Uri insert(Uri uri, ContentValues values) {
return null;
}
@Override
public int delete(Uri uri, String selection,
String[] selectionArgs) {
return 0;
}
@Override
public int update(Uri uri, ContentValues values, String selection,
String[] selectionArgs) {
return 0;
}
@Override
public String getType(Uri uri) {
return null;
}
}
O ContentProviderdependedeuma Uri,quealémdedeterminaraopera-
çãodesejada,indicatambémsobrequaisdadoseladeveserexecutada.
Nonossocaso,iremosdisponibilizarcinco Uriscomobjetivosdistintos:
• Inserçãooupesquisadeviagens;
• Atualizaçãoouremo çãodeviagens;
• Pesquisadegastosdeumaviagem;
• Inserçãooupesquisadeumgasto;
• Atualizaçãoouremo çãodeumgasto.
Cada Urideverápossuirumsegmentoqueidentificaoprovedor,tambémco-
nhecidocomoautoridade(authority ),eo pathqueindicaráalocalizaçãodosdados.
Adicionalmente,a Uripodeterumsegmentoqueindicao _IDdodadodesejado.
157

## Página 160

5.3. CrieumContentProviderparaoseuaplicativo CasadoCódigo
Aestruturada Uriémuitoimportanteedeveserescolhidacomcuidado,pois
éapartirdelaqueoprovedortomaráasdecisõessobreoqueexecutar.
Paraas Urisdeviagens,teremosumaparainseriroupesquisarviagensea
outraparaatualizarouremoverumregistro,sendonecessário,nesteúltimocaso,
informaro _IDdaviagemcomoparteda Uri. Faremosomesmoparaas Uris
degastos,alémdedisponibilizarumaespecificamentepararecuperargastosdeuma
determinadaviagem.Aideiaéqueelassejamassim:
// inserir ou pesquisar viagens
content://br.com.casadocodigo.boaviagem.provider/viagem
// atualizar ou remover viagem
content://br.com.casadocodigo.boaviagem.provider/viagem/#
// pesquisar gastos de uma viagem
content://br.com.casadocodigo.boaviagem.provider/gasto/viagem/#
// inserir ou pesquisar gastos
content://br.com.casadocodigo.boaviagem.provider/gasto
// atualizar ou remover gasto
content://br.com.casadocodigo.boaviagem.provider/gasto/#
O #indicaqueaquelesegmentodevecorresponderaumasequênciadecaracte-
resnuméricosdequalquertamanho,ouseja,deveserumnúmeroquerepresentará
o _IDdodadodesejado.
Uma Uritambémpodeconter *,queindicaqueosegmentodeveseruma
Stringdequalquertamanho. Comoasboaspráticasrecomendam,utilizaremos
constantespararepresentaras Uris. Tambéméimportantecriarconstantesque
representamascolunasqueserãorecuperadas,tantoparafacilitarousoporterceiros
quantoparainternamenteorganizarmosocódigoeassimevitarousoexplícitode
Stringe Integer.
Valesalientarqueessascolunasnãosãonecessariamenteasmesmascolunasdo
bancoSQLitedaaplicaç ão. Podemosexporumconjuntodiferentededadosque
inclusivepodenãorefletiraestruturadetabelasexistentesnobancodedados.Por-
tantolembre-sequeapesardasimilaridade,o patheascolunasdo providernãosão
amesmascoisasqueastabelasecolunasdobancodedados.
Crieumaclasse BoaViagemContractquedefiniráascolunase Urisdonosso
ContentProvider,atravésdeconstantes.Elateráoseguintecódigo:
158

## Página 161

CasadoCódigo Capítulo5. CompartilhedadosentreaplicaçõescomosContentProviders
public final class BoaViagemContract {
public static final String AUTHORITY =
"br.com.casadocodigo.boaviagem.provider";
public static final Uri AUTHORITY_URI =
Uri.parse("content://" + AUTHORITY);
public static final String VIAGEM_PATH = "viagem";
public static final String GASTO_PATH = "gasto";
public static final class Viagem{
public static final Uri CONTENT_URI =
Uri.withAppendedPath(AUTHORITY_URI, VIAGEM_PATH);
public static final String _ID = "_id";
public static final String DESTINO = "destino";
public static final String DATA_CHEGADA = "data_chegada";
public static final String DATA_SAIDA = "data_saida";
public static final String ORCAMENTO = "orcamento";
public static final String QUANTIDADE_PESSOAS =
"quantidade_pessoas";
}
public static final class Gasto{
public static final Uri CONTENT_URI =
Uri.withAppendedPath(AUTHORITY_URI, GASTO_PATH);
public static final String _ID = "_id";
public static final String VIAGEM_ID = "viagem_id";
public static final String CATEGORIA = "categoria";
public static final String DATA = "data";
public static final String DESCRICAO = "descricao";
public static final String LOCAL = "local";
}
}
Paracriaras Urisutilizamosdoismétodosutilitários:o Uri.parse,quecria
uma Uriválidaapartirdeuma String,eo Uri.withAppendedPath,queé
utilizadoparaincluirumnovosegmentoauma Uriexistente.
Quandoalgumaoperaçãoforsolicitadaparaonosso ContentProvider,pre-
cisaremosapartirda Urideterminaroquedeveserfeito.Paraisso,utilizaremosa
classeutilitária UriMatcherquefazacomparaç ãoda Uriinformadapelousuário
comas Urisdefinidas,retornandoumvalorpreviamentedefinidoindicandoqual
foia Uriemquehouveo matching,comoaseguir:
159

## Página 162

5.3. CrieumContentProviderparaoseuaplicativo CasadoCódigo
int VIAGENS = 1;
UriMatcher uriMatcher = new UriMatcher(UriMatcher.NO_MATCH);
uriMatcher.addURI(AUTHORITY, VIAGEM_PATH, VIAGENS);
if(uriMatcher.match(uri) == VIAGENS){
// operação de listar viagens
}
Nestetrechodecódigo,criamosa UriMatchereadicionamosa Uriquecor-
respondeàoperaç ãodepesquisarviagens. Ovalor VIAGENSseráutilizadopara
compararoretornodométodo UriMatcher.matche,casosejamiguais,querdi-
zerquea Uriinformadaéadepesquisadeviagens.
Énecessárioadicionarao UriMatchercada Uriqueseráutilizadapelopro-
vedor.Portantonaclasse BoaViagemProviderteremosocódigoparaisso:
import static br.com.casadocodigo.boaviagem.BoaViagemContract.*;
public class BoaViagemProvider extends ContentProvider {
private static final int VIAGENS = 1;
private static final int VIAGEM_ID = 2;
private static final int GASTOS = 3;
private static final int GASTO_ID = 4;
private static final int GASTOS_VIAGEM_ID = 5;
private static final UriMatcher uriMatcher =
new UriMatcher(UriMatcher.NO_MATCH);
static{
uriMatcher.addURI(AUTHORITY, VIAGEM_PATH, VIAGENS);
uriMatcher.addURI(AUTHORITY, VIAGEM_PATH + "/#", VIAGEM_ID);
uriMatcher.addURI(AUTHORITY, GASTO_PATH, GASTOS);
uriMatcher.addURI(AUTHORITY, GASTO_PATH + "/#", GASTO_ID);
uriMatcher.addURI(AUTHORITY,
GASTO_PATH + "/"+ VIAGEM_PATH + "/#", GASTOS_VIAGEM_ID);
}
160

## Página 163

CasadoCódigo Capítulo5. CompartilhedadosentreaplicaçõescomosContentProviders
// demais códigos existentes
}
Assim,adicionamosascinco Urisqueiremosutilizarepoderemosposterior-
menteinvocarométodo UriMatcher.matchparadeterminarqualoperaç ãodeve
serrealizada.
Já temos as definições e a estrutura doContentProvider prontas e
agora partiremos para a implementação dos seus métodos. Como nossos da-
dos estão armazenados em um bancoSQLite, utilizaremos a nossa classe
DatabaseHelper para acessá-lo. A sua instanciação será feita no método
onCreatedo BoaViagemProvider.
private DatabaseHelper helper;
@Override
public boolean onCreate() {
helper = new DatabaseHelper(getContext());
return true;
}
Opróximométodoaserimplementadoéo query,pararealizarconsultasno
provedordeconteúdo. Apartirda Uriinformadacomoparâmetro,determina-
remosqualéaconsultaquedeveserrealizada. Come çaremospelasconsultasde
viagensevamosprecisardeumainstânciade SQLiteDatabase,queconseguimos
atravésdo DatabaseHelperqueacabamosdeinstanciarnométodo onCreate:
@Override
public Cursor query(Uri uri, String[] projection, String selection,
String[] selectionArgs, String sortOrder) {
SQLiteDatabase database = helper.getReadableDatabase();
// as consultas virão aqui
}
Agoratemosquefazeracomparaç ãoda Uriinformadacomaquelascarregadas
previamenteno UriMatcher.Casoa Uriinformadasejaade VIAGENS,execu-
tamosumaconsultanatabela viagem.
161

## Página 164

5.3. CrieumContentProviderparaoseuaplicativo CasadoCódigo
switch (uriMatcher.match(uri)) {
case VIAGENS:
return database.query(VIAGEM_PATH, projection,
selection, selectionArgs, null, null, sortOrder);
}
Aqui, propositadamente fizemos opath coincidir com o nome da tabela
a que ele se refere. Repare também que os parâmetros recebidos pelo mé-
todo ContentProvider.query são praticamente os mesmos recebidos pelo
SQLiteDatabase.query. Entãosimplesmenterepassamososparâmetrospara
queaconsultasejaexecutada. Lembre-sequeemalgunscasospodesernecessá-
riovalidarouchecarosparâmetrosrecebidosparagarantiraexecuç ãocorretada
operação.
Casoa Urifor VIAGEM_ID,anossaconsultadeveráterumacláusula where
pararestringiraconsultacombaseno _IDinformado. Paraisso,recuperamoso
últimosegmentoda Uri,querepresentao _IDdoregistro,utilizandoométodo
uri.getLastPathSegmenteexecutamosaconsultadesejada.
Porfim,nocasoda Uriinformadanãocoincidircomnenhumadasdefinidas
no UriMatcher,lan çamosumaexce ção.
case VIAGEM_ID:
selection = Viagem._ID + " = ?";
selectionArgs = new String[] {uri.getLastPathSegment()};
return database.query(VIAGEM_PATH, projection,
selection, selectionArgs, null, null, sortOrder);
default:
throw new IllegalArgumentException("Uri desconhecida");
Agorapodemosfazerasconsultasparaosgastos,quefuncionarãodeformasi-
milaràsdeviagens.Vamosusarasconstantes GASTOSe GASTO_ID:
case GASTOS:
return database.query(GASTO_PATH, projection,
selection, selectionArgs, null, null, sortOrder);
case GASTO_ID:
selection = Gasto._ID + " = ?";
selectionArgs = new String[] {uri.getLastPathSegment()};
return database.query(GASTO_PATH, projection,
selection, selectionArgs, null, null, sortOrder);
162

## Página 165

CasadoCódigo Capítulo5. CompartilhedadosentreaplicaçõescomosContentProviders
utilizacomorestriçãoa VIAGEM_ID.Vejaentãocomoficouocódigocompleto
dométodo query:
case GASTOS_VIAGEM_ID:
selection = Gasto.VIAGEM_ID + " = ?";
selectionArgs = new String[] {uri.getLastPathSegment()};
return database.query(GASTO_PATH, projection,
selection, selectionArgs, null, null, sortOrder);
Aimplementaçãodométodo insertébastantesimples,poisjárecebemos
comoparâmetroum ContentValuesquecontémosdadosqueousuáriode-
sejainseriretambémnãofazemosnenhumarestriç ão. Aocontráriodométodo
insertdo SQLiteDatabaseque retorna o_IDdo registro inserido, o do
ContentProviderretornauma Uriqueorepresenta. Dessaforma,apósreali-
zarainser ção,retornaremosuma Uricontendoo _IDdonovoregistro.
@Override
public Uri insert(Uri uri, ContentValues values) {
SQLiteDatabase database = helper.getWritableDatabase();
long id;
switch (uriMatcher.match(uri)) {
case VIAGENS:
id = database.insert(VIAGEM_PATH, null, values);
return Uri.withAppendedPath(Viagem.CONTENT_URI,
String.valueOf(id));
case GASTOS:
id = database.insert(GASTO_PATH, null, values);
return Uri.withAppendedPath(Gasto.CONTENT_URI,
String.valueOf(id));
default:
throw new IllegalArgumentException("Uri desconhecida");
}
}
Aimplementaçãodométodo updateésemelhanteàrealizadano insertjá
quetambémtemoso ContentValuescomoparâmetro.Adiferen çaéquerecebe-
mosdoisparâmetrosamaisquerepresentamacláusula wheredainstruçãoSQLde
163

## Página 166

5.3. CrieumContentProviderparaoseuaplicativo CasadoCódigo
UPDATE,oprimeiroparâmetroéuma stringcomoscamposeosegundoéum
arraycomosrespectivosvalores. Ométodo deletetambémrecebeessesdois
parâmetrosalémda Uri.
Agora precisamos adicionar suporte à alteração e exclusão de informações
deacordocomo _ID.Utilizaremosas Urisquecontenhamo _IDdodado
alémdesubstituirosparâmetrosrecebidosparaincluiressarestriç ão. Paraaex-
clusãotantodogasto, quantodaviagem, faremosusodométodo deletedo
SQLiteDatabase:
@Override
public int delete(Uri uri, String selection, String[] selectionArgs) {
SQLiteDatabase database = helper.getWritableDatabase();
switch (uriMatcher.match(uri)) {
case VIAGEM_ID:
selection = Viagem._ID + " = ?";
selectionArgs = new String[] {uri.getLastPathSegment()};
return database.delete(VIAGEM_PATH,
selection, selectionArgs);
case GASTO_ID:
selection = Gasto._ID + " = ?";
selectionArgs = new String[] {uri.getLastPathSegment()};
return database.delete(GASTO_PATH,
selection, selectionArgs);
default:
throw new IllegalArgumentException("Uri desconhecida");
}
}
Eparaaalteraç ão,temosquechamarométodo updatedo SQLiteDatabase:
@Override
public int update(Uri uri, ContentValues values,
String selection, String[] selectionArgs) {
164

## Página 167

CasadoCódigo Capítulo5. CompartilhedadosentreaplicaçõescomosContentProviders
SQLiteDatabase database = helper.getWritableDatabase();
switch (uriMatcher.match(uri)) {
case VIAGEM_ID:
selection = Viagem._ID + " = ?";
selectionArgs = new String[] {uri.getLastPathSegment()};
return database.update(VIAGEM_PATH, values,
selection, selectionArgs);
case GASTO_ID:
selection = Gasto._ID + " = ?";
selectionArgs = new String[] {uri.getLastPathSegment()};
return database.update(GASTO_PATH, values,
selection, selectionArgs);
default:
throw new IllegalArgumentException("Uri desconhecida");
}
}
Oúltimométododoprovedordeconteúdoquedeveserimplementadoéo
getType.Estemétododeveretornaruma StringnoformatoMIMEquerepre-
sentaotipodedadoretornadoporumadeterminada Uri. Comonosso provider
lidacomtabelas,énecessárioretornarumformatoMIMEespecíficodoAndroid
(vendor-specific MIME format). Senosso ContentProviderutilizassearquivos,
poderíamosutilizarostiposMIMEexistentes,comoporexemplo image/jpeg.
Em se tratando de tabelas, podemos retornar uma determinada li-
nha ou um conjunto. O Android disponibiliza respectivamente os tipos
vnd.android.cursor.item e vnd.android.cursor.dir para estes
casos. Além disso, também temos que identificar oprovidere o tipo do dado
retornado. Vejacomoficaa StringquerepresentaotipoMIMEdas Urisde
viagem:
// uma única viagem
"vnd.android.cursor.item/vnd.br.com.casadocodigo.boaviagem.provider
/viagem"
165

## Página 168

5.3. CrieumContentProviderparaoseuaplicativo CasadoCódigo
// uma lista de viagens
"vnd.android.cursor.dir/vnd.br.com.casadocodigo.boaviagem.provider
/viagem"
Estes tipos também devem constar na nossa classe de contrato
BoaViagemContract. Então vamos incluir mais algumas constantes para
representá-los:
public static final class Viagem {
public static final String CONTENT_TYPE =
"vnd.android.cursor.dir/" +
"vnd.br.com.casadocodigo.boaviagem.provider/viagem";
public static final String CONTENT_ITEM_TYPE =
"vnd.android.cursor.item/" +
"vnd.br.com.casadocodigo.boaviagem.provider/viagem";
// demais constantes
}
public static final class Gasto {
public static final String CONTENT_TYPE = "vnd.android.cursor.dir/"+
"vnd.br.com.casadocodigo.boaviagem.provider/gasto";
public static final String CONTENT_ITEM_TYPE =
"vnd.android.cursor.item/" +
"vnd.br.com.casadocodigo.boaviagem.provider/gasto";
// demais constantes
}
Aimplementaçãodométodo getTyperetornaráessestiposdeacordocoma
Uriinformada,entãoprecisamosimplementaro switchquefaráadevoluçãoda
Stringadequadareferenteao CONTENT_TYPE:
@Override
public String getType(Uri uri) {
switch (uriMatcher.match(uri)) {
case VIAGENS:
return Viagem.CONTENT_TYPE;
166

## Página 169

CasadoCódigo Capítulo5. CompartilhedadosentreaplicaçõescomosContentProviders
case VIAGEM_ID:
return Viagem.CONTENT_ITEM_TYPE;
case GASTOS:
case GASTOS_VIAGEM_ID:
return Gasto.CONTENT_TYPE;
case GASTO_ID:
return Gasto.CONTENT_ITEM_TYPE;
default:
throw new IllegalArgumentException("Uri desconhecida");
}
}
Nocasoda Uriserde GASTOSou GASTOS_VIAGEM_ID,otiporetornadoé
sempreumalistadegastos,porissoo CONTENT_TYPEdeveseromesmo,ficandoo
casede GASTOSembranco.Agoraquejátemostodososmétodosimplementados,
sófaltaadicionaro ContentProviderno AndroidManifest.xmleelejáestará
prontoparaserusado!Adicioneumelemento <provider>,dessaforma:
<provider
android:name=".provider.BoaViagemProvider"
android:authorities="br.com.casadocodigo.boaviagem.provider" >
</provider>
Epronto,acabamosdeimplementarnosso provider.
5.4 Adicione regras de permissão ao seu Content-
Provider
Porpadrão,o ContentProvidernãopossuinenhumtipodepermissão. Dessa
forma,qualqueraplicativopodeacessaroprovedorerealizaroperações,oquepode
seralgoindesejável,dependendodacircunstância.Noentanto,épossívelacrescentar
permissõesglobaisparaaleituraeescrita,permissõesparaapenasalgumastabelas
ouaindaparaalgunsregistros,outambémcombinartodosessestiposdepermissões.
Aspermissõessãodefinidasnomanifestojuntamentecomadeclaraç ãodopro-
vedoreelastambémprecisamterumnomeúnico,porisso,utilizamosonomedo
167

## Página 170

5.5. Conclusão CasadoCódigo
pacoteemsuacomposiç ão.
Paradefinirumapermissãoglobalparaescritaeleituradonossoprovedor,pode-
mosutilizaroatributo android:permissiondoelemento <provider>,assim:
<provider
android:name=".provider.BoaViagemProvider"
android:authorities="br.com.casadocodigo.boaviagem.provider"
android:permission=
"br.com.casadocodigo.boaviagem.provider.permission.ALL">
</provider>
Para dividir as permissões de leitura e escrita, podemos usar o
android:readPermissioneo android:writePermission:
<provider
android:name=".provider.BoaViagemProvider"
android:authorities="br.com.casadocodigo.boaviagem.provider"
android:readPermission=
"br.com.casadocodigo.boaviagem.provider.permission.READ"
android:writePermission=
"br.com.casadocodigo.boaviagem.provider.permission.WRITE">
</provider>
Deformamaisespecífica,podemosutilizaroelemento <path-permission>
paradefinirpermissõesparaumdeterminado path,sendopossívelentãorestringir
oacessoatabelaseregistros.Dessemodo,podemosrestringiracessoàsviagens:
<provider
android:name=".provider.BoaViagemProvider"
android:authorities="br.com.casadocodigo.boaviagem.provider" >
<path-permission
android:path="viagem"
android:permission=
"br.com.casadocodigo.boaviagem.provider.permission.ALL" />
</provider>
Oaplicativoquedesejautilizaro BoaViagemProviderdeveráincluir,emseu
respectivomanifesto,aspermissõescorretasparaconseguiracessá-lo.
5.5 Conclusão
Neste capítulo exploramos mais um dos componentes da plataforma, o
ContentProvider, cuja função principal é o compartilhamento de dados
168

## Página 171

CasadoCódigo Capítulo5. CompartilhedadosentreaplicaçõescomosContentProviders
entreaplicações.Entendemoscomoosprovedoresdeconteúdofuncionamatravés
deexemplosdeusodoprovedordecontatos. Porfim,criamosonossopróprio
ContentProviderparaoaplicativoBoaViagem,compermissõesespecíficaspara
escritaeleitura.
169

## Página 173

Capítulo6
IntegraçãodeaplicaçõesAndroid
comserviçosREST
Nossaaplicaçãoatingiuumconjuntodefuncionalidadesrazoável,comoqualpode-
moscadastrarepesquisarviagensegastos.Porém,algumasvezes,funcionalidades
interessantesacabamindoalémdosdadosquetemosdisponíveisemnossaaplica-
ção.Colocarumamensagemdiretonasredessociaisdousuárioedescobriroque
aspessoascomentamsobreumdeterminadoassuntosãoexemplosdisso.Comofa-
zemosparaterosdadosdessasaplicações?
Algoquetemsetornadobastantecomuméqueasaplicações,tantowebcomo
mobileeatémesmoaplicações desktop,utilizemserviçosremotosdisponibilizados
poroutrasaplicações.Osusuáriosesperamcadavezmaiscentralizaç ãoeintegraç ão
dedados,comointuitodetrazeracessorápidoecomodidade,obtendoasinforma-
çõesliteralmentecomapontadosdedos.
GrandesempresascomoFacebook,Twitter,GoogleeYahoo! disponibilizam
acessoremotoaseusserviçosatravésdeumaAPIepodemosutilizá-losparaen-

## Página 174

6.1. TrabalhecomRESTeJSON CasadoCódigo
riquecernossasaplicações.
Nestecapítulovocêaprenderácomoconsumirserviçosremotosemumaaplica-
çãoAndroid.Aproveitaremostambémparaaprendermaissobreoutroscomponen-
tesdaplataforma,os Serviceseos BroadcastReceivers.
Terminologia
Utilizaremosmuitosvezesotermo serviçoaolongodestecapítulo
comosinônimodeserviçosremotose webservices.Paraevitarconfusão,
quandoestivermosnosreferindoaocomponentedaplataformaAndroid
demesmonome,utilizaremosotermo service.
6.1 Trabalhe com REST eJSON
Umtipode webserviceemespecialtemseconsolidadocomopadrãoquandosetrata
dedisponibilizarserviçosnaweb.Trata-sedosserviçosdotipoRESTquepossuem
basicamentecincopremissas:
• UtilizarosmétodosdoprotocoloHTTPpararepresentarasoperaçõesque
podeserexecutadaspeloserviço;
• ExporasinformaçõesatravésdeURLsrepresentativas,similaraumaestrutura
dediretórios;
• Oserviçonãodevearmazenarestadoentrerequisições;
• TransmitirosdadosemformatoXMLe/ouJSON;
• Ousodehypermediapararepresentarpossíveistransições.
Comoresultado,oquetemosentãoéumaURLque,quandoacessada,utilizando
ométodoHTTPcorretoeosparâmetrosnecessários,retornadadosemformato
texto.DeformasimplistaistoéumserviçoREST.Estasimplicidadeefacilidadeper-
mitemseuusoempraticamentequalquertipodeplataforma,desde webatémobile.
Quandopedimosinformaçõesparaumoutroserviço,eleprecisanostransfe-
rirosdadosquepedimos,paraquepossamosdecidiroquefazercomeleemnossa
aplicação.Paratrafegarasinformações,poderíamosutilizartantooconhecidofor-
matoXML,comooJSON, JavaScript Object Notation,queéumformatosimples
172

## Página 175

CasadoCódigo Capítulo6. IntegraçãodeaplicaçõesAndroidcomserviçosREST
utilizadopararepresentardados,voltadoprincipalmenteparaaconversãodedados
estruturadosparaaformatextual.Esseformatoécapazderepresentarquatrotipos
primitivos(números, strings,valoresbooleanose null)edoistiposestruturados
(objetose arrays). Considerandoasinformaçõesdeumlivro,teríamosumJSON
parecidocomoseguinte:
{
"Livro": {
"titulo": "Introdução ao desenvolvimento Android",
"editora": "Casa do Código",
"autores": [
"João Bosco O. Monteiro"
],
"anoPublicacao": 2012
}
}
Vamoslevaremconsideraç ãoumaplicativoparaauxiliarousuárioamanter
registrossobreoslivrosqueeleleuetambémdoslivrosqueelepossui.Seriainteres-
santequeousuáriopudessepesquisareescolherolivroemvezdeterquecadastrar
todasasinformaçõesdomesmo,taiscomotítulo,autor,editoraetc.Nãoseriamais
simplesseexistisseumserviçojáprontoqueatravésdeumaURL,nosfornecesseos
dadosdeumdeterminadolivro,numformatosimplesdeprocessarcomooJSON?
Poisbem,esteserviçoexisteesechamaGoogleBooksAPI.Vocêpodeacessá-
loutilizandooseupróprionavegador,paravercomofuncionaumserviçoRESTe
verificarosdadosretornadosemformatoJSON.Paratestar,acesseaseguinteURL:
https://www.googleapis.com/books/v1/volumes?q=android
Oresultadoobtidoéumalistadelivros,contendotítulo,autores,datadepubli-
caçãoeváriasoutrasinformações:
{
"kind": "books#volumes",
"totalItems": 1253,
"items": [
{
"kind": "books#volume",
"id": "wH1gzgAACAAJ",
"etag": "esMB5pqt+jI",
173

## Página 176

6.1. TrabalhecomRESTeJSON CasadoCódigo
"selfLink":
"https://www.googleapis.com/books/v1/volumes/wH1gzgAACAAJ",
"volumeInfo": {
"title": "Android in Action",
"authors": [
"W. Frank Ableson",
"Robi Sen",
"Chris King",
"C. Enrique Ortiz"
],
"publisher": "Manning Pubns Co",
"publishedDate": "2011-09-28",
"description": "Android is a free, open source...",
"industryIdentifiers": [
{
"type": "ISBN_10",
"identifier": "1617290505"
},
{
"type": "ISBN_13",
"identifier": "9781617290503"
}
]
AGoogleBooksAPIébastantepoderosaeutilizamosapenasumadasfunciona-
lidadesparaexemplificarumserviçoREST.AnalisandoesseJSONvocêpodeachar
queserácomplicadotrabalharcomesseformato,masfiquetranquilo,poisoAndroid
possuialgumasclassescomoa JSONObjectparafacilitarotrabalho.Alémdisso,
existemoutrasbibliotecascomoaGson(http://code.google.com/p/google-gson/)do
próprioGoogleeaJackson(http://jackson.codehaus.org/)quetrazemaindamaisfa-
cilidadesparaamanipulaç ãodedadosemformatoJSON.
AgoraquejásabemosobásicosobreREST,quetalimplementarumaplicativo
querealizaconsultasnoTwitteretambémnotificaquandoalguémnosmenciona
emalgum tweet?Essaéumasituaç ãointeressantepoisseráconstruídacomimple-
mentaçõesquesãobastantecomunsquandosetrabalhacomserviçosREST.
Porexemplo,utilizaremostarefasassíncronas, AsyncTasks,doAndroidpara
realizarrequisiçõesHTTP,criaremos threadserealizaremosexecuçõesperiódicas
emum ServicedoAndroid.Alémdisso,utilizaremosum BroadcastReceiver
parainiciarautomaticamentenossoaplicativoquandoodispositivoforiniciado.
174

## Página 177

CasadoCódigo Capítulo6. IntegraçãodeaplicaçõesAndroidcomserviçosREST
6.2 Conheça a Twitter SearchAPI
DamesmaformaquefizemoscomoGoogleBooksAPI,nossooprimeirocontato
comaAPIdebuscadoTwitterseráutilizandoonavegador. AcesseaURLabaixo
quefazumapesquisaportodosos tweetsquemencionamousuário @android:
http://search.twitter.com/search.json?q=@android
OretornoseráemformatoJSON,aproximadamentecomomostraaimagem 6.1.
Sãoapresentadosapenasos tweetsmaisrecentes. DiferentementedoJSONobtido
daBooksAPI,estenãoestáformatado,sendovisualmentedifícildeidentificarquais
dadosaconsultaretornou.
Figura6.1:JSONobtidodeumaconsultanoTwitter
Comoesteénossoprimeirocontato,nãovamosrecorrerdiretamenteparaado-
cumentaçãodaAPIqueinformaquaissãotodososdadosretornados. Iremosre-
correraosite http://www.jsonlint.org,quepossuiumafuncionalidadeinteressante
devalidaçãoeformataç ãodetextoemformatoJSON.Bastacopiarecolaroretorno
175

## Página 178

6.2. ConheçaaTwitterSearchAPI CasadoCódigo
obtidodoTwitternocampodetextodositeeescolheraop çãodevalidaç ão.Aima-
gem6.2mostracomoficouaformataç ãodoresultadodapesquisaanterior.
Figura6.2:JSONobtidodeumaconsultanoTwitter
Nãoentraremosemdetalhessobretodososatributoseop çõesdeconsultaexis-
tentes.VamosnosfocaremrealizarumapesquisanoTwitter,utilizandoostermos
informadospelousuário,etambémrealizarumabuscaespecíficasobremen çõesa
umdeterminadousuário,daformamaissimplespossível. Paraisto,precisaremos
utilizarbasicamentequatroatributosquesãoretornadosnaconsulta.Identifique-os
noJSONobtido:
•refresh_url-URLutilizadapararepetiraconsultaapartirdoúltimo tweet
recuperado.
•results- arraycomos tweetsencontrados.
•from_user-usuárioquerealizouo tweet
•text-textodo tweet
176

## Página 179

CasadoCódigo Capítulo6. IntegraçãodeaplicaçõesAndroidcomserviçosREST
Casoqueiraseaprofundar,adocumentaç ãocompletadaTwitterAPIestádis-
ponívelemhttps://dev.twitter.com/docs.
6.3 Faça consultas no Twitter
Jásabemosonecessárioparainiciaraimplementaç ãodanossabuscanoTwitter!
Crieumnovoprojetocomonomede TwitterSearch.Selecionecomo target
oAndroid2.3e br.com.casadocodigo.twittersearchcomonomedopa-
cote.Apósacriaç ãodoprojeto,nãoseesque çadeincluirapermissãoparaacessoà
Internetno AndroidManifest.xml:
<uses-permission android:name="android.permission.INTERNET"/>
Anossa activityprincipalteráumlayoutsimples,comum EditTextparao
usuárioinformarostermosdapesquisa,um Buttonparadispararaconsultae
uma ListViewparaapresentarosresultados,noarquivo main.xml.Aimagem
6.3mostracomoficaráanossaaplicaç ão.
Figura6.3:PesquisanoTwitter
177

## Página 180

6.3. FaçaconsultasnoTwitter CasadoCódigo
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
android:layout_width="fill_parent"
android:layout_height="fill_parent"
android:orientation="vertical" >
<LinearLayout
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:orientation="horizontal" >
<EditText
android:id="@+id/texto"
android:layout_width="250dp"
android:layout_height="wrap_content"
android:inputType="text"
android:singleLine="true" />
<Button
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:onClick="buscar"
android:text="@string/buscar" />
</LinearLayout>
<ListView
android:id="@+id/lista"
android:layout_width="wrap_content"
android:layout_height="wrap_content" >
</ListView>
</LinearLayout>
Eprecisamostambémdasmensagens,noarquivo strings.xml.
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="app_name">TwitterSearch</string>
<string name="buscar">Buscar</string>
</resources>
178

## Página 181

CasadoCódigo Capítulo6. IntegraçãodeaplicaçõesAndroidcomserviçosREST
A TwitterSearchActivity,quefoicriadajuntamentecomoprojeto,por
enquantoapenasinicializaasvariáveiscorrespondentesaos widgetsedefineomé-
todo buscar,ficandoassim:
public class TwitterSearchActivity extends Activity {
private ListView lista;
private EditText texto;
@Override
public void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.main);
lista = (ListView) findViewById(R.id.lista);
texto = (EditText) findViewById(R.id.texto);
}
public void buscar(View v) {
}
}
PararealizaraconsultanoTwitterfaremosumarequisiç ãoHTTP.Noentanto,
nãodevemos(enempodemos)acessararedeapartirda threadqueestárodando
a activity(UI thread).Qualquertipodeprocessamentoouoperaç ãoquesejademo-
radanãodeveserexecutadanaUI thread,poisistobloqueariaainterfacegráfica
epoderiacausaroerrode Application Not Responding(ANR).
EspecificamentenocasodeacessoàInternetapartirda threadprincipal,o
Androidlan çaumaexce çãoenãopermitearealizaç ãodaoperaç ão.
Paraessasituaç ão,oAndroiddisponibilizaatravésdaclasse AsyncTaskuma
formasimplesdecriartarefasassíncronasqueexecutamoperaçõesem background
(emoutra thread)equepodempublicarosresultadosdaoperaç ãonaUI thread.
Iremosutilizá-lapararealizarabuscanoTwitter,atualizaranossa ListViewe
controlarum ProgressDialog. A AsyncTaskéumaclassegenéricaeutiliza
trêstipos:
•Params-éotipodosparâmetrosquesãoenviadosparaaexecuç ãodatarefa.
Porexemplo,podeseruma StringquerepresentaaURLdapesquisaque
deveserrealizada.
179

## Página 182

6.3. FaçaconsultasnoTwitter CasadoCódigo
•Progress-éotipoquerepresentaaunidadedeprogressodatarefa.Podeser
o Integer,representandoaporcentagemdeprogressodeumaoperaç ãode
downloadouaindaumaclassesuaquecontenhaoutrosatributosquepossam
realizarestaindicaç ão.
•Result-éotipoderetornodaoperaç ãorealizada.Podeserum arraycom
todosos tweetsobtidosnaconsulta,porexemplo.
Quandouma AsyncTaskéexecutada,elapercorrequatroetapas(métodos):
1) onPreExecute-invocadonaUI threadantesdatarefaserexecutada.Neste
passogeralmentepreparamosaexecuç ãodaoperaç ão,oquepode,porexemplo,
incluiraexibiçãodeum ProgressDialog.
2) doInBackground-éinvocadoemumaoutra threadeéondeaoperaçãodeve
serimplementada.Estemétodorecebeos Paramsdefinidospela AsyncTask
eretornaosresultadosdaoperaç ãocomosendodotipo Result.Nestemétodo
podemosinvocaro publishProgessparainformaroandamentodaoperaç ão.
3) onProgressUpdate - este método é invocado na UIthread após o
publishProgressser executado. Aqui podemos utilizar o valor (do tipo
Progress)informadoparafazerpossíveisatualizaçõesdetela,comoporexem-
ploatualizaroprogressodeum ProgressBar.
4) onPostExecute-tambéminvocadonaUI thread, estemétodorecebeo
Resultcomoparâmetroefazasatualizaçõesdetelanecessárias,comofechar
o ProgressDialogeatualizaruma ListViewcomosdadosobtidosdomé-
todo doInBackground.
Oúnicométodoquedevemosobrigatoriamenteimplementarquandoestende-
mosaclasse AsyncTaskéo doInBackground.
Dentroda TwitterSearchActivity,vamoscriarumaclasseprivadaque
estendede AsyncTask,parainvocaroserviçodoTwitter,chamada TwitterTask.
Duranteestaoperaç ão,vamosexibirum ProgressDialognatelaeaofinaldo
processamentoiremosatualizara ListViewcomos tweetsencontrados.Aimagem
6.4demonstracomoficaráanossacaixadediálogoinformandoqueaoperaç ãoestá
emandamento.
180

## Página 183

CasadoCódigo Capítulo6. IntegraçãodeaplicaçõesAndroidcomserviçosREST
Figura6.4:PesquisanoTwitter
Começamoscomadeclaraç ãodaclasse,definindoqueo Paramsédotipo
String,poisiremospassarostermosdapesquisaquedeveserrealizada. Jáo
Progressédefinidocomo Void,ouseja,nãofaremosaatualizaç ãodeprogresso,
eotipoderetornoéum String[]comos tweetsencontrados.
private class TwitterTask extends AsyncTask<String, Void, String[]> {
}
Nométodo onPreExecuteexibimosum ProgressDialogsimpleseno
onPostExecutefechamoseste dialogapósconstruirum ArrayAdaptercomos
resultadoseatribuí-loanossa ListView.
private class TwitterTask extends AsyncTask<String, Void, String[]> {
ProgressDialog dialog;
181

## Página 184

6.3. FaçaconsultasnoTwitter CasadoCódigo
@Override
protected void onPreExecute() {
dialog = new ProgressDialog(TwitterSearchActivity.this);
dialog.show();
}
@Override
protected void onPostExecute(String[] result) {
if(result != null){
ArrayAdapter<String> adapter =
new ArrayAdapter<String>(getBaseContext(),
android.R.layout.simple_list_item_1, result);
lista.setAdapter(adapter);
}
dialog.dismiss();
}
}
Paraimplementarométodo doInBackground,precisamosrealizarumare-
quisiçãoHTTPparaumaURL,queserámontadaapartirdostermosdebuscain-
formadoscomoparâmetroeemseguida,processaremosarepostaobtidaqueestá
emformatoJSON,criandoum String[]comosdadosdos tweets.
Comofazerumarequisiç ãoHTTPecapturararespostasãotarefascorriqueiras,
vamoscriarumaclasse,chamada HTTPUtilsparaencapsularestaimplementaç ão.
Nestaclasseteremosummétodochamado acessar,querecebeuma String
comoparâmetroqueéaURLdesejadaeretornauma Stringqueéoconteúdo
obtidocomorespostadasolicitaç ão.
Nasuaimplementação,abrimosumaconexãoapartirdoendere çoinformadoe
naslinhasseguintesfazemosaleituradosdadosrecebidosutilizandoum Scanner.
public class HTTPUtils {
public static String acessar(String endereco){
try {
URL url = new URL(endereco);
URLConnection conn = url.openConnection();
InputStream is = conn.getInputStream();
182

## Página 185

CasadoCódigo Capítulo6. IntegraçãodeaplicaçõesAndroidcomserviçosREST
Scanner scanner = new Scanner(is);
String conteudo = scanner.useDelimiter("\\A").next();
scanner.close();
return conteudo;
} catch (Exception e) {
return null;
}
}
}
Agora precisamos implementar o métododoInBackground na nossa
AsyncTaskchamada TwitterTask.
@Override
protected String[] doInBackground(String... params) { }
Precisamosfazerumavalidaç ãosimples,paraevitararealizaç ãodeconsultas
semqueostermosdesejadostenhamsidoinformados. Emseguida,utilizamoso
método Uri.parseparaconstruirumaURLválidajáincluindoostermosdapes-
quisa.Estecuidadoénecessáriopoisalgunscaracteresdevemserconvertidospara
formarumaURLválida—éocasodo @quesetransformaem %40 edoespaço
embrancoquesetorna %20 . Etambémchamamosométodo acessar,para
recuperarmosoconteúdodaURL.
@Override
protected String[] doInBackground(String... params) {
try {
String filtro = params[0];
if(TextUtils.isEmpty(filtro)){
return null;
}
String urlTwitter = "http://search.twitter.com/search.json?q=";
String url = Uri.parse(urlTwitter + filtro).toString();
String conteudo = HTTPUtils.acessar(url);
183

## Página 186

6.3. FaçaconsultasnoTwitter CasadoCódigo
// vamos usar o conteúdo
} catch (Exception e) {
throw new RuntimeException(e);
}
}
Depoisdeinvocarométodo HTTPUtils.acessar,criamosum JSONObject
apartirdoconteúdorecebidodoserviço.Atravésdelepoderemosacessarosatribu-
tosdesejadossemprecisarmanipularas Stringsdaresposta.Emseguida,utiliza-
mosométodo getJSONArrayinformandooatributo( "results")quearmazena
os tweetsemformatode array.
@Override
protected String[] doInBackground(String... params) {
try {
String filtro = params[0];
if(TextUtils.isEmpty(filtro)){
return null;
}
String urlTwitter = "http://search.twitter.com/search.json?q=";
String url = Uri.parse(urlTwitter + filtro).toString();
String conteudo = HTTPUtils.acessar(url);
// pegamos o resultado
JSONObject jsonObject = new JSONObject(conteudo);
JSONArray resultados = jsonObject.getJSONArray("results");
} catch (Exception e) {
throw new RuntimeException(e);
}
}
Paracadaresultadoobtido,criamosumnovo JSONObjectpararecuperaros
dadosespecíficosquedesejamosdecada tweet,quesãooseutextoeousuárioque
orealizou.Apósextrairessesdados,elessãoarmazenadosemuma String[]que
éretornadaparasercolocadana ListView.
@Override
protected String[] doInBackground(String... params) {
184

## Página 187

CasadoCódigo Capítulo6. IntegraçãodeaplicaçõesAndroidcomserviçosREST
try {
String filtro = params[0];
if(TextUtils.isEmpty(filtro)){
return null;
}
String urlTwitter = "http://search.twitter.com/search.json?q=";
String url = Uri.parse(urlTwitter + filtro).toString();
String conteudo = HTTPUtils.acessar(url);
// pegamos o resultado
JSONObject jsonObject = new JSONObject(conteudo);
JSONArray resultados = jsonObject.getJSONArray("results");
// montamos o resultado
String[] tweets = new String[resultados.length()];
for (int i = 0; i < resultados.length(); i++) {
JSONObject tweet = resultados.getJSONObject(i);
String texto = tweet.getString("text");
String usuario = tweet.getString("from_user");
tweets[i] = usuario + " - " + texto;
}
return tweets;
} catch (Exception e) {
throw new RuntimeException(e);
}
}
Parafinalizar,agoraprecisamosiniciaraexecuç ãoda TwitterTaskquandoo
botãobuscarforpressionado,veja:
public void buscar(View v) {
String filtro = texto.getText().toString();
new TwitterTask().execute(filtro);
}
Agoraésóexecutaraaplicaç ãoetestar!Aimagem 6.5mostraosresultadosde
umapesquisapor @android.ParasabermaissobreaAPIdepesquisadoTwitter
185

## Página 188

6.4. Implementeumserviçodebackground CasadoCódigo
visitehttps://dev.twitter.com/docs/using-search.
Figura6.5:PesquisanoTwitter
6.4 Implemente um serviço de background
Aprimeirapartedoaplicativo TwitterSearchestápronta.Oobjetivodestase ção
écriarumserviçode backgroundquefazpesquisasperiódicasnoTwitterembusca
demen çõesaoseuusuário. Quandoumanovamen çãoforencontrada,criaremos
umanotificaçãonabarrade statusdodispositivoparaalertarousuário.
O ServiceéumcomponentedaplataformaAndroidquepodeexecutarta-
refasdelongaduraç ãoemplanodefundoequenãopossuiinterfacegráfica. Ele
podeseriniciadoporqualqueroutrotipodecomponente(uma Activityououtro
Service,porexemplo)epodecontinuaremexecuç ãomesmoqueocomponente
queoiniciousejadestruído. Algunsexemplosdeusode Serviceincluemfazer
downloads,tocarumamúsicaeacessarumserviçoremoto.
Porpadrão,o Serviceéexecutadonomesmoprocessoena threadprinci-
186

## Página 189

CasadoCódigo Capítulo6. IntegraçãodeaplicaçõesAndroidcomserviçosREST
paldaaplicaç ão. Portanto,seelerealizaoperaçõesbloqueantes,odesempenhoda
aplicaçãopodeficarcomprometido,sendonecessáriocriarno Serviceumanova
threadparaexecutaressasoperações.
Um Servicepodeassumirduasformas, startede bound,quetêmrelação
comaformacomoomesmoéiniciado.
Um Serviceé startedquandofoiiniciadoexplicitamenteporalgumou-
tro componente através do métodoContext.startService. Neste caso, o
Serviceéexecutadoemplanodefundoindefinidamentemesmoqueocompo-
nentequeoiniciousejadestruído. Estetipode Serviceégeralmenteutilizado
pararealizaroperaçõesquenãoretornamresultadosparaquemoinvocou.Quando
aoperaçãofinalizar, o Service%devepararasimesmoutilizandoométodo
stopSelf.
Ele é bound quando foi iniciado por um componente através do método
Context.bindService.Estaformade Servicepermiteainteraçãoentrecom-
ponentes,comooenvioderequisiçõeseobten çãoderespostas,numaespéciede
cliente-servidor.Destemodotambémépossívelrealizaracomunicaç ãoentrepro-
cessos(IPC).Várioscomponentespodemfazer bindparaomesmo Serviceque
continuaráexistindoenquantohouverclientes(componentes)conectados.
O ServicemaisadequadoparaanossanecessidadedefazerpesquisasnoTwit-
teremplanodefundoéo startedpois,umaveziniciado,eleseráexecutadoinde-
finidamentealémdenãoretornardadosparaocomponentequeoinvocou.Aideia
équeacadamen çãonoTwitter,o Servicecrienotificaçõesnabarrade statuspara
alertarousuário. Pararealizarmosestaimplementaç ão,criamosumanovaclasse
chamada NotificacaoService,estendendode android.app.Service:
public class NotificacaoService extends Service{
@Override
public IBinder onBind(Intent intent) {
return null;
}
}
Ométodo onBinddeveserimplementado. Essemétodoéinvocadoquando
algumcomponentedesejarealizaro bindcomeste Serviceedeveretornaruma
implementaçãode IBinderqueseráainterfaceutilizadaparaacomunicaç ãoen-
treoscomponentes. Comononossocasonãopermitiremoso bind,poisnosso
Serviceé started,ométodo onBindretorna null. Precisamosentãoso-
187

## Página 190

6.4. Implementeumserviçodebackground CasadoCódigo
brescreverométodo onStartCommandquerespondequandoalgumcomponente
iniciao Serviceatravésdométodo Context.startService:
@Override
public int onStartCommand(Intent intent, int flags, int startId) {
//nossa implementação será feita aqui
return START_STICKY;
}
Ométodo onStartCommandretornaum intqueindicacomooserviçodeve
serreiniciadopeloAndroidquando,poralgummotivo,eleforencerrado.OAndroid
podeencerrar(kill )um Service,casoosistemaestejacomfaltaderecursos,e
recriá-loposteriormente.A flag START_STICKYindicaqueo Servicedeveser
reiniciadoeométodo onStartCommanddeveserinvocadonovamente,mesmo
quenãohajanenhuma Intentpendentedeprocessamento.
Existem outras flags como a START_NOT_STICKY, que indica que
o Service só deve ser reiniciado se houver Intents pendentes, e a
START_REDELIVER_INTENT para que o Service seja reiniciado com a úl-
tima Intentenviada.
Nométodo onStartCommanddevemoscriarumanova threadparareali-
zaraconsultapormen çõesnoTwitterefazercomqueelasejaexecutadaperiodi-
camente,de10em10minutos,porexemplo. Parafazeristo,utilizaremosaclasse
ScheduledThreadPoolExecutorquepermitequeumainstânciade Runnable
sejaexecutadadetemposemtemposapenasconfigurandoasuaexecuç ão,utilizando
ométodo scheduleAtFixedRate.
Então,instanciaremosumnovo ScheduledThreadPoolExecutorpassando
noseuconstrutoraquantidadede threadsquedevemsermantidasno pool.No
nossocaso,apenasuma threadbasta.Naslinhasseguintesdefinimosqualseráo
atraso(delay)inicialparaoiníciodaexecuç ão, 0indicaqueaexecuç ãodeveiniciar
imediatamente.
Emseguidadefinimosoperíododetempoparaqueaoperaç ãosejarealizada.
Escolhemosquea threaddeveserexecutadade10em10minutos. Obviamente
queemcenáriosmaisreaisprovavelmenteestevalorseráconfiguradopelousuário
elidodas SharedPreferences.Eporfim,fazemosoagendamentodaexecuç ão
da NotificacaoTaskqueéumaclasseprivadaquedefiniremosaseguir.
@Override
public int onStartCommand(Intent intent, int flags, int startId) {
188

## Página 191

CasadoCódigo Capítulo6. IntegraçãodeaplicaçõesAndroidcomserviçosREST
ScheduledThreadPoolExecutor pool =
new ScheduledThreadPoolExecutor(1);
long delayInicial = 0;
long periodo = 10;
TimeUnit unit = TimeUnit.MINUTES;
pool.scheduleAtFixedRate(new NotificacaoTask(),
delayInicial, periodo,unit);
return START_STICKY;
}
Agoraprecisamosimplementara NotificacaoTask,queseráresponsávelpor
realizaratarefa.Elaimplementaráainterface Runnable,oquetornapossívelque
elasejaexecutadapelo ScheduledThreadPoolExecutor.
Aimplementaçãodométodo runébastanteparecidacomaquejárealizamos
parabuscarosresultadosnoTwitter,apartirdostermosinformadospelousuário.
Vamosentãoàsdiferen ças.Definimosumavariávelcomostermosquedevemser
utilizadosnaprimeiravezqueapesquisaforrealizada.IncluaoseuusuáriodoTwit-
terláedepois,acrescentamosummétodoqueverificaseháconectividadeparadar
prosseguimentoàexecuçãodométodo,chamado estaConectado,queimplemen-
taremosemseguida.
private class NotificacaoTask implements Runnable {
private String baseUrl = "http://search.twitter.com/search.json";
private String refreshUrl = "?q=<seu_usuario_no_twitter>";
@Override
public void run() {
if (!estaConectado()) {
return;
}
try {
String json = HTTPUtils.acessar(baseUrl + refreshUrl);
JSONObject jsonObject = new JSONObject(json);
refreshUrl = jsonObject.getString("refresh_url");
JSONArray resultados = jsonObject.getJSONArray("results");
for (int i = 0; i < resultados.length(); i++) {
JSONObject tweet = resultados.getJSONObject(i);
189

## Página 192

6.4. Implementeumserviçodebackground CasadoCódigo
String texto = tweet.getString("text");
String usuario = tweet.getString("from_user");
criarNotificacao(usuario, texto, i);
}
} catch (Exception e) {}
}
}
Quandoumapesquisaérealizada,oTwitterretornaumaURLdeatualizaç ão,
contendoapesquisaoriginaleumparâmetro since_idqueindicaqualfoio
últimoresultadoretornado. Entãona NotificacaoTaskatualizamosavariável
refreshUrlpararealizarasconsultasposteriores,obtendoapenasasnovasmen-
ções.Osresultadosobtidossãopercorridoseparacadaumdelesécriadaumanova
notificação.Veremoscomofazerissonase çãoseguinte.
Agoraprecisamosimplementarométodo estaConectado,queatravésdo
ConnectivityManagerpoderáobterinformaçõesvariadassobreoestadodasco-
nexões,sejamelasWI-FI,3Getc. Nonossocaso,recuperamosasinformaçõesda
conexãoativaenalinhaseguinteretornamosovalorqueindicaseodispositivoestá
ounãoconectadoaumaredededados.
public class NotificacaoService extends Service {
//demais códigos existentes
private boolean estaConectado() {
ConnectivityManager manager =
(ConnectivityManager) getSystemService(
Context.CONNECTIVITY_SERVICE);
NetworkInfo info = manager.getActiveNetworkInfo();
return info.isConnected();
}
}
Agora, para ficar completo, precisamos implementar o método
criarNotificacao.
190

## Página 193

CasadoCódigo Capítulo6. IntegraçãodeaplicaçõesAndroidcomserviçosREST
6.5 Crie notificações na barra de status
AbarradestatusdoAndroidéolocalondeasnotificaçõessãoexibidas.Essasnoti-
ficaçõespodemserdoprópriosistema,comoporexemploumavisosobreodescar-
regamentodabateria,oupodemtersidocriadasporqualqueraplicativo.
A figura6.6 mostra como deve ficar as notificações do nosso aplicativo
TwitterSearchnabarrade status.Quandoousuárioselecionaralgumadasno-
tificações,devemosmostraro tweetemumanova activitydanossaaplicaç ão. A
imagem6.7mostraumavisualizaç ãosimplesdo tweet.
Figura6.6:Notificaçõesnabarradestatus
191

## Página 194

6.5. Crienotificaçõesnabarradestatus CasadoCódigo
Figura6.7:Notificaçõesnabarradestatus
Para construir as notificações, implementamos na classe
NotificacaoService o método criarNotificacao. Este método re-
cebecomoparâmetrootextodo tweeteousuárioqueorealizou, alémdeum
identificadorparaanotificaç ão.
Ométodovaireceberousuário,otextoeoiddotweet:
private void criarNotificacao(String usuario, String texto, int id) { }
Definimosqualseráoíconedanotificaç ão,recuperamosdo strings.xmlo
textoqueiráaparecernabarrade status,obtemosum longquerepresentaadata
danotificaçãoalémdeconstruirotítulodanotificaç ãoqueseráalgocomo“alguém
mencionouvocê”.Emseguida,criamosumaIntentqueseráutilizadaparainiciar
uma activityqueexibiráosdadosdo tweet,incluídoscomoextrasda Intent.
192

## Página 195

CasadoCódigo Capítulo6. IntegraçãodeaplicaçõesAndroidcomserviçosREST
Utilizaremosa PendingIntentparainiciara TweetActivityquandoo
usuárioselecionarumanotificação.Basicamentea PendingIntentpermiteque
outrocomponenteexecuteaaç ãodefinidaanteriormentepela Intentcomosefosse
aprópriaaplicaç ãoqueacriou.Utilizaremosesterecursoparavincularcadanotifi-
caçãoauma Intentqueexibeosdadosdo tweet.
private void criarNotificacao(String usuario, String texto, int id) {
int icone = R.drawable.ic_launcher;
String aviso = getString(R.string.aviso);
long data = System.currentTimeMillis();
String titulo = usuario + " " + getString(R.string.titulo);
Context context = getApplicationContext();
Intent intent = new Intent(context, TweetActivity.class);
intent.putExtra(TweetActivity.USUARIO, usuario.toString());
intent.putExtra(TweetActivity.TEXTO, texto.toString());
PendingIntent pendingIntent =
PendingIntent.getActivity(context, id, intent,
Intent.FLAG_ACTIVITY_NEW_TASK);
}
Criamosuma PendingIntent,recebendocomoparâmetroocontexto,um
identificadorparaarequisiç ão(atualmentenãoutilizadopeloAndroid),a Intent
desejadaeuma flagdeinicialização.
Agora,vamoscriarumanovanotificaç ãocomoícone,otextodeavisoeadata
previamentedefinidos.Utilizaremosa flag FLAG_AUTO_CANCELparaindicarque,
aoserselecionadaestanotificaç ão,iremossairdalistadenotificações. Adicional-
menteconfiguramosparaqueanotificaç ãoprovoqueavibraç ãododispositivo,to-
queosompadrãoeaindaativeailuminaç ãodeaviso.
Vamosusarométodo setLatestEventInfoparaincluirasinformaçõesda
notificaçãoquesãoousuárioetextodo tweetea PendingIntentqueseráexecu-
tada. Agoraqueanotificaçãoestápronta,utilizamoso NotificationManager
paraefetivamenteacolocarnabarrade status.
private void criarNotificacao(String usuario, String texto, int id) {
// Recupera as informações e cria a PendingIntent
Notification notification = new Notification(icone, aviso, data);
193

## Página 196

6.5. Crienotificaçõesnabarradestatus CasadoCódigo
notification.flags = Notification.FLAG_AUTO_CANCEL;
notification.flags = Notification.FLAG_AUTO_CANCEL;
notification.defaults |= Notification.DEFAULT_VIBRATE;
notification.defaults |= Notification.DEFAULT_LIGHTS;
notification.defaults |= Notification.DEFAULT_SOUND;
notification.setLatestEventInfo(context, titulo,
texto, pendingIntent);
String ns = Context.NOTIFICATION_SERVICE;
NotificationManager notificationManager =
(NotificationManager) getSystemService(ns);
notificationManager.notify(id, notification);
}
Precisamoscolocartambémasmensagensno strings.xml.
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="app_name">TwitterSearch</string>
<string name="buscar">Buscar</string>
<string name="aviso">Você foi mencionado!</string>
<string name="titulo">mencionou você</string>
</resources>
A activitycriadaparaaexibiç ãodos tweetsébastantesimplesenãopossuinada
dediferentedoquejáfoiapresentadonodecorrernolivro. Confiraoarquivode
layout tweet.xml:
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
android:layout_width="fill_parent"
android:layout_height="fill_parent"
android:orientation="vertical" >
<TextView
android:id="@+id/usuario"
android:layout_width="wrap_content"
android:layout_height="wrap_content" />
<TextView
android:id="@+id/texto"
android:layout_width="wrap_content"
194

## Página 197

CasadoCódigo Capítulo6. IntegraçãodeaplicaçõesAndroidcomserviçosREST
android:layout_height="wrap_content" />
</LinearLayout>
Eaclasse TweetActivity:
public class TweetActivity extends Activity {
public static final String TEXTO = "texto";
public static final String USUARIO = "usuario";
@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.tweet);
TextView usuarioTextView =
(TextView) findViewById(R.id.usuario);
TextView textoTextView = (TextView) findViewById(R.id.texto);
String usuario = getIntent().getStringExtra(USUARIO);
String texto = getIntent().getStringExtra(TEXTO);
usuarioTextView.setText(usuario);
textoTextView.setText(texto);
}
}
Parafinalizaraimplementaç ãodo Serviceedasnotificações,énecessáriode-
clararo Serviceno AndroidManifest.xml,assimcomoa TweetActivity.
Tambéméprecisoinserirumapermissãoreferenteaoacessoàsinformaçõesderede
eoutraparaativaravibraç ãododispositivo.Vejacomoficou:
<!-- permissões necessárias -->
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission
android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.VIBRATE"/>
<application
android:icon="@drawable/ic_launcher"
android:label="@string/app_name">
<!-- declarações existentes -->
195

## Página 198

6.6. UtilizeumBroadcastReceiverparainiciaroService CasadoCódigo
<service android:name=".NotificacaoService" />
<activity android:name=".TweetActivity" />
</application>
Ainda não é possível ver o serviço implementado executando pois
em nenhum momento fizemos a sua inicialização chamando o método
Context.startService. A ideia é que isto não seja feito pelo usuário e
simpelopróprioAndroidquandoodispositivofoiiniciado.
6.6 U tilize um Broadcast Receiver para iniciar o
Service
Aúltimapartedanossaaplicaç ãoqueutilizaotwitter,consisteemimplementarum
outrotipodecomponentedoAndroid,chamadode Broadcast Receiver.Estecompo-
nentepoderesponderaeventospropagados(broadcasts)pelosistemaetambémpor
outrosaplicativos.Assimcomoocomponente Service,o BroadcastReceiver
tambémnãopossuiinterfacegráficaegeralmenteinteragecomousuárioatravésde
notificações.
Faremos uma implementaç ão que representa bem o papel do
BroadcastReceiver, que é receber um evento e processá-lo, geralmente
delegandoaexecuç ãoparaoutrocomponente.
Crie uma nova classe com nome deStartupReceiver, estendendo de
BroadcastReceiver.Temosqueimplementarapenasométodo onReceiveque
recebecomoparâmetroocontextoeoeventoquenaverdadeéuma Intent,algo
quejáconhecemosbem.Nessemétodoiniciaremoso NotificacaoService.O
códigoaseguirdemostraaimplementaç ãodo StartupReceiver.
public class StartupReceiver extends BroadcastReceiver{
@Override
public void onReceive(Context context, Intent intent) {
Intent it = new Intent(context, NotificacaoService.class);
context.startService(it);
}
}
No nosso caso, o evento que queremos capturar é o
android.intent.action.BOOT_COMPLETED que indica que o dispositivo
foi inicializado. Como os eventos na verdade sãoIntents fica fácil ima-
ginar que precisaremos incluir umintent filter para capturá-los. No
196

## Página 199

CasadoCódigo Capítulo6. IntegraçãodeaplicaçõesAndroidcomserviçosREST
AndroidManifest.xmlfaremosadeclaraç ãodo BroadcastReceiveredo
filtro necessário, além, é claro, de uma permissão para receber o evento, dessa
forma:
<!-- permissões já existentes -->
<uses-permission
android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
<application
android:icon="@drawable/ic_launcher"
android:label="@string/app_name">
<!-- declarações existentes -->
<receiver android:name=".StartupReceiver" >
<intent-filter>
<action
android:name="android.intent.action.BOOT_COMPLETED" />
</intent-filter>
</receiver>
</application>
Agoraaaplicação TwitterSearchestápronta!Execute-anormalmente.
Naprimeiraexecuç ão,oADTiráinstalaroaplicativo,noentanto,oeventode
bootjáfoidisparadoeentãooaplicativonãoiráiniciaro Service.Fecheoemula-
doreoinicienovamente,masdestavezpeloAVDManager(menu Window-> AVD
Manager,op ção start). Agoraoserviçodeveseriniciado,eparatestarbasta
tuitaralgocomostermosquevocêespecificou.
Verificando serviços em execução
No Android é possível verificar quais aplicativos e serviços es-
tão sendo executados através do menuConfigurações, opção
Aplicativos,aba Em execução.
6.7 Conclusão
AcabamosdeaprenderumpoucodosserviçosRESTqueutilizamoformatoJSON
paratransmitirdados.ExperimentamosaGoogleBooksAPIquedisponibilizain-
formaçõessobrelivrosatravésdeumserviçoRESTeimplementamosumaaplicaç ão
197

## Página 200

6.7. Conclusão CasadoCódigo
deexemploquerealizabuscasnoTwitterefaznotificaçõesquandoalguémnosmen-
cionaemalgum tweet.
Paraasimplementações,utilizamos AsyncTaskeoscomponentes Service
e BroadcastReceiverdaplataformaAndroid,alémdeagendaraexecuç ãode
threadcomo ScheduledThreadPoolExecutor.Todosestesitenssãofrequen-
tementeutilizadosquandotrabalhamoscomserviçosremotos.
VocêpodeaprendermuitomaissobreRESTatravésdelivrosespecíficos,comoo
RESTfulWebservices,doLeonardRichardsoneSamRuby,ouentão,atravésdobom
materialdisponibilizadopelaIBM,emseublogdedesenvolvedores: http://www.
ibm.com/developerworks/webservices/library/ws-restful.
198

## Página 201

Capítulo7
UtilizeGoogleAPIsecrie
funcionalidadesinteressantes
Nocapítulo6,fizemosaintegraç ãocomotwitterecriamosumaaplicaç ãoquenotifi-
cavaousuárioacadanovo tweetquesurgissesobreumdeterminadoassunto.Mase
sequisermoscolocaremnossaaplicaç ãoumserviçodecalendário,parapodermos
guardaremnossasagendasasviagensqueteremosquefazer? Comopoderíamos
implementaressafuncionalidade?
OGoogledisponibilizadiversosserviçosrelacionadosaosseusprodutosquepo-
demserutilizadosgratuitamentepornós,desenvolvedores.Essesserviçostambém
sãoconhecidoscomoGoogleAPIs.AlgunsexemplossãoaPlacesAPIquepermite
obterinformaçõessobredeterminadalocalidade,aTasksAPIquepermiteinterações
comoGoogleTasks,aGoogleMapsAPIalémdaDriveAPIparaintegraç ãocomo
GoogleDrive.
Deformageral,estesserviçospodemseracessadosdiretamenteviaHTTP,sendo
responsabilidadedoaplicativoclienterealizarosprocedimentosdeautenticaç ão,

## Página 202

7.1. Instaleoadd-onGoogleAPIs CasadoCódigo
executararequisiçãoeprocessararespostadoserviço.NoentantooGoogledisponi-
bilizaumasériedebibliotecas,emdiversaslinguagensdeprogramaç ão,conhecidas
como Google APIs Client Libraries,quefacilitamousodessesserviços.
NestecapítuloveremoscomoutilizarumacontadoGoogleparaautenticarum
usuárioeincluiremosessafuncionalidadenologindonossoaplicativoBoaViagem.
Alémdisso,faremosumaintegraç ãodoaplicativocomaagendadousuárionoGo-
ogleCalendar.Assimqueelecriarumanovaviagem,registraremosemsuaagenda
umnovoeventocompreendendoasdatasdaviagemusandoaCalendarAPI.Para
realizaressasimplementaçõessãonecessáriosalgunsprocedimentosdepreparaç ão,
queveremosnasse çõesseguintes.
Não conhece o GoogleCalendar?
OGoogleCalendar,ouGoogleAgendacomoéchamadonoBrasil,
éumserviçogratuito,cominterfaceweb,noqualépossívelregistrare
controlareventosecompromissosalémdepodercompartilhá-loscom
outraspessoas.ParautilizaroserviçoénecessárioumacontadoGoogle.
Conheçaoserviçoem http://www.google.com/calendar
7.1 Instale o add-on GoogleAPIs
Oadd-onGoogleAPIséumaextensãodoAndroidSDKquedisponibilizaessenci-
almenteumaAPIexternaparatrabalharcommapasalémdeoutroscomponentes
eserviçosdoGooglequerodamnoAndroid.Nonossocaso,estamosinteressados
noserviçodecontasdeusuárioqueutilizaremosparaautenticaç ão. Éimportante
ressaltarqueeste add-onnadatemavercomosdiversosserviçosdisponibilizados
peloGoogle,taiscomoaGoogle+API,CalendarAPIeCustomSearchAPI,eassuas
respectivasbibliotecasdeacesso.
Pararealizarodownload, acesseoAndroidSDKManageratravésdomenu
Window -> Android SDK Manager doEclipse,selecioneeinstaleo add-onGo-
ogleAPIsdaversão2.3.3queestamosutilizando,conformedemonstraaimagem
7.1
200

## Página 203

CasadoCódigo Capítulo7. UtilizeGoogleAPIsecriefuncionalidadesinteressantes
Figura7.1:DownloaddopacoteGoogleAPIs
Depoisqueopacoteforinstalado,vamoscriarumnovoAVDcompatívelcom
aGoogleAPIs.Acesseomenu Window -> AVD Manager doEclipse,eselecione
aop ção New...najanelaqueirásurgir.Aimagem 7.2mostracomoconfiguraro
novoAVD.
201

## Página 204

7.2. Adicionebibliotecasauxiliares CasadoCódigo
Figura7.2:AVDcomGoogleAPIs
ParautilizaroserviçodoGoogleCalendar,énecessárioqueousuáriopossua
umacontadoGoogle. Estacontatambémprecisaestarregistradanodispositivo
paraquepossamosutilizá-la,tantoparaautenticarousuáriocomoparasolicitar
acessoàsuaagenda.
InicieonovoAVDcriadocomo add-onGoogleAPIs.Comoemuladorjáini-
ciado,acesseomenudodispositivoeselecione Configuraçõeseemseguidaa
opção Contas e Sincronização.Escolha Adicionar nova conta esigaas
instruções.VocêpodeutilizarasuaprópriacontadoGoogleoucriarumaespecifi-
camenteparatestes.
7.2 Adicione bibliotecas auxiliares
OGoogle,alémdedisponibilizarAPIsparaacessarremotamenteosseusserviços,
tambémdisponibilizaumconjuntodebibliotecasparaacessá-losemdiversaslin-
guagensdeprogramaç ãodiferentes. Utilizaremosalgumasdelasparanosajudar
naautenticaçãodousuárioenaintegraç ãocomoGoogleCalendar. Acesseosite
http://code.google.com/p/google-api-java-client/wiki/APIs#Calendar_APIefaçao
downloaddaúltimaversãodabibliotecaCalendarAPI.
Aofazerodownloadedescompactaroarquivo,alémdaprópriaCalendarAPI,
tambémteremosassuasdependências,localizadasnapasta dependencies.Para
202

## Página 205

CasadoCódigo Capítulo7. UtilizeGoogleAPIsecriefuncionalidadesinteressantes
utilizaraCalendarAPInoAndroidprecisamosadicionarosseguintesarquivos jar
aonossoprojeto:
• google-api-calendar-v3-rev7-java-1.6.0-beta.jar
• google-api-client-1.X.X-beta.jar
• google-api-client-android2-1.X.X-beta.jar
• google-oauth-client-1.X.X-beta.jar
• google-http-client-1.X.X-beta.jar
• google-http-client-android2-1.X.X-beta.jar
• gson-2.X.jar
• guava-11.X.X.jar
• jackson-core-asl-1.X.X.jar
• jsr305-1.3.9.jar
• protobuf-java-2.X.X.jar
NoEclipse,crieumanovapastanoprojetocomonomede libsecopiepara
láosarquivoslistadosacima.Éessencialqueonomesejaeste,poiséláqueoplugin
ADTiráprocurarasbibliotecasutilizadaspeloaplicativo. Aestruturadoprojeto
ficaráconformedemostraaimagem 7.3.
203

## Página 206

7.3. Adicioneaspermissõesnecessárias CasadoCódigo
Figura7.3:Pastalibdoprojeto
7.3 Adicione as permissões necessárias
Énecessárioadicionaralgumaspermissõesno AndroidManifest.xmlparaque
possamosacessaraInterneterecuperarascontasarmazenadasnodispositivo. As
permissõesnecessáriassãoasseguintes:
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.USE_CREDENTIALS" />
<uses-permission android:name="android.permission.GET_ACCOUNTS" />
<uses-permission android:name="android.permission.MANAGE_ACCOUNTS" />
7.4 Registre a aplicação no Google
Alémdasbibliotecasauxiliares,pararealizaraintegraç ãocomoGoogleCalendar
precisaremosdemaisduascoisas. Aprimeiraéobterumachave(API key)para
identificaronossoaplicativojuntoaoGoogle.
Tambémprecisaremoscriarum client ID,queseráutilizadoparaqueousuário
autorizeoacessoaosdadosdasuaagenda.Estaautorizaç ãoserárealizadaatravésdo
204

## Página 207

CasadoCódigo Capítulo7. UtilizeGoogleAPIsecriefuncionalidadesinteressantes
protocoloOAuth2.0,umprotocoloparaautorizaç ãoeautenticaç ão,utilizadopor
diversosserviçosconhecidos,comooTwittereFacebook.
Oregistrodaaplicaç ãoparaaobten çãodaschaveséfeitoatravésdoGoogle
Console.ÉnecessáriopossuirumacontadoGooglepararealizaresteprocedimento.
Faremosistoagora.
Acesse o sitehttps://code.google.com/apis/console/ e clique em Create
Project.
Figura7.4:GoogleConsole
Natelaseguinte,ativeaCalendarAPIclicandonobotão offdacoluna Status.
205

## Página 208

7.4. RegistreaaplicaçãonoGoogle CasadoCódigo
Figura7.5:Ativandooserviço
Nomenulocalizadodoladoesquerdo,selecioneaop ção API Access.Naparte
inferiordapáginaapresentadaestálistadaaAPI keyqueutilizaremosparaidentificar
nossoaplicativonoGoogle.Aimagem 7.6destacaaAPI key.
206

## Página 209

CasadoCódigo Capítulo7. UtilizeGoogleAPIsecriefuncionalidadesinteressantes
Figura7.6:APIKey
Nestamesmapáginatambémteremosumaop çãoparacriaruma“OAuth2.0
clientID”.Aoselecionarestaopção,seránecessárioinformaronomedoaplicativo
queseráapresentadoaousuárioquandoforsolicitadaautorizaç ãoparaacessarseus
dadosdaagenda.Opcionalmente,podemosinformaraURLdalogodoproduto.
Aoselecionaraop ção Next,devemosinformarotipodaaplicaç ão.Nonosso
caso,aop çãoadequadaéa Installed Application poisanossaaplicaç ãoserá
instaladaemumdispositivo.Asimagensaseguirdemonstramessespassos.
207

## Página 210

7.4. RegistreaaplicaçãonoGoogle CasadoCódigo
Figura7.7:CriandoclientID
208

## Página 211

CasadoCódigo Capítulo7. UtilizeGoogleAPIsecriefuncionalidadesinteressantes
Figura7.8:CriandoclientID
Epronto,vocêjáregistrousuaaplicaçãonoGoogle!
7.5 Autentique o usuário com a conta do Google
Comoambientepreparado,agorapodemosiniciaraimplementaç ãodasnovasfun-
cionalidades! Iniciaremosrealizandoaautenticaç ãodousuáriocombasenasua
contadoGoogle,registradanodispositivo.Estaabordageméinteressante,poisevita
quenossoaplicativotenhaquemanterumabaseprópriadeusuáriosalémdetrazer
comodidadeaelesjáquepodemutilizarosseus loginsesenhasjáexistentes.
Naclasse BoaViagemActivityvamossubstituiraautenticaç ãoexistenteein-
cluirestanovaimplementaç ão. Aideiaéqueousuárioforne çao loginesenhade
suacontaGoogle.Apartirdessasinformações,utilizaremoso AccountManager
doAndroidesolicitaremosparaqueascredenciaissejamconfirmadas.
O AccountManagersuportaváriostiposdeconta,comocontasdoFacebook
eMicrosoftExchange.NomomentonosinteressaapenasascontasdotipoGoogle
209

## Página 212

7.5. AutentiqueousuáriocomacontadoGoogle CasadoCódigo
porissoutilizaremosaclasse GoogleAccountManagerquejátrazfacilidadespara
lidarcomestetipodeconta.
No método onCreate da BoaViagemActivity, vamos instanciar o
GoogleAccountManager,passandoocontextocomoparâmetro. Tambémrea-
lizamosalgumasalteraçõesnométodo onCreate,parautilizarumarquivodepre-
ferênciasglobalparaoaplicativoemovemosaconstante MANTER_CONECTADOpara
aclassedeconstantes.
Incluímosumnovométodo iniciarDashboardqueseráutilizadotambém
emoutraspartesdocódigo:
import static br.com.casadocodigo.boaviagem.Constantes.*
// novos atributos
private SharedPreferences preferencias;
private GoogleAccountManager accountManager;
private Account conta;
@Override
public void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.login);
accountManager = new GoogleAccountManager(this );
usuario = ( EditText) findViewById(R.id.usuario);
senha = (EditText) findViewById(R.id.senha);
manterConectado = (CheckBox) findViewById(R.id.manterConectado);
preferencias = getSharedPreferences(PREFERENCIAS, MODE_PRIVATE);
boolean conectado = preferencias
.getBoolean(MANTER_CONECTADO, false);
if(conectado){
iniciarDashboard();
}
}
private void iniciarDashboard(){
startActivity(new Intent(this, DashboardActivity.class));
}
210

## Página 213

CasadoCódigo Capítulo7. UtilizeGoogleAPIsecriefuncionalidadesinteressantes
public class Constantes {
// novas constantes
public static final String PREFERENCIAS = "preferencias_globais";
public static final String MANTER_CONECTADO = "manter_conectado";
}
Vamosalteraraimplementaçãodométodo entrarOnClick,queagorapassará
ainvocarométodo autenticar.
public void entrarOnClick(View v){
String usuarioInformado = usuario.getText().toString();
String senhaInformada = senha.getText().toString();
autenticar(usuarioInformado, senhaInformada);
}
Nométodo autenticar,casonãosejapossívellocalizaraconta,emitimos
umamensagemdeavisoparaousuário. Pararealizaraautenticaç ãoconstruímos
um Bundle,informandoascredenciaisdousuárioesolicitamossuaverificaç ão
invocandoométodo confirmCredentialsdo AccountManager.
private void autenticar(final String nomeConta, String senha) {
conta = accountManager.getAccountByName(nomeConta);
if(conta == null){
Toast.makeText(this, R.string.conta_inexistente,
Toast.LENGTH_LONG).show();
return;
}
Bundle bundle = new Bundle();
bundle.putString(AccountManager.KEY_ACCOUNT_NAME, nomeConta);
bundle.putString(AccountManager.KEY_PASSWORD, senha);
accountManager.getAccountManager()
.confirmCredentials(conta , bundle, this,
new AutenticacaoCallback(), null);
}
Comoparâmetroparaométodo confirmCredentialsprecisamospassara
211

## Página 214

7.5. AutentiqueousuáriocomacontadoGoogle CasadoCódigo
conta,o bundlecomascredenciais,ocontextoeum callbackqueseráinvocado
quandoaoperaç ãoforrealizada,alémdeum handler(nulononossoexemplo).
Ométodo confirmCredentialsnãoretornanadadeimediato,eleseráexe-
cutadodeformaassíncronaequandoaoperaç ãosolicitadafinalizar,o callback
seráinvocado.Éláqueverificaremosseaautenticaç ãoocorreucomsucesso.
Optamosporimplementareste callbackcomoumaclasseprivada,etemos
queimplementarainterface AccountManagerCallback:
private class AutenticacaoCallback
implements AccountManagerCallback<Bundle> {
@Override
public void run(AccountManagerFuture<Bundle> future) { }
}
Emseguida,obtemoso bundlequecontémosresultadosdaoperaç ãodecon-
firmaçãodecredenciais.
private class AutenticacaoCallback
implements AccountManagerCallback<Bundle> {
@Override
public void run(AccountManagerFuture<Bundle> future) {
try {
Bundle bundle = future.getResult();
} catch (OperationCanceledException e) {
// usuário cancelou a operação
} catch (AuthenticatorException e) {
// possível falha no autenticador
} catch (IOException e) {
// possível falha de comunicação
}
}
}
Emseguida,verificamosseaoperaç ãofoirealizadacomsucesso,ouseja,seo
loginesenhaforaminformadoscorretamente,avaliandoseoconteúdoarmazenado
212

## Página 215

CasadoCódigo Capítulo7. UtilizeGoogleAPIsecriefuncionalidadesinteressantes
nachave KEY_BOOLEAN_RESULTéverdadeiro.Emcasodefalha,alertamosousuá-
rio,casocontrário,adashboarddoaplicativoéiniciada.
private class AutenticacaoCallback
implements AccountManagerCallback<Bundle> {
@Override
public void run(AccountManagerFuture<Bundle> future) {
try {
Bundle bundle = future.getResult();
if(bundle.getBoolean(AccountManager.KEY_BOOLEAN_RESULT)) {
iniciarDashboard();
} else {
Toast.makeText(getBaseContext(),
getString(R.string.erro_autenticacao),
Toast.LENGTH_LONG).show();
}
} catch (OperationCanceledException e) {
//usuário cancelou a operação
} catch (AuthenticatorException e) {
//possível falha no autenticador
} catch (IOException e) {
//possível falha de comunicação
}
}
}
Pronto!Executeaaplicaç ãoeautentique-secomamesmacontaadicionadaao
dispositivo!
7.6 Solicite autorização para o GoogleCalendar
Pararealizaraintegraç ão,vamosprecisardeumaautorizaç ãoconcedidapelousuá-
rio,paraqueonossoaplicativopossaacessarseusdadosdaagenda.
EstaautorizaçãoseráfeitautilizandooprotocoloOAuth2.0quetemsidoam-
plamenteutilizadoporserviçosnawebequeestabeleceumaformasimplesesegura
213

## Página 216

7.6. SoliciteautorizaçãoparaoGoogleCalendar CasadoCódigo
deautorizaroacessoaumdadorecursoporumdeterminadoaplicativo,nãosendo
necessárioqueeletenhaacessoàscredenciaisdousuário.
Basicamente,ospassosrealizadosparaumaautorizaç ãoviaOAuth2.0sãoos
seguintes:
1) Oaplicativorequeraoserviçodesejadoautorizaç ãoparaacessardeterminado
recurso;
2) Oserviçosolicitaoconsentimentodousuário;
3) Seautorizado,oserviçoforneceum tokendeacessoparaoaplicativo;
4) Oaplicativoutilizaeste tokenpararealizarasrequisições.
O client IDquecriamosanteriormenteseráutilizadonospassos1e2paraiden-
tificaronossoaplicativo.Comoestamosutilizandoasbibliotecasauxiliaresdisponi-
bilizadaspeloGoogle,nãoprecisaremosimplementartodoesseprocedimento.No
aplicativoBoaViagem,aproveitaremosomomentodo loginparasolicitaraautoriza-
çãonecessáriaparaacessaraagendadousuário.
Quandofazemosopedidodeacesso, precisamosinformarqualéorecurso
desejado. NoâmbitodoOAuth,oquedesejamosacessaréconhecidocomo“es-
copo”,quenonossocasoéoGoogleCalendar,identificadocomo oauth2:https:
//www.googleapis.com/auth/calendar.
Precisaremosinformaresteescopoquandofizermosasolicitaç ãodeum token
deacesso.Vamosincluirestevalornaclasse Constantes.Aproveitetambémpara
incluirmaisduasconstantesquesereferemàsuaAPI keyeaonomedaaplicaç ão
utilizadonoregistrodoGoogleConsole.Vejaaseguiradefiniç ãodasnovascons-
tantes:
public class Constantes {
// novas constantes
public static final String TOKEN_ACESSO = "token_acesso";
public static final String NOME_CONTA = "nome_conta";
public static final String APP_NAME = "BoaViagem";
public static final String AUTH_TOKEN_TYPE =
"oauth2:https://www.googleapis.com/auth/calendar";
public static final String API_KEY =
"sua_api_key_obtida_no_google_console";
// constantes existentes
}
214

## Página 217

CasadoCódigo Capítulo7. UtilizeGoogleAPIsecriefuncionalidadesinteressantes
Assim como fizemos na autenticação, criaremos um novo método e
um callback para tratar da autorização. Novamente utilizaremos o
AccountManager, invocando o seu métodogetAuthToken para recuperar
um tokendeacesso. Comoparâmetroinformaremosacontaeoescopo,alémda
activityedo callbackqueseráinvocadoquandoaoperaç ãoterminar. Opcio-
nalmentepodemosinformartambémum bundleeum handler. Ométodo
solicitarAutorizacaoteráoseguintecódigo:
private void solicitarAutorizacao() {
accountManager.getAccountManager()
.getAuthToken(conta,
Constantes.AUTH_TOKEN_TYPE,
null,
this,
new AutorizacaoCallback(),
null);
}
O AutorizacaoCallbackseráutilizadoparatratararespostadopedidode
autorização. Oqueprecisaremosfazerérecuperaro tokendeacessoeonomeda
contaegravaressasinformaçõesnaspreferênciasdoaplicativoparautilizarmospos-
teriormente.
private class AutorizacaoCallback
implements AccountManagerCallback<Bundle> {
@Override
public void run(AccountManagerFuture<Bundle> future) {
try {
Bundle bundle = future.getResult();
String nomeConta =
bundle.getString(AccountManager.KEY_ACCOUNT_NAME);
String tokenAcesso =
bundle.getString(AccountManager.KEY_AUTHTOKEN);
} catch (OperationCanceledException e) {
// usuário cancelou a operação
} catch (AuthenticatorException e) {
// possível problema no autenticador
215

## Página 218

7.6. SoliciteautorizaçãoparaoGoogleCalendar CasadoCódigo
} catch (IOException e) {
// possível problema de comunicação
}
}
}
Emseguidagravamosessasinformaçõesnaspreferênciaseiniciamosa Dashbo-
arddoaplicativo.
private class AutorizacaoCallback
implements AccountManagerCallback<Bundle> {
@Override
public void run(AccountManagerFuture<Bundle> future) {
try {
Bundle bundle = future.getResult();
String nomeConta =
bundle.getString(AccountManager.KEY_ACCOUNT_NAME);
String tokenAcesso =
bundle.getString(AccountManager.KEY_AUTHTOKEN);
gravarTokenAcesso(nomeConta, tokenAcesso);
iniciarDashboard();
} catch (OperationCanceledException e) {
// usuário cancelou a operação
} catch (AuthenticatorException e) {
// possível falha no autenticador
} catch (IOException e) {
// possível falha de comunicação
}
}
}
private void gravarTokenAcesso(String nomeConta, String tokenAcesso) {
Editor editor = preferencias.edit();
editor.putString(NOME_CONTA, nomeConta);
editor.putString(TOKEN_ACESSO, tokenAcesso);
editor.commit();
}
216

## Página 219

CasadoCódigo Capítulo7. UtilizeGoogleAPIsecriefuncionalidadesinteressantes
No AutenticacaoCallback,quandoaautenticaç ãoérealizadacomsucesso,
emvezdeiniciara Dashboard,invocamosométodo solicitarAutorizacao.
private class AutenticacaoCallback
implements AccountManagerCallback<Bundle> {
@Override
public void run(AccountManagerFuture<Bundle> future) {
try {
Bundle bundle = future.getResult();
if(bundle.getBoolean(AccountManager.KEY_BOOLEAN_RESULT)) {
solicitarAutorizacao();
} else {
Toast.makeText(getBaseContext(),
getString(R.string.erro_autenticacao),
Toast.LENGTH_LONG).show();
}
} catch (OperationCanceledException e) {
// usuário cancelou a operação
} catch (AuthenticatorException e) {
// possível problema no autenticador
} catch (IOException e) {
// possível problema de comunicação
}
}
}
Comessasimplementaçõesfinalizamosapartedeautorizaç ãoparautilizaro
GoogleCalendar!Agoraquandovocêseautenticarnoaplicativo,seráperguntadose
autorizaoacessoaosseusdadosdaagenda,comomostraafigura 7.9.Experimente!
217

## Página 220

7.7. Trateaexpiraçãodotokendeacesso CasadoCódigo
Figura7.9:Solicitaçãodeautorizaç ão
7.7 Trate a expiração do token de acesso
O tokenfornecidoparaacessarosserviçosdoGooglegeralmenteexpiramumahora
apósasuacriaç ão. Noentanto,outrosserviçostaiscomoTwittereFacebookque
tambémpossuemautorizaçãoviaOAuthpodemestipularumperíododetempo
diferenteparaavalidadedo tokendeacesso. Nossasaplicaçõesprecisamtratarda
expiraçãodele,casocontrárioteremosproblemasdeacessonãoautorizado.
Existemdiversasestratégiasparalidarcomessaexpiraç ão,quevariamdeacordo
comocenáriodeusoeotipodeaplicaç ão(web,mobileetc.)queutilizao token.
Umaalternativaémonitorarotempodeexpiraç ãoerevalidaro tokenantesque
otemposeesgote. Existemdoismétodosnaclasse Credentialquepodemnos
ajudarnisso:o getExpirationTimeMilliseconds,queretornaavalidadedo
218

## Página 221

CasadoCódigo Capítulo7. UtilizeGoogleAPIsecriefuncionalidadesinteressantes
tokenemmilissegundoseo getExpiresInSeconds()quedevolveaquantidade
desegundosquerestamantesqueeleexpire.
NaaplicaçãoBoaViagemsempreobteremosumnovo tokenquandoousuário
acessaraaplicação.Parafazerisso,seránecessárioinvalidaro tokenobtidoanterior-
mentedo AccountManager.O tokenjáconhecidoseráretornado,epodejáestar
expirado.
Éimportantefrisarqueobterumnovo tokennãoquerdizerqueousuárioterá
queautorizaroaplicativonovamente.Oaplicativocontinuaautorizado.Ousuário
nãonotaráqueissoaconteceu.
A invalidação do token e a recuperação de um novo serão realizadas no
método solicitarAutorizacao. Para invalidá-lo, invocamos o método
invalidateAuthTokendo AccountManager. Ocódigoquesolicitaumnovo
tokenpermaneceomesmojáapresentado.
Ainda que o usuário tenha escolhido se manter conectado, ou seja, en-
trardiretoseminformarascredenciais,teremosqueobterum tokenválidono-
vamente. Portanto, alteramos o métodoonCreate para invocar o método
solicitarAutorizacaoemvezde iniciarDashboardquandoaop ção“Man-
terconectado”foimarcada.Comisso,teremososeguintecódigo:
private void solicitarAutorizacao() {
String tokenAcesso = preferencias.getString(TOKEN_ACESSO, null);
String nomeConta = preferencias.getString(NOME_CONTA, null);
if(tokenAcesso != null){
accountManager.invalidateAuthToken(tokenAcesso);
conta = accountManager.getAccountByName(nomeConta);
}
accountManager.getAccountManager()
.getAuthToken(conta,
Constantes.AUTH_TOKEN_TYPE,
null,
this,
new AutorizacaoCallback(),
null);
}
@Override
219

## Página 222

7.8. ConheçaaCalendarAPI CasadoCódigo
public void onCreate(Bundle savedInstanceState) {
//códigos existentes
if(conectado){
solicitarAutorizacao();
}
}
Pronto!Agoraanossaaplicaç ãoestáutilizandoumacontadoGoogleparaau-
tenticarousuárioemantê-loconectado.
7.8 Conheça a CalendarAPI
ACalendarAPIpermitedesenvolveraplicaçõesqueinteragemcomaagendado
usuário,sendopossívelcriarnovoseventos,alterareexcluirosquejáexistem,além
depermitirarealizaç ãodebuscas.Tambémépossívelcriareremovercalendários.
ACalendarAPIpossuialgunsconceitosbásicos:
•Event-éumeventodeumaagenda(calendário)quepossuiinformaçõestais
comotítulo,participantesedatadeinícioefim;
•Calendar-representaumaúnicaagendadousuário.NoGoogleCalendaré
possívelcriarváriasagendas,umaéconsideradacomoaprincipaleéidenti-
ficadapelonomedacontadoGoogle.Asdemaisagendascriadassãoclassifi-
cadascomosecundárias;
•Calendar List -éalistadecalendáriosdousuário,contendooprincipale
ossecundários;
•Setting-representaaspreferênciasdousuário,comooseufusohorário;
•ACL-éumaregradeacesso(compartilhamento)docalendário;
•Color-sãoascoresutilizadasparadestacaroseventoseasagendas;
•Free/busy-conjuntodeperíodosnosquaisoscalendáriosnãopossuem
nenhumevento.
Paracadaconceitoexisteumrecursoassociado( Event, Calendareou-
tros).Osrecursossãoagrupadosedisponibilizadospeloserviçoatravésdecole ções(
Events, Calendars, CalerdarList, Settingse ACL).Estemodelosereflete
nabibliotecaclientequedispõedeclassespararepresentaressesrecursosecole ções.
220

## Página 223

CasadoCódigo Capítulo7. UtilizeGoogleAPIsecriefuncionalidadesinteressantes
AdocumentaçãocompletadaCalendarAPIestádisponívelem http://code.
google.com/apis/calendar/v3/using.html. Veremos a seguir algumas formas de
utilizá-la.
7.9 Adicione eventos noGoogleCalendar
Aautenticaçãoeautorizaç ãoestãoprontasenãocorremosmaisoriscodeutilizar
um tokendeacessoinválido. Alémdisso,jávimosumpoucodoqueéaCalendar
API.
Partiremosagoraparaainclusãodeumeventonaagendadousuário. Basica-
menteoqueprecisaremosfazeréutilizarasclassesdisponibilizadaspelabiblioteca
clientedaCalendarAPIparacriarosobjetosnecessárioseinvocarométodoque
realizaráainclusãodosdadosnaagenda.Todaapartedecomunicaç ãoHTTP,seri-
alizaçãodosdadosetratamentodasrespostasserãofeitospelabibliotecacliente.
Para continuar mantendo nosso código organizado, vamos criar
uma nova classe para tomar conta dessa integraç ão com o Go-
ogle Calendar. Crie a classe CalendarService no pacote
br.com.casadocodigo.boaviagem.calendar. De antemão, precisare-
mosdonomedacontaedo tokendeacessoqueserãoutilizados,vamosrecebê-los
noconstrutordaclasse:
public class CalendarService {
private Calendar calendar;
private String nomeConta;
public CalendarService(String nomeConta, String tokenAcesso) {
this.nomeConta = nomeConta;
GoogleCredential credencial = new GoogleCredential();
credencial.setAccessToken(tokenAcesso);
}
}
Onomedacontaseráutilizadoposteriormenteparaidentificarqualcalendário
seráutilizado,lembrandoqueesteseráocalendárioprincipaldousuário.Criamos
tambémumanovacredencialdoaplicativoeatribuímosaelao tokendeacesso.Esta
credencialseráutilizadaduranteasrequisiçõesparaoserviço.
Aclasse Calendardopacote com.google.api.services.calendarre-
presentaoserviçopropriamenteditoeatravésdelaconseguiremosmanipularos
221

## Página 224

7.9. AdicioneeventosnoGoogleCalendar CasadoCódigo
eventos.Suainstanciaçãoéfeitaatravésdeum builderquedependededoisoutros
objetosquefazempartedaGoogleAPIClientLibrary,quesãoo HttpTransport,
paraacomunicaçãoHTTPedo JsonFactory,paraserializaçãodosobjetos.Além
disso,devemosatribuirànossaAPI keyacredencialeonomedoaplicativo.Tudo
issorealizadoaindanoconstrutor:
public CalendarService(String nomeConta, String tokenAcesso) {
this.nomeConta = nomeConta;
GoogleCredential credencial = new GoogleCredential();
credencial.setAccessToken(tokenAcesso);
HttpTransport transport = AndroidHttp.newCompatibleTransport();
JsonFactory jsonFactory = new GsonFactory();
calendar = Calendar.builder(transport, jsonFactory)
.setApplicationName(Constantes.APP_NAME)
.setHttpRequestInitializer(credencial)
.setJsonHttpRequestInitializer(
new GoogleKeyInitializer(Constantes.API_KEY))
.build();
}
Aideiaéqueumeventosejacriadoapartirdasinformaçõesdeumaviagem.
Entãocriaremosummétodono CalendarServicequerecebeumaviagem,cha-
mado criarEvento:
public String criarEvento(Viagem viagem) { }
Criaremosumnovo Eventecolocamosasuadescriç ãocomosendoodestino
daviagem. Éobrigatórioinformarumalistadeparticipantesidentificadosatravés
doe-mail. Nonossocaso,oparticipanteéoprópriousuário,entãoinformamoso
nomedaconta(queéume-maildoGoogle)eincluímosno Event. Emseguida
criamosasdatasdeinícioefimdoeventobaseadosnoperíododaviagem,incluindo
asinformaçõesdefusohorário,obrigatóriosparaoCalendar.
public String criarEvento(Viagem viagem) {
Event evento = new Event();
evento.setSummary(viagem.getDestino());
List<EventAttendee> participantes =
Arrays.asList((new EventAttendee().setEmail(nomeConta)));
222

## Página 225

CasadoCódigo Capítulo7. UtilizeGoogleAPIsecriefuncionalidadesinteressantes
evento.setAttendees(participantes);
DateTime inicio = new DateTime(viagem.getDataChegada(),
TimeZone.getDefault());
DateTime fim = new DateTime(viagem.getDataSaida(),
TimeZone.getDefault());
evento.setStart(new EventDateTime().setDateTime(inicio));
evento.setEnd(new EventDateTime().setDateTime(fim));
}
Invocamosométododeacessoàcole ção eventsenelainserimosonovoevento
especificandoocalendárioatravésdonomedaconta.Paradefatorealizararequisi-
çãoparaoserviçodevemosinvocarométodo execute.
Emcasodesucesso,estemétodoretornaum Eventquepossuiumidentifica-
dorúnicoqueutilizamoscomovalorderetorno.Devemosutilizaresseidentificador
posteriormentesequisermoseditarouremoveroevento.Porsetratardeumarequi-
siçãoremotaépossívelqueuma IOExceptionsejalan çadaenestecasorelan çamos
aexce ção.
public String criarEvento(Viagem viagem) {
Event evento = new Event();
evento.setSummary(viagem.getDestino());
List<EventAttendee> participantes =
Arrays.asList((new EventAttendee().setEmail(nomeConta)));
evento.setAttendees(participantes);
DateTime inicio = new DateTime(viagem.getDataChegada(),
TimeZone.getDefault());
DateTime fim = new DateTime(viagem.getDataSaida(),
TimeZone.getDefault());
evento.setStart(new EventDateTime().setDateTime(inicio));
evento.setEnd(new EventDateTime().setDateTime(fim));
223

## Página 226

7.9. AdicioneeventosnoGoogleCalendar CasadoCódigo
try {
Event eventoCriado = calendar.events()
.insert(nomeConta, evento)
.execute();
return eventoCriado.getId();
} catch (IOException e) {
throw new RuntimeException(e);
}
}
Já estamos quase lá. Só falta alterar aViagemActivity para utilizar o
CalendarServiceeteremosainclusãodeeventosnaagendadousuáriocon-
cluída.
No método onCreate da ViagemActivity instanciaremos um
CalendarService recuperando o nome da conta e otoken de acesso das
preferênciasdoaplicativo:
// novo atributo
private CalendarService calendarService;
@Override
protected void onCreate(Bundle savedInstanceState) {
//códigos existentes
calendarService = criarCalendarService();
}
private CalendarService criarCalendarService() {
SharedPreferences preferencias =
getSharedPreferences(PREFERENCIAS, MODE_PRIVATE);
String nomeConta = preferencias.getString(NOME_CONTA, null);
String tokenAcesso = preferencias.getString(TOKEN_ACESSO, null);
return new CalendarService(nomeConta, tokenAcesso);
}
Comoinserirumnovoeventonaagendadousuárioéumaoperaç ãodemorada,
poisenvolveacessoàrede,implementaremosuma AsyncTask,paraexecutaressa
operaçãoemsegundoplano.Nocapítulo 6jáaprendemoscomofazê-lo.
Nométodo salvarViagem,logoapósagravaç ãonobancodedados,executa-
remosuma AsyncTaskparainseriroeventonaagendadousuário:
public void salvarViagem(View view){
// códigos existentes
224

## Página 227

CasadoCódigo Capítulo7. UtilizeGoogleAPIsecriefuncionalidadesinteressantes
if(id == -1) {
resultado = dao.inserir(viagem);
new Task().execute(viagem);
} else {
resultado = dao.atualizar(viagem);
}
// códigos existentes
}
private class Task extends AsyncTask<Viagem, Void, Void> {
@Override
protected Void doInBackground(Viagem... viagens) {
Viagem viagem = viagens[0];
calendarService.criarEvento(viagem);
return null;
}
}
Semmaisdelongas,inicieoaplicativo,cadastreumanovaviagemeconfirao
eventocriadonasuaagendadoGoogleCalendar!Pararealizarasoperaçõesdeatu-
alizaçãoeremo çãodeeventosdoGoogleCalendarénecessárioreferenciaro id
doeventodesejadoqueéretornadoquandoomesmoécriado.Apartirdelepode-
ríamosimplementarosmétodosderemo çãoeatualizaç ãono CalendarService
invocandoaAPIclientedaseguinteforma:
// para remover
calendar.events().delete(nomeConta, "eventId").execute();
// para atualizar
service.events().update(nomeConta, "eventId", eventoAtualizado)
.execute();
7.10 Conclusão
Nestecapítulorealizamosumaintegraç ãoparaincluirumnovoeventonaagenda
dousuárionoGoogleCalendarquandoumanovaviagemforcriadanoaplicativo
BoaViagem.
Utilizamostambémumacontaregistradanodispositivopararealizaraauten-
ticaçãodosusuários.AprendemosumpoucosobreoprotocoloOAuth2.0ecomo
225

## Página 228

7.10. Conclusão CasadoCódigo
aproveitaraGoogleClientLibrarypararealizaraautorizaç ãodeumaplicativoe
tambémefetuaraschamadasremotasaoserviçoGoogleCalendar.
Oconhecimentoadquiridonestecapítulopodeseraplicadoparaousodequal-
queroutraAPIdoGoogle,aproveite-as!
226

## Página 229

Capítulo8
Exploreosrecursosdehardware
UmadascaracterísticasquetornamaplataformaAndroidamigávelaodesenvolve-
doréaexistênciadeAPIsparafacilitaramanipulaç ãodosrecursosdehardware.
Quandobemutilizados,elesincrementamasfuncionalidadesdasaplicaçõeseme-
lhoramaexperiênciadousuário.
Nestecapítuloveremoscomoutilizaracâmeradodispositivoparacapturareexi-
birimagensevídeos.Atravésdo MediaPlayerfaremosareproduçãodemúsicase
vídeosalémdeimplementarumexemploutilizandooGPSparaobteralocalizaç ão
doaparelhoeexibi-laemummapa.
Para começar, crie um novo projeto Android, para testar os códigos
apresentados. Chame-o de Hardware para o projeto e utilize o pacote
br.com.casadocodigo.hardware.Nasse çõesseguintesveremoscódigospara
trabalharcomalgunsdosrecursosdehardwaredisponíveis.Érecomendadoutilizar
umaparelhoAndroidemvezdoemuladorpoisdestaformaserámaisrápidoemais
fácildeverificaroresultadodasimplementações.

## Página 230

8.1. Capturefotoscomseuaparelho CasadoCódigo
8.1 Capture fotos com seu aparelho
Umdosrecursosquemaissepopularizouentreostelefonescelulares,antesmesmo
daexistênciados smartphones,foiacâmerafotográficaembutidanodispositivo.
Comoumaimagempublicadaemumaredesocialvalemaisdoque140caracte-
res,aplicativoscomoInstagram,Skitcheváriosoutrosexploramesterecursopara
criarnovasformasdeinteraç ão.
Oobjetivonestase çãoéconhecercomoutilizaracâmeradodispositivoemum
aplicativoAndroid. Emnossoexemplo,iremosrequisitaraopróprioaplicativoda
câmeraparaqueafotosejacapturadautilizandouma Intent.Estaéumaforma
simplesepráticadeincluiressafuncionalidadenoseuaplicativo.
Asimagenscapturadasdevemserarmazenadasnocartãodememóriaparaevitar
queoespaçodearmazenamentointerno,queémaislimitadoeutilizadopelosistema
operacional,nãosejacomprometido.Alémdisso,ousuáriopoderetirarocartãodo
dispositivoeutilizaroseucomputadorpararecuperarasfotosfacilmente.
Por padrão, existem dois diretórios que podemos utilizar para salvar as
imagens capturadas. O getExternalStoragePublicDirectory, da classe
Environment,queretornaumdiretóriocompartilhadoportodasasaplicações,é
orecomendadoparaoarmazenamentodefotosevídeos.Comoelenãoestáasso-
ciadoaoaplicativoquegravouaimagem,quandoesteédesinstalado,osdadosnão
sãoperdidos.
O outro diretório que pode ser utilizado é o obtido através de
Context.getExternalFilesDir, que retorna um diretório associado ao
aplicativo. Asimagenssalvasnelesãoremovidasquandooaplicativoédesins-
talado. Aescolhadequalutilizardependedopropósitodoaplicativoedequal
comportamentoéomaisadequadoemcasodedesinstalaç ão.
Parainiciarostestescomacâmera, crieumanova activitycomonomede
CameraActivity. Nelaimplementaremosasfuncionalidadesdecapturaevisu-
alizaçãodaimagem.O layoutdesta activity( câmera.xml)terádoisbotõespara
dispararasfuncionalidadescitadas:
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
android:layout_width="match_parent"
android:layout_height="match_parent"
android:orientation="vertical" >
<Button
228

## Página 231

CasadoCódigo Capítulo8. Exploreosrecursosdehardware
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:text="@string/capturar_imagem"
android:onClick="capturarImagem"/>
<Button
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:text="@string/visualizar_imagem"
android:onClick="visualizarImagem"/>
</LinearLayout>
Na CameraActivityfaremosachamadaaoaplicativodacâmeraatravésde
uma Intent. Noentanto,precisaremosobterumarespostadesteaplicativopara
saberseacapturafoibemsucedidaounão.Nessassituaçõespodemosiniciaruma
atividadeutilizandoométodo startActivityForResult.Quandoaoperaç ão
solicitadaforfinalizada,ométodo onActivityResult,daatividadequefezaso-
licitação,éinvocado.Ocódigoinicialda CameraActivityéoseguinte:
public class CameraActivity extends Activity {
private static final int CAPTURAR_IMAGEM = 1;
private Uri uri;
@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.camera);
}
@Override
protected void onActivityResult(int requestCode,
int resultCode, Intent data) {
}
public void capturarImagem(View v){
}
public void visualizarImagem(View v){
}
}
229

## Página 232

8.1. Capturefotoscomseuaparelho CasadoCódigo
Pararealizaracapturadaimagem,precisaremoscriaruma Intentepassar
comoextraa Uriinformandoonomeelocaldearmazenamentodaimagem.Uti-
lizaremosodiretóriopúblico,queéorecomendado.
Recuperamosodiretórioeoescolhemosparaarmazenarnossasimagens. Em
seguidageramosonomedaimagemcombasenodiretórioobtidoutilizandoain-
formaçãodetempodosistemaemmilissegundosparatermosumnomeúnico. A
extensãodoarquivoédefinidacomo .jpg.Emseguida,recuperamosoobjeto Uri
comocaminho:
public void capturarImagem(View v) {
File diretorio = Environment
.getExternalStoragePublicDirectory(
Environment.DIRECTORY_PICTURES);
String nomeImagem = diretorio.getPath() + "/" +
System.currentTimeMillis() +
".jpg";
uri = Uri.fromFile(new File(nomeImagem));
}
Precisamosdefinira Intenteutilizá-laparainiciarumanovaatividadeque
deveretornarumresultado. Paraométodo startActivityForResulténe-
cessárioinformarumcódigoparaidentificarasolicitaç ão. Utilizamosaconstante
CAPTURAR_IMAGEMcomestafinalidade. Issoénecessário,poispodemosiniciar
váriasatividadesdistintasquedevemretornarresultados.Nonossoexemplo,mais
adianteutilizaremosométodo startActivityForResultcomuma Intent
paracapturarvídeos.
public void capturarImagem(View v) {
// Recupera o arquivo e a URI
Intent intent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
intent.putExtra(MediaStore.EXTRA_OUTPUT, uri);
startActivityForResult(intent, CAPTURAR_IMAGEM);
}
Quandooaplicativodacâmeratirarafotoeousuárioconfirmaracaptura,a ac-
tivitydacâmeraseráfinalizadacomumresultadoeométodo onActivityResult
230

## Página 233

CasadoCódigo Capítulo8. Exploreosrecursosdehardware
da CameraActivity será invocado. Neste método, faremos uma checa-
gem para saber se o resultado é para a solicitação que foi feita com o código
CAPTURAR_IMAGEM.
Emseguida,avaliaremosseoresultadoinformadopelacâmeraserefereaosu-
cessooufalhanacapturadaimagem.Emcasodesucesso,aimagemdeveseradici-
onadaàgaleriadefotosdoAndroid.Aimplementaç ãodo onActivityResulté
aseguinte:
@Override
protected void onActivityResult(int requestCode,
int resultCode, Intent data) {
if (requestCode == CAPTURAR_IMAGEM) {
if (resultCode == RESULT_OK) {
mostrarMensagem("Imagem capturada!");
adicionarNaGaleria();
} else {
mostrarMensagem("Imagem não capturada!");
}
}
}
private void mostrarMensagem(String msg){
Toast.makeText(this, msg,
Toast.LENGTH_LONG)
.show();
}
Pormaisquetenhamosarmazenadoaimagememumdiretóriocompartilhadoe
acessívelpelagaleriadefotosdoAndroid,elanãoéadicionadaláautomaticamente.
Énecessárioquefaçamosasuainclusão.Paraisso,bastadispararum broadcast
paranotificarqueafotodeveserincluídanagaleriautilizandoa Uridaimagem.O
códigopararealizarestaoperaç ãoéoseguinte:
private void adicionarNaGaleria() {
Intent intent = new Intent(
Intent.ACTION_MEDIA_SCANNER_SCAN_FILE);
intent.setData(uri);
this.sendBroadcast(intent);
}
Paraexibiraimagemcapturada,utilizaremosuma Intentparainvocaragale-
riadeimagensdoAndroid.Nométodo visualizarImagempassaremosa Urie
231

## Página 234

8.1. Capturefotoscomseuaparelho CasadoCódigo
oMIMEtypedaimagemna Intentparainiciara activity.Vejacomoficaocódigo:
public void visualizarImagem(View v){
Intent intent = new Intent(Intent.ACTION_VIEW);
intent.setDataAndType(uri, "image/jpeg");
startActivity(intent);
}
Comistotemosasfuncionalidadesdecapturarevisualizarimagensutilizando
Intentsprontas!Parainiciara CameraActivity,altereo main.xmlparain-
cluirumbotãoqueirádispararessaop ção.
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
android:layout_width="fill_parent"
android:layout_height="fill_parent"
android:orientation="vertical" >
<Button
android:id="@+id/camera"
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:onClick="escolherOpcao"
android:text="@string/testar_camera" />
</LinearLayout>
Na HardwareActivityimplementeométodo escolherOpcaoconformeo
códigoaseguir,paraabrira Intentparaacâmera.
public void escolherOpcao(View view){
if(view.getId() == R.id.camera){
Intent intent = new Intent(this, CameraActivity.class);
startActivity(intent);
}
}
Pronto,agoraésóexecutaraaplicaç ãoetestaracapturadefotos!
Nassituaçõesemqueacâmeraéessencialparaofuncionamentodoaplicativo
podemosincluiressaobrigatoriedadeno AndroidManifest.xml.Dessaforma,
dispositivosquenãopossuemcâmeranãopoderãoinstalaroaplicativo.Tambémé
possívelinformarqueoaplicativoutilizaacâmeramasqueelanãoéobrigatória.
232

## Página 235

CasadoCódigo Capítulo8. Exploreosrecursosdehardware
Parachecaraexistênciadacâmeraemtempodeexecuç ãopodemosfazerose-
guinte:
public void capturarImagem(View v){
boolean temCamera = getPackageManager()
.hasSystemFeature(PackageManager.FEATURE_CAMERA);
if(temCamera){
//códigos implementados para a captura de imagens
}
}
Aseguir,vejaaformadedeclararousodacâmeranomanifestocomorequisito
paraaaplicação.Repareque,comonãoestamosutilizandodiretamenteohardware
dacâmera,nãoénecessárioadicionarnenhumapermissão.
<!-- Câmera é obrigatória -->
<uses-feature android:name="android.hardware.camera"/>
<!-- Câmera não é obrigatória -->
<uses-feature android:name="android.hardware.camera"
android:required="false"/>
8.2 Grave vídeos
Outrorecursoquepodemosexploraremnossosaplicativoséagravaç ãodevídeos.
Tambémépossívelutilizar Intentpararequisitaragravaç ãodevídeosparaacâ-
meradodispositivoassimcomoéfeitoparaacapturadeimagens.
Alémdapossibilidadedeinformarondeovídeodeveserarmazenado,podemos
incluiroutrasinformaçõesextrasna Intentparaconfiguraracapturadovídeo:
•MediaStore.EXTRA_DURATION_LIMIT- configura a duração limite da
capturadevídeoemsegundos.
•MediaStore.EXTRA_VIDEO_QUALITY-determinaemqualqualidadeoví-
deodevesercapturado.Paravídeosembaixaqualidadedevemosinformaro
valor 0eparaosvídeosemaltaqualidade,ovalor 1.
•MediaStore.EXTRA_SIZE_LIMIT-defineotamanholimiteem bytespara
ovídeoqueestásendocapturado.
233

## Página 236

8.2. Gravevídeos CasadoCódigo
Para testar a gravação de vídeos, na CameraActivity criaremos um
novo método que utilizará o aplicativo da câmera para gravar em alta qua-
lidade, com duração de 5 segundos. Não informaremos nada para o extra
MediaStore.EXTRA_OUTPUT,oquefarácomqueovídeogravadosejaarmaze-
nadonodiretóriopadrãoecomumnomegeradoautomaticamente.Vejaocódigo
parainiciara Intent:
// nova constante para identificar a requisição
private static final int CAPTURAR_VIDEO = 2;
public void capturarVideo(View v){
Intent intent = new Intent(MediaStore.ACTION_VIDEO_CAPTURE);
intent.putExtra(MediaStore.EXTRA_VIDEO_QUALITY, 1);
intent.putExtra(MediaStore.EXTRA_DURATION_LIMIT, 5);
startActivityForResult(intent, CAPTURAR_VIDEO);
}
Nométodo onStartActivityteremosqueverificarseoresultadoobtidose
refereàcapturadevídeoeiremosutilizara Intentrecebidacomoparâmetropara
saberonomedoarquivoeolocalondeovídeofoiarmazenado.Veja:
@Override
protected void onActivityResult(int requestCode,
int resultCode, Intent data) {
if (requestCode == CAPTURAR_IMAGEM) {
if (resultCode == RESULT_OK) {
mostrarMensagem("Imagem capturada!");
adicionarNaGaleria();
} else {
mostrarMensagem("Imagem não capturada!");
}
} else if(requestCode == CAPTURAR_VIDEO) {
if (resultCode == RESULT_OK) {
String msg = "Vídeo gravado em " +
data.getDataString();
mostrarMensagem(msg);
uri = data.getData();
} else {
mostrarMensagem("Vídeo não gravado");
}
234

## Página 237

CasadoCódigo Capítulo8. Exploreosrecursosdehardware
}
}
Paraexibirovídeo,criaremosuma Intentutilizandoa Urirecuperadade
Intent.getData()querepresentaoarquivoquedesejamosvisualizar:
public void visualizarVideo(View v){
Intent intent = new Intent(Intent.ACTION_VIEW);
intent.setDataAndType(uri, "video/mp4");
startActivity(intent);
}
Para testar essas novas funcionalidades, acrescente emcamera.xml dois
Buttonsparachamarosmétodosdecapturarevisualizarovídeo.
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout ... >
<!-- botoes existentes -- >
<Button
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:onClick="capturarVideo"
android:text="@string/capturar_video" />
<Button
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:onClick="visualizarVideo"
android:text="@string/visualizar_video" />
</LinearLayout>
8.3 Execute vídeos e músicas
Nestase çãoiremosimplementaralgumasformasdeexecutarvídeosemúsicasem
uma aplicação Android, utilizando basicamente a classeMediaPlayere uma
VideoViewparaexibirosvídeos.Comececriandoumanovaatividadecomonome
de MediaPlayerActivityeumarquivodelayout media_player.xml,que
contarácomalgunsbotõesparaacionarasdiferentesformasdeexecuç ãodemúsi-
casedevídeoqueiremosimplementar,etambémparacontrolarasuaexecuç ão.A
definiçãoseráaseguinte:
235

## Página 238

8.3. Executevídeosemúsicas CasadoCódigo
<?xml version="1.0" encoding="utf-8"?>
<TableLayout xmlns:android="http://schemas.android.com/apk/res/android"
android:layout_width="match_parent"
android:layout_height="match_parent" >
<Button
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:onClick="executarMusicaArquivo"
android:text="@string/executar_musica_arquivo" />
<Button
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:onClick="executarMusicaUrl"
android:text="@string/executar_musica_url" />
<Button
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:onClick="executarVideo"
android:text="@string/executar_video" />
<TableRow>
<Button
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:onClick="parar"
android:text="@string/parar" />
<Button
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:onClick="executar"
android:text="@string/executar" />
<Button
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:onClick="pausar"
236

## Página 239

CasadoCódigo Capítulo8. Exploreosrecursosdehardware
android:text="@string/pausar" />
</TableRow>
</TableLayout>
Oprimeiroexemploconsisteemexecutarumarquivo .mp3existentedentroda
aplicação. Escolhaumadassuasmúsicaspreferidaseaincluanapasta res/raw
doprojeto(crieapasta rawsenecessário). Éimportantequeonomedoarquivo
nãocontenhacaracteresespeciais,porisso,nesteexemploutilizaremosumarquivo
chamado musica.mp3.
Naclasse MediaPlayerActivitycriaremosumnovo MediaPlayer,carre-
gandoestearquivodemúsica.Emseguidautilizaremososmétodosdisponíveisno
MediaPlayerparacontrolarsuaexecuç ão.
Vejaocódigoaseguir:
public class MediaPlayerActivity extends Activity{
private MediaPlayer player;
@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.media_player);
}
public void executarMusicaArquivo(View v) {
player = MediaPlayer.create(this, R.raw.musica);
player.start();
}
}
Utilizamosométodoutilitário MediaPlayer.createpassandoocontexto
eoidentificadordoarquivodemúsicaparacriarumnovo MediaPlayer. Para
iniciaraexecuç ãoinvocamosométodo start.Nométodo createoarquivofoi
carregadoeo MediaPlayer preparadoparaaexecuç ão.Oscontrolesserãofeitos
utilizandoosmétodosrespectivospresentesno MediaPlayer:
public void executar(View v) {
if(!player.isPlaying()) {
player.start();
237

## Página 240

8.3. Executevídeosemúsicas CasadoCódigo
}
}
public void pausar(View v) {
if(player.isPlaying()) {
player.pause();
}
}
public void parar(View v) {
if(player.isPlaying()) {
player.stop();
}
}
Ométodo startpodeserutilizadotantoparainiciaraexecuç ãopelapri-
meiravez,comopararetomarquandoestaestiverempausa. Noentanto,seare-
produçãoforinterrompidacomo stop,sóépossíveliniciá-lanovamenteapóso
MediaPlayerser preparado,ouseja,ométodo preparedeveserinvocado.
Outra questão importante é que devemos sempre liberar oMediaPlayer
quandoomesmonãoformaisnecessário.Istocontribuiráparaaliberaç ãodame-
móriaetambémdos codecsutilizados.
Podemossobrescreverométodo onStopda MediaPlayerActivitypara
tratardestaquestão:
@Override
protected void onStop() {
super.onStop();
liberarPlayer();
}
private void liberarPlayer() {
if(player != null){
player.release();
}
}
Nopróximoexemplo,emvezdecarregarumarquivo .mp3existentenaapli-
cação,faremososeucarregamentoapartirdeumaURL.Estecenáriorequeruma
atençãoespecialpoisenvolveacessoàInternet,oquepodetornaraoperaç ãodemo-
rada.
238

## Página 241

CasadoCódigo Capítulo8. Exploreosrecursosdehardware
Jávimosquenestescasosdevemosrealizaraoperaç ãodeformaassíncronapara
nãobloquearaUIecomoestaéumasituaç ãorecorrente,o MediaPlayerjádis-
ponibilizaummétododepreparaç ãoassíncrona.
Precisamosimplementarainterface OnPreparedListener,quepossuium
métodochamado onPrepared,queseráinvocadonotérminodapreparaç ãoas-
síncrona. Nestemétodo,apenaschamaremoso startparainiciarareproduç ão.
Nométodo executarMusicaUrlliberamosainstânciaanteriordo player,que
podetersidocriadaparaexecutarumarquivodaaplicaç ão,ecriamosumnovo
MediaPlayer.
public class MediaPlayerActivity extends Activity
implements OnPreparedListener {
//códigos existentes
public void executarMusicaUrl(View v) {
liberarPlayer();
player = new MediaPlayer();
}
@Override
public void onPrepared(MediaPlayer mp) {
player.start();
}
}
Agora,precisamoscriaruma UriapartirdeumaURLqualquer,querefe-
renciaoarquivo .mp3desejado. Emseguidaaatribuímoscomo datasourcedo
MediaPlayer,alémdeinformarqueeladeveráserexecutada.Porfim,atribuímos
aprópria activitycomoo listenerdapreparaçãoassíncronaqueéinvocada.
public class MediaPlayerActivity extends Activity
implements OnPreparedListener {
//códigos existentes
public void executarMusicaUrl(View v) {
liberarPlayer();
player = new MediaPlayer();
try {
239

## Página 242

8.3. Executevídeosemúsicas CasadoCódigo
Uri uri = Uri.parse("http://<alguma-url>/musica.mp3");
player.setDataSource(this, uri);
player.setAudioStreamType(AudioManager.STREAM_MUSIC);
player.setOnPreparedListener(this);
player.prepareAsync();
} catch (Exception e) {
throw new RuntimeException(e);
}
}
@Override
public void onPrepared(MediaPlayer mp) {
player.start();
}
}
Comisto,temosareproduç ãodemúsicasdaInternetetambémaquelasexis-
tentesnoaplicativoimplementadas!Antesdetestar,incluaapermissãodeacessoà
Internetno AndroidManifest.xml:
<uses-permission android:name="android.permission.INTERNET" />
Formatos suportados
OAndroidsuportadiversosformatosdeáudioevídeo,dentreeles
arquivos .mp3, .mp4e .3gp.Paraumarelaç ãocompletadosforma-
tossuportadosconsulte http://developer.android.com/guide/appendix/
media-formats.html.
Agoraprecisamosexibirumvídeoarmazenadonoaplicativo. Incluanapasta
res/rawumarquivodevídeocomumdosformatossuportados.Utilizaremosum
arquivocomnomede video.mp4. Aocontráriodareproduçãodeumarquivo
demúsicaemquemanipulamoso MediaPlayerdiretamente,agorairemosuti-
lizaruma viewquealémderealizaraexibiç ãodovídeopropriamentedito,tam-
bémofereceoscontrolesdeexecuç ão.Noarquivo media_player.xmlincluauma
VideoView:
<TableLayout ...>
<!-- códigos existentes -->
240

## Página 243

CasadoCódigo Capítulo8. Exploreosrecursosdehardware
<VideoView android:id="@+id/videoView" />
</TableLayout>
No método onCreate da MediaPlayerActivity obteremos uma re-
ferência para aVideoView e utilizá-la-emos na implementação do método
executarVideo. Basicamente,oquefaremosécriaruma Uriparaovídeoar-
mazenadonodispositivo,atribuí-laparaa VideoView,adicionaroscontrolesde
execuçãoquesãoimplementadospelaclasse MediaControllereporfim,iniciar
areproduçãoinvocandoométodo VideoView.start.
public class MediaPlayerActivity extends Activity
implements OnPreparedListener{
private MediaPlayer player;
private VideoView videoView;
@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.media_player);
videoView = (VideoView) findViewById(R.id.videoView);
}
public void executarVideo(View v) {
Uri uri = Uri.parse("android.resource://"+ getPackageName() +
"/" + R.raw.video);
videoView.setVideoURI(uri);
MediaController mc = new MediaController(this);
videoView.setMediaController(mc);
videoView.start();
}
}
A Uriinformadaparaa VideoViewpodesereferirtantoaumarquivolocal
comoaumarquivoremoto.A VideoViewjátrataapreparaçãoassíncronado player
etambémjáoliberaquandonãoestámaisemuso.Paraabrirestanova activity,
acrescenteumbotãoem main.xmleimplementeoscódigosnecessáriosnométodo
escolherOpcaoda HardwareActivity:
<!-- main.xml -->
<?xml version="1.0" encoding="utf-8"?>
241

## Página 244

8.4. DeterminealocalizaçãoatravésdoGPSedaRede CasadoCódigo
<LinearLayout...>
<!-- botoes existentes -->
<Button
android:id="@+id/mediaplayer"
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:onClick="escolherOpcao"
android:text="@string/testar_media_player" />
</LinearLayout>
public void escolherOpcao(View view){
if(view.getId() == R.id.mediaplayer){
Intent intent = new Intent(this, MediaPlayerActivity.class);
startActivity(intent);
}
}
Executeaaplicaçãoeexperimenteareproduç ãodevídeos.
8.4 Determine a localização através do GPS e da
Rede
GrandepartedossmartphonesetabletsAndroiddisponíveisnomercadocontam
comumsistemadeposicionamentoglobal,oGPS.Atravésdeleépossíveldeter-
minaralocalizaç ãododispositivocomboaprecisão. Noentanto,parafuncionar
adequadamenteénecessárioqueodispositivoestejaemumambienteabertopara
facilitaracomunicaçãocomossatélites.
Oprocessodelocalizareconectaraossatélitespodeserdemorado,oqueau-
mentaotempodeesperaporinformaçõesdelocalizaç ão.
Outraformadeseobteralocalizaç ãoéatravésdo Network Location Provider
queutilizaossinaisdarededecelulareWI-FIparadeterminaralocalizaç ãodo
usuário. Apesardesermenosprecisa,estaformaconsomemenosbateriaeobtém
resultadosdelocalizaç ãocommaisrapidez,alémdefuncionartantoemambientes
abertoscomoemrecintosfechados.
Apartirdessasinformaçõesdelocalizaç ão,podemos,porexemplo,desenvol-
verumaplicativoqueapresentaemummapaospontosdeinteressepróximosao
usuário,comosupermercados,farmáciasetc. Alocalizaçãodousuáriopassaaser
relevante.
242

## Página 245

CasadoCódigo Capítulo8. Exploreosrecursosdehardware
VamosutilizaroGPSearedeparaobterascoordenadasdelatitudeelongitude
eapresentarestalocalizaç ãoemummapadoGoogle.Continuaremosutilizandoo
mesmoprojeto Hardware.
Para acessar informações de localização a plataforma Android disponi-
biliza o LocationManager. Através dessa classe podemos registrar um
LocatitonListenerparareceberasatualizaçõesdelocalizaç ão, tantodeum
GPS_PROVIDERcomodeum NETWORK_PROVIDER.Alémdereceberdadosdelo-
calização,o listenerénotificadoquandoalgumprovedoréhabilitadooudesa-
bilitadopelousuárioetambémquandooprovedormudadeestado(foradeserviço,
disponível,temporariamenteindisponívelououtro).
Conforme o provedor de localização (GPS, rede ou ambos) que o
aplicativo irá utilizar, é necessário declarar as permissões adequadas no
AndroidManifest.xml. Quando o aplicativo utilizar apenas o provedor de
rede,entãoapermissãoquedeveserdeclaradaéaseguinte:
<uses-permission
android:name="android.permission.ACCESS_COARSE_LOCATION" />
JánocasoondeoGPSseráutilizado,apermissãonecessáriaéaseguinte:
<uses-permission
android:name="android.permission.ACCESS_FINE_LOCATION" />
Casooaplicativoutilizeosdoisprovedoresdelocalizaç ão,entãobastadeclarar
apermissão android.permission.ACCESS_FINE_LOCATION,quealémdeau-
torizarousodoGPS,tambémpermiteautilizaç ãodo Network Location Provider.
Incluaestapermissãonomanifestodoprojeto.
Para iniciar a implementação, crie uma nova classe com o nome de
LocalizacaoActivityeumnovoarquivode layoutparaelacomonomede
localizacao.xml.Inicialmente,nestatelaapresentaremosascoordenadasdela-
titudeelongitude,bemcomo providerresponsávelporessasinformações. Vejaa
definiçãodo layout:
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
android:layout_width="match_parent"
android:layout_height="match_parent"
android:orientation="vertical" >
243

## Página 246

8.4. DeterminealocalizaçãoatravésdoGPSedaRede CasadoCódigo
<TextView android:id="@+id/provedor"
android:layout_width="wrap_content"
android:layout_height="wrap_content" />
<TextView android:id="@+id/latitude"
android:layout_width="wrap_content"
android:layout_height="wrap_content" />
<TextView android:id="@+id/longitude"
android:layout_width="wrap_content"
android:layout_height="wrap_content" />
</LinearLayout>
Na LocalizacaoActivityregistraremosum listenerparareceberasatu-
alizaçõesdelocalizaç ãoeexibiremosessasinformaçõesnos TextViews.
Precisaremosobtero LocationManager, queéresponsávelporgerenciar
osprovedoresdelocalizaç ão. Depois, declaramosonosso listener, queve-
remos em seguida, e o registramos para receber as atualizações oriundas do
NETWORK_PROVIDERedo GPS_PROVIDER.
Para registrar um listener utilizamos o método
requestLocationUpdates informando o provedor desejado, o intervalo
detempoemmilissegundoseadistânciaemmetrosentreasatualizações.Aocon-
figurarestesdoisparâmetroscomo 0,issoindicaqueasatualizaçõesdelocalizaç ão
devemserrealizadasomaisfrequentementepossível.
public class LocalizacaoActivity extends Activity {
private LocationManager locationManager;
private TextView latitude, longitude, provedor;
@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.localizacao);
latitude = (TextView) findViewById(R.id.latitude);
longitude = ( TextView) findViewById(R.id.longitude);
provedor = (TextView) findViewById(R.id.provedor);
locationManager = (LocationManager)
this.getSystemService(Context.LOCATION_SERVICE);
244

## Página 247

CasadoCódigo Capítulo8. Exploreosrecursosdehardware
Listener listener = new Listener();
long tempoAtualizacao = 0;
float distancia = 0;
locationManager.requestLocationUpdates(
LocationManager.NETWORK_PROVIDER,
tempoAtualizacao, distancia, listener);
locationManager.requestLocationUpdates(
LocationManager.GPS_PROVIDER,
tempoAtualizacao, distancia, listener);
}
}
Repare que registramos olistener para receber atualizações tanto do
NETWORK_PROVIDERcomodo GPS_PROVIDER.
Agoraprecisamosimplementarum LocationListenerquereceberáasin-
formaçõesdelocalizaç ãoeatualizaráatelacomessesdados.Paraisso,criamosuma
classeprivadachamada Listener.
Quandoalocalizaç ãoobtidaporalgumdosprovedoresforalterada,ométodo
onLocationChangedéinvocadocomonovalocalizaç ãosendoenviadacomopa-
râmetro. Aclasse Locationfornecemétodospararecuperarasinformaçõesde
latitude,longitudeeoprovedordeorigem.Utilizamosestesmétodosparaatualizar
ovalordos TextViews.:
private class Listener implements LocationListener{
@Override
public void onLocationChanged(Location location) {
String latitudeStr = String.valueOf(location.getLatitude());
String longitudeStr = String.valueOf(location.getLongitude());
provedor.setText(location.getProvider());
latitude.setText(latitudeStr);
longitude.setText(longitudeStr);
}
@Override
245

## Página 248

8.4. DeterminealocalizaçãoatravésdoGPSedaRede CasadoCódigo
public void onStatusChanged(String provider, int status,
Bundle extras) {}
@Override
public void onProviderEnabled(String provider) {}
@Override
public void onProviderDisabled(String provider ) {}
}
Paraexecutaresteexemploerealizarostestesdelocalizaç ãoérecomendávelque
sejautilizadoumdispositivoAndroidaoinvésdoemulador.
Casonãotenhaumaparelhodisponível,épossívelutilizaroemuladoresimular
aslocalizaçõesdeGPS.Paraisto,noEclipseváem Window> Show View > Other
> Emulator Control.Umanovaabacomoamostradanaimagem 8.1seráaberta
enelapoderemosenviarinformaçõesdelocalizaç ãosimuladaparaoemulador.
Figura8.1:EmulatorControl
Incluaa LocalizacaoActivitynomanifesto,crieumbotãono main.xml
ealtereométodo escolherOpcaoda HardwareActivityparainiciaranova
atividade:
<!-- main.xml -->
<?xml version="1.0" encoding="utf-8"?>
246

## Página 249

CasadoCódigo Capítulo8. Exploreosrecursosdehardware
<LinearLayout...>
<!-- botoes existentes -->
<Button
android:id="@+id/localizacao"
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:onClick="escolherOpcao"
android:text="@string/testar_localizacao" />
</LinearLayout>
public void escolherOpcao(View view){
//códigos existentes
if(view.getId() == R.id.localizacao){
Intent intent = new Intent(this, LocalizacaoActivity.class);
startActivity(intent);
}
}
Agorasim! Executeaaplicaç ãoevejaasualocalizaç ão. Seestiverutilizando
umdispositivoparatestar,inicialmentealocalizaç ãoobtidaserádaredeeposteri-
ormentedoGPS,casoalgumsinalsejaobtido.Aimagem 8.2mostracomoficoua
aplicaçãoutilizandoalocalizaç ão.
Figura8.2:EmulatorControl
Opróximopassoéutilizaressasinformaçõesdelatitudeelongitudeparaexibira
localizaçãoemummapa.Parafazerisso,podemosutilizaro add-onGoogleAPIsque
contacomumabibliotecaparautilizaroGoogleMapsnoAndroidatravésdeuma
MapView. Noentanto,estaabordagemrequerumasériedepassosdepreparaç ão
247

## Página 250

8.4. DeterminealocalizaçãoatravésdoGPSedaRede CasadoCódigo
quesóéviávelquandooaplicativonecessitamanipulareinteragirintensamentecom
mapas.
Nonossoexemplo,noqualqueremosapenasexibiralocalizaç ão,podemosuti-
lizaraGoogleStaticMapsAPI,quepermitearecuperaç ãodeummapaemformato
deimagem,construídoapartirdealgunsparâmetrosinformadosemumaURL.Re-
sumindo,oquefaremoséumachamadaparaumaURL,informandoascoordenadas
dalocalizaçãocomoparâmetroereceberemoscomorespostaumaimagemqueéo
mapapropriamentedito.
TantoarequisiçãoparaoserviçodoGooglecomoaexibiç ãodaimagemserão
feitasutilizandouma viewdoAndroidchamadade WebView.A WebViewpermite
aexibiçãodepáginasdawebqueutilizaomesmo enginedonavegadordisponível
noAndroid.Ouseja,quandoincluímosuma WebViewemnossoaplicativo,temos
praticamentetodososrecursosdonavegadorpadrão.
Paracarregarpáginasdawebemuma WebView,énecessárioincluiraseguinte
permissãonomanifesto:
<uses-permission android:name="android.permission.INTERNET" />
Emseguida,adicioneuma WebViewnoarquivodelayout localizacao.xml
dessaforma:
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout...>
<!-- textviews existentes -->
<WebView
android:id="@+id/mapa"
android:layout_width="wrap_content"
android:layout_height="wrap_content" />
</LinearLayout>
Na LocalizacaoActivity criaremos dois novos atributos. Um para a
WebVieweooutroparaarmazenaraURLbaseparaoserviçodemapasestáticos.
Nométodo onCreaterecuperamosa WebViewparautilizá-laposteriormente.
private String urlBase = "http://maps.googleapis.com/maps/api" +
"/staticmap?size=400x400&sensor=true&markers=color:red|%s,%s";
private WebView mapa;
@Override
protected void onCreate(Bundle savedInstanceState) {
// códigos existentes
248

## Página 251

CasadoCódigo Capítulo8. Exploreosrecursosdehardware
mapa = (WebView) findViewById(R.id.mapa);
}
AURLdoserviçodemapasjáestáconfiguradacomalgunsparâmetros,quesão
otamanhodaimagemquedeveserretornada,uma flagindicandoqueascoorde-
nadasforamobtidasdeumsensoreasconfiguraçõesdomarcadordalocalizaç ão.
Omarcadorteráacorvermelhaeseráposicionadonascoordenadasdelatitude
elongitude,queserãoincluídasnolugardos %s.Estessãoalgunsdosparâmetros
disponíveisnaGoogleStaticMapsAPI—parasabermaisvisite https://developers.
google.com/maps/documentation/staticmaps/.
Paraexibiromapana WebView,bastamontaraURLcomascoordenadase
carregá-lacomométodo loadUrl,veja:
@Override
public void onLocationChanged(Location location) {
// códigos existentes
String url = String.format(urlBase, latitudeStr, longitudeStr);
mapa.loadUrl(url);
}
Dessaforma,semprequealocalizaç ãomudar,umnovomapaseráexibido. A
imagem8.3demonstracomoomapaseráexibidonaaplicaç ãodeexemplo. Éim-
portanteressaltarquenestecasoestamosutilizandoumaconfiguraç ãoparareceber
asatualizaçõesdelocalizaç ãoomaisfrequentementepossível.Emcenáriosreaisisto
nãoérecomendado,poisaumentaoconsumodabateria.
249

## Página 252

8.5. Conclusão CasadoCódigo
Figura8.3:EmulatorControl
8.5 Conclusão
Nestecapítulovimoscomoutilizaracâmeradodispositivoparaincrementarnossas
aplicaçõesfazendousodeimagensevídeos.Tambémutilizamoso MediaPlayer
parareproduzirmúsicasevídeostantodearquivosarmazenadosnodispositivo
comodearquivosdaweb.
AtravésdoGPS,recuperamosascoordenadasdelatitudeelongitudeeexibimos
alocalizaçãoobtidautilizandoummapageradopelaGoogleStaticMapsAPI.
ParafacilitarousodaStaticMapsAPI,queéumserviçoRESTqueretornauma
imagem,lan çamosmãodeuma WebViewquepermiterenderizarpáginasdaweb.
Comestesconhecimentosépossívelincrementarasfuncionalidadesdosseusaplica-
tivosequetalagoraincluirnoBoaViagemascoordenadasgeográficasrepresentando
250

## Página 253

CasadoCódigo Capítulo8. Exploreosrecursosdehardware
olocalondeogastofoirealizado?Bonscódigos!
251

## Página 255

Capítulo9
SuporteTabletseoutrosdispositivos
Aversão4doAndroidunificouaplataformaparaasuautilizaç ãotantoem tablets
como smartphones.Antesdissotínhamosaversão3.xprojetadaespecificamentepara
tabletseaversão2.xamplamenteutilizadaem smartphoneseemalgunsmodelosde
tablet.
A versão 3.0 introduziu novos recursos de UI como aActionBar e os
Fragments,quesãocomponentesdeinterfacegráficamodulares,possuindociclo
devidapróprio,ecriadosparafacilitarodesenvolvimentodeaplicativoscom layouts
diferentesparacadatipodedispositivo. Paratrazeralgunsdestesrecursosparaas
versõesanterioresdoAndroid,oGooglelan çouumpacotedecompatibilidadeque
permiteautilizaçãode Loaderse Fragments,inclusivenaversão1.6doAndroid.
Nestecapítuloveremoscomoutilizaropacotedecompatibilidadeparautilizar
osrecursosmaisrecentesdaplataforma,bemcomoconhecerasformasdesuportar
diversasversõesdoAndroideváriostamanhosdetela,incluindo tablets.

## Página 256

9.1. Prepareoseuambiente CasadoCódigo
9.1 Prepare o seu ambiente
Paraimplementarosexemplosdestecapítuloseránecessáriofazerodownloaddo
pacotedecompatibilidadeetambémcriarumnovoAVDparaemularumtabletde
10”comoAndroid4.1(JellyBean).
Opacotedecompatibilidadeéobtidoatravésdo Android SDK Manager. No
Eclipse,acesseomenu Window-> Android SDK Manager.Najanelaapresentada,
selecioneaop ção Android Support Library. Aproveiteetambémmarquea
opção Android 4.1( API 16)parabaixarestaversão,conformemostraaimagem
9.1.
Figura9.1:AndroidSupport
Depoisqueosdownloadsacabarem,abrao AVD Manager atravésdomenu
WindowdoEclipseecrieumnovoAVDcomosdadosilustradosnaimagem 9.2
paraemularum tablet.
254

## Página 257

CasadoCódigo Capítulo9. SuporteTabletseoutrosdispositivos
Figura9.2:Emulandoumtablet
Notequeaop ção Snapshotfoihabilitada.Esterecursopermitequeoestado
doemuladorsejasalvoemdisco,reduzindoconsideravelmenteotempodesuaini-
cializaçãodepoisqueomesmoéiniciadopelaprimeiravez.
TambéménecessárioincluiropacotedecompatibilidadenoprojetodoEclipse.
Paraisto,vánodiretóriodeinstalaç ãodoSDK,napasta extras/android/v4e
copieoarquivo android-support-v4.jarparaapasta libsdoprojeto.
9.2 Suporte v árias versões do Android
OAndroidpodeserexecutadoemumaquantidadebastantediversificadadedispo-
sitivos.Porumlado,issoaumentaagamadeusuárioseporoutro,tornanecessário
queosdesenvolvedoreslevememconsideraç ãoqualpúblico/dispositivosirãoaten-
dercomseusaplicativos.
Aversão2.xdoAndroidéaquepossuiamaiorbaseinstaladaeespera-seque,
comoaumentodonúmerodetabletsAndroidecomolan çamentodaversão4,esta
255

## Página 258

9.2. SuporteváriasversõesdoAndroid CasadoCódigo
situaçãomude. Aimagem 9.3mostraaparticipaç ãodecadaversãocombasenos
dispositivosqueacessamoGooglePlay.
Figura9.3:VersionShare
OGooglerecomendaqueoseuaplicativosejacompatívelcomcercade90%da
baseinstalada.DeacordocomosdadosdeJunhode2012,paraatenderestameta,
nossoaplicativoBoaViagem,desenvolvidoutilizandoaversão2.3.3,deveriasercom-
patíveltambémcomasversões2.2e2.1doAndroid.
Manteracompatibilidadecomversõesanterioresexigequeseabramãoderecur-
sosdisponíveisemAPIsmaisrecentes,oupior,mantercódigosespecíficosparacada
versão,causandoduplicaç ão.Noscasosemqueénecessárioverificar,emtempode
execução,qualéaversãodoAndroid,utilizamosasinformaçõescontidasnaclasse
Build.Vejacomoficaumcódigoqueverificaseoaplicativoestásendoexecutado
emumaversãosuperiora1.6paradecidircomorealizardeterminadaoperaç ão:
private void algumaOperacao() {
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.DONUT) {
// usar api nova
} else {
// usar api antiga
}
}
256

## Página 259

CasadoCódigo Capítulo9. SuporteTabletseoutrosdispositivos
Geralmente,quandosaiumanovaversãodoAndroid,novosatributosparaos
XMLstambémsãoincluídos. Issoquerdizerqueteremosversõesdiferentesde
XMLsparacadaversão?Felizmente,não.OAndroidautomaticamenteignoraestes
novosatributosquandooaplicativoestiversendoexecutadoemumaversãoanterior
quenãoospossui.
Para definir quais versões nosso aplicativo suporta, devemos declarar no
AndroidManifest.xmlqualéaversãomínimaetambémqualéaversãoalvo,
ouseja,aversãonaqualoaplicativofoidesenvolvido,testadoesabe-sequefunci-
onacorretamente.Vejaumexemploondeaversãomínimaéa2.2(API8)eaversão
alvoéa4.1(API16):
<manifest ... >
<uses-sdk android:minSdkVersion="8" android:targetSdkVersion="16" />
<!-- demais declarações -->
</manifest>
Alémderestringirporversões,tambémpodemosrestringirainstalaç ãodoapli-
cativocombasenascaracterísticaserecursosdisponíveisnosdispositivos.Podemos,
porexemplo,restringirquenossoaplicativosósejainstaladoemumdispositivoque
possuacâmeraeGPS:
<manifest ... >
<uses-feature android:name="android.hardware.location.gps" />
<uses-feature android:name="android.hardware.camera" />
<!-- demais declarações -->
</manifest>
Paraumarelaçãocompletadetodasosfiltrosquepodemseraplicadosparaim-
pedirqueseuaplicativosejainstaladoporumdispositivoquenãoofereceosrecursos
necessários,visitehttp://developer.android.com/guide/google/play/filters.html.Es-
tasconfiguraçõesnãosãoobrigatóriasmassemdúvidaauxiliamadirecionarseu
aplicativoapenasparaosdispositivosquepossamexecutá-locorretamente.
9.3 Suporte diversos tamanhos de tela
AtualmenteexisteumagrandevariedadededispositivosrodandoaplataformaAn-
droid,desde smartphonescomtelascompactas, tabletsdediferentestamanhoseaté
mesmo Smart TVscomtelasqueultrapassam32polegadas.
257

## Página 260

9.3. Suportediversostamanhosdetela CasadoCódigo
Paraqueousuáriotenhaumaboaexperiênciadeuso,independentementedo
dispositivoqueestejautilizando,éimportantequeseuaplicativosuporteváriostipos
detela,tirandoproveitodastelasmaioresparaexibirmaisconteúdoeotimizandoa
visualizaçãodeinformaçõesnocasodastelasmenores.
Paracadatamanhodetelaquesedesejasuportar,um layoutdiferentedeveser
definidoedeacordocomodispositivoqueestáexecutandoaaplicaç ão,oAndroid
aplicao layoutadequado.
NaplataformaAndroidastelassãoclassificadasdeacordocomduascaracterísti-
casprincipais:adensidadeeotamanho.Adensidadeserefereàquantidadedepixels
existentesemumadeterminadaáreadatela(umapolegada),cujaunidadedeme-
didaéo dpi(dots per inch).Porsimplificação,oAndroiddefinequatrodensidades:
baixa( ldpi),média( mdpi),alta( hdpi),extraalta( xhdpi).
Adensidadedeveserlevadaemconsideraç ãoquandoestamosdefinindoasdi-
mensõesdoscomponentesdeUIetambémquandoestamosconfeccionandoasima-
gens( drawables)queserãoutilizadosnoaplicativo. Supondoquetemosuma
imagemcomtamanho100x100paraumateladedensidademédia,paraatenderas
demaisdensidadesteremosoutrasversõescomtamanho75x75parabaixa,150x150
paraaltae200x200paraextraaltadensidade.Aescalautilizadaparadeterminaro
tamanhodasimagensdeacordocomadensidadeéaseguinte:
• ldpi-0.75
• mdpi-1.0
• hdpi-1.5
• xhdpi-2.0
Umavezcriadas,asimagensdevemsercolocadasnosdiretóriosde drawables
específicosparacadadensidade,vejaumexemplo:
BoaViagem/
res/
drawable-xhdpi/
configuracoes.png
drawable-hdpi/
configuracoes.png
drawable-mdpi/
configuracoes.png
258

## Página 261

CasadoCódigo Capítulo9. SuporteTabletseoutrosdispositivos
drawable-ldpi/
configuracoes.png
Deacordocomadensidadedodispositivo,oAndroidescolheráaimagemade-
quadaemtempodeexecuç ão. Casovocênãoforne çaimagensparacadatipode
densidade,oAndroidfaráporcontaprópriaoredimensionamentodasimagenso
quepodelevaraperdadequalidade.Noentanto,seaúnicaimagemdisponívelse
refereaumadensidademaiordoqueadisponível,oAndroidlan çaráumerro.
Jáotamanhoserefereaotamanhofísicodatela,medidopelocomprimento(em
polegadas)dadiagonaldatela.Algunsexemplosdetamanhodetelasãoasde 4.7",
7"e 10.1"polegadas.OAndroidagrupaastelasemquatrotamanhos:pequena(
small),normal( normal),grande( large)eextragrande( extra large).
Alémdisso,aindaexisteaorientaç ãodatelaquepodeserretrato(portrait )ou
paisagem(landscape),deacordocomopontodevistadousuário.Oseuaplicativo
develevaremcontaasmudan çasdeorientaç ãododispositivoqueacontecemem
tempodeexecuçãoparaajustaro layoutconformenecessário.Podemoscriar layouts
paratamanhoseorientaç ãodetelaespecíficos.Paraistobastacriaro layoutdesejado
ecolocá-lonodiretóriocorrespondente,seguindoaconven ção:
res/layout-<tamanho_da_tela>-<orientacao>
// exemplos
res/layout-small-port
res/layout-normal-land
Comoexisteumavariedadegrandedetamanhosdetela,comdensidadesdis-
tintas,oAndroiddefineumaunidadedemedidavirtual,o density-independent pixel
( dp),quedeveserutilizadaparaexpressardimensõesde layouteposiçõesinde-
pendentementedadensidadedatela. Um dpequivaleaumpixelfísicoemuma
telade160 dpi,queéadensidadepadrãoassumidapeloAndroidparaumatelade
densidademédia( mdpi).
Eleautomaticamentefazasconversõeseredimensionamentosdasmedidasem
dpparapixelsfísicosdeacordocomadensidadedatelaemuso.
Tambémexisteumamedidarelativaparaadefiniç ãodetamanhodostextos,o
sp(scale-independent pixel). O spseassemelhaao dp,comadiferen çadequeé
redimensionadodeacordocomaspreferênciasdetextodousuário.O spdeveser
utilizadounicamenteparaadefiniç ãodotamanhodetextos,nuncaparadimensões
de layout.Vejaalgunsexemplosdeuso:
259

## Página 262

9.3. Suportediversostamanhosdetela CasadoCódigo
<Button android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:text="@string/gastei"
android:layout_marginTop="25dp" />
<TextView
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:text="@string/local"
android:textSize="20sp" />
Apartirdaversão3.2doAndroid,aformadedefiniro layoutdeacordocom
otamanhodatela( small, normal, largee extra large)foidepreciada.
Agorapodemosdefini-losdeacordocomalarguraoualturadisponíveisem dp.
Épossível,porexemplo,definirum layoutquedeveserexibidoquandoalargura
datelaforde,nomínimo,600 dp,colocandooarquivoXMLcorrespondenteno
diretório res/layout-sw600dp.
Oqualificador swquerdizer smallest width.Alarguramínima( sw)serefereà
larguraespecificadapelodispositivo(600x1024mdpiemumtabletde7”,porexem-
plo),portanto,seuvalornãoéalteradoquandoaorientaç ãomuda.Podemosutilizar
oqualificador wparaindicaralarguradisponível,nãoimportandoseelafoialterada
porcontadamudan çadeorientaç ão.Vejaoutrosexemplos:
res/layout-w600dp/main.xml // a largura deve ser de 600dp
res/layout-h320dp/main.xml // altura mínima de 320dp
Sefornecessáriorestringirparaqueoaplicativonãosejainstaladoemumdis-
positivoquenãopossuiotamanhodetelasuportado,podemosincluirumadiretiva
no AndroidManifest.xmlquepodeconteraindaadensidadedetelarequerida.
Vejacomodeclararestarestriç ãoutilizandoo <supports-screens>:
<supports-screens android:resizeable=["true"| "false"]
android:smallScreens=["true" | "false"]
android:normalScreens=["true" | "false"]
android:largeScreens=["true" | "false"]
android:xlargeScreens=["true" | "false"]
android:anyDensity=["true" | "false"]
android:requiresSmallestWidthDp="integer"
android:compatibleWidthLimitDp="integer"
android:largestWidthLimitDp="integer"/>
Nessecaso,vocêpodeindicarparacadatipodetelaseeleserásuportadoounão.
260

## Página 263

CasadoCódigo Capítulo9. SuporteTabletseoutrosdispositivos
9.4 Utilize Fragments para simplificar seus
layouts
Os Fragmentssãocomponentesmodularesdeinterfacegráfica,comumciclode
vidapróprio,criadosparafacilitarodesenvolvimentodeaplicativoscom layouts
ajustáveisadiferentestamanhosdetela. EsterecursofoiadicionadonoAndroid
3edisponibilizadoparaasversõesanterioresatravésdeumabibliotecadecompati-
bilidade.
Aideiaéqueum Fragmentpossarepresentarorauma Activityúnica,sendo
exibidaemumdispositivocomtelacompacta,oraumapartedeuma Activity
quetambémexibeoutros Fragmentsnocasodeumtablet.Éoquedemonstraa
imagem9.4.
Figura9.4:Exibiç ãodeFragments
Um Fragmentdevenecessariamentefazerpartedeuma Activityeoseu
ciclodevidaéafetadoporela. Porexemplo,quandoumaatividadeédestruída,
todososseus fragmentstambémsão.
Outracaracterísticaimportanteéqueos Fragmentspodemseradicionados
eremovidosdaatividadeemtempodeexecuç ão,trazendoflexibilidadeparaacri-
açãodeumfluxodeinteraç ãocomousuárioquelevaemcontaodispositivoque
estásendoutilizado. Paraadicionarum Fragmentauma Activity,podemos
declará-lono layoutdamesma,atravésdoelemento <fragment>ouadicioná-lo
programaticamenteaum ViewGroup(todososlayoutsherdamdestaclasse)jáexis-
tente.
RetornaremosaoaplicativoBoaViagemparaimplementarumanovafuncionali-
261

## Página 264

9.4. UtilizeFragmentsparasimplificarseuslayouts CasadoCódigo
dadequetiraráproveitodatelamaiordeum tablet.Comoumaespéciedediáriode
bordo,estafuncionalidadeconsisteemregistraranotaçõesdiversassobreaviagem.
Aimagem 9.5ilustracomoos fragmentsserãoutilizados.
Figura9.5:UtilizandoFragments
Como o foco é o uso da API deFragments, não iremos nos preocupar
em recuperar as informações do banco de dados e nem criarlayoutspersona-
lizados para as listagens. Começaremos esta nova versão implementando um
Fragmentparaalistadeviagens. Porquestõesdeorganizaç ão, crieumnovo
pacote br.com.casadocodigo.boaviagem.fragmentparamantertodosos
Fragmentsqueserãocriados.
De forma análoga àListActivity, para utilizar umaListViewpode-
mosestenderaclasse ListFragment.Crieentãoumanovaclassecomnomede
ViagemListFragmentqueestendede ListFragment.Alémdisso,paratrataro
eventodequandoumitemdalistaforselecionado,nossanovaclassedeveráimple-
mentar %OnItemClickListener,veja:
public class ViagemListFragment extends ListFragment
implements OnItemClickListener {
@Override
public void onStart() {
}
262

## Página 265

CasadoCódigo Capítulo9. SuporteTabletseoutrosdispositivos
@Override
public void onItemClick(AdapterView<?> parent ,
View view, int position,
long id) {
}
}
Diferentementedométodo onCreateda Activity,ométodo onCreatede
um Fragmentéexecutadoantesdacriaçãodasua viewcorrespondente,oqueem
outraspalavrasquerdizerquenãotemoscomoacessarcomponentesdeinterface
gráficanestemétodo,poisosmesmosaindanemforamcriados. Porisso,iremos
sobrescreverométodo onStart,queéexecutadoquandoo Fragmentjáestá
prontoparaserexibido,pararealizarasimplementaçõesnecessárias.Vejaocódigo:
@Override
public void onStart() {
super.onStart();
List<String> viagens = Arrays.asList("Campo Grande", "São Paulo",
"Miami");
ArrayAdapter<String> adapter =
new ArrayAdapter<String>(getActivity(),
android.R.layout.simple_list_item_1, viagens);
setListAdapter(adapter);
getListView().setOnItemClickListener(this);
}
No método onStart criamos uma lista simulada de viagens e um
ArrayAdaptercomalistacriadaparaalimentara ListViewqueseráexibida.
Tambématribuímosopróprio Fragmentcomooresponsávelportrataroseventos
desele çãodeitensdalistagem.
Omínimonecessárioparaonossoprimeiro Fragmentjáfoiimplementado.Na
sequênciairemoscriaruma Activityparacontrolaraexibiç ãodos Fragments
quecompõemestánovafuncionalidade.Paraisto,precisaremoscriardois layouts,
umdelesseráutilizadopara tabletseoutroparadispositivoscomtelasmenores.
No layoutdestinadoa tabletsutilizaremostrês Fragmentsenquantonooutro
apenasum.CrieumnovoXMLde layoutchamado anotacoes.xmlecoloque-o
nodiretório res/layout.Adefiniç ãodeste layoutéaseguinte:
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
android:layout_width="match_parent"
263

## Página 266

9.4. UtilizeFragmentsparasimplificarseuslayouts CasadoCódigo
android:layout_height="match_parent"
android:orientation="vertical" >
<FrameLayout
android:id="@+id/fragment_unico"
android:layout_width="wrap_content"
android:layout_height="match_parent" />
</LinearLayout>
Reparequenãodeclaramosumelemento <fragment>nolayout.Emvezdisso,
incluímosum FrameLayout,oqualserásubstituídoemtempodeexecuç ãopelo
Fragmentquedeveserexibido.
Parao tablet,crieumnovo layoutcomomesmonome( anotacoes.xml),po-
rém,coloque-onodiretório res/layout-large-land.Este layoutseráutilizado
quandoodispositivoestivercomaorientaç ãopaisagemepossuirumatelaclassifi-
cadacomogrande.
Neste layoutdefiniremostrês fragmentsmascomoaindanãocriamostodos
eles,declararemosapenasum,edois FrameLayoutsparasimularoespaçoocu-
padopelosoutros fragments,veja:
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
android:layout_width="match_parent"
android:layout_height="match_parent"
android:orientation="horizontal" >
<fragment
android:id="@+id/fragment_viagens"
android:name=
"br.com.casadocodigo.boaviagem.fragment.ViagemListFragment"
android:layout_width="0dp"
android:layout_height="match_parent"
android:layout_weight="1" />
<FrameLayout
android:id="@+id/fragment_anotacoes"
android:layout_width="0dp"
android:layout_height="match_parent"
android:layout_weight="1" >
264

## Página 267

CasadoCódigo Capítulo9. SuporteTabletseoutrosdispositivos
<TextView
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:text="FRAGMENT B" />
</FrameLayout>
<FrameLayout
android:id="@+id/fragment_anotacao"
android:layout_width="0dp"
android:layout_height="match_parent"
android:layout_weight="1" >
<TextView
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:text="FRAGMENT C" />
</FrameLayout>
</LinearLayout>
Oatributo namedoelemento <fragment>deveseronomequalificadoda
classequeoimplementa.Opróximopassoserácriaraclasse AnotacaoActivity
quecontrolaráaexibiçãodos fragmentseacomunicaç ãoentreeles.Iniciaremos
aimplementaçãodestaclassecomocódigoaseguir:
public class AnotacaoActivity extends FragmentActivity {
private boolean tablet = true;
@Override
protected void onCreate(Bundle bundle) {
super.onCreate(bundle);
setContentView(R.layout.anotacoes);
View view = findViewById(R.id.fragment_unico);
if(view != null){
tablet = false;
ViagemListFragment fragment = new ViagemListFragment();
fragment.setArguments(bundle);
265

## Página 268

9.4. UtilizeFragmentsparasimplificarseuslayouts CasadoCódigo
FragmentManager manager = getSupportFragmentManager();
FragmentTransaction transaction =
manager.beginTransaction();
transaction.replace(R.id.fragment_unico, fragment);
transaction.addToBackStack(null);
transaction.commit();
}
}
}
Reparequeaclasseestendede FragmentActivityemvezde Activity.A
classe FragmentActivitypertenceaopacotedecompatibilidadeeatravésdela
podemosutilizarosrecursosdaAPIde FragmentsemversõesdoAndroidanteri-
oresàversão3.Noentanto,seoseuaplicativotivercomoalvoaversão3ousuperior,
entãovocêdeveutilizaraclasse ActivityquejáimplementaaAPInessasversões.
No método onCreate atribuímos a view identificada por
R.layout.anotacaoesparaa activity. Emtempodeexecuç ão,oAndroid
decidiráseiráutilizaro anotacoes.xmldapasta layoutouaquelelocalizado
em layout-large-land, deacordocomodispositivoqueestáemuso. Por
isso,tentamosrecuperaro FrameLayoutcomo id R.id.fragment_unico
paradeterminarqual layoutestásendoutilizado. Seesta viewexistir,entãoo
dispositivoemusonãoéum tableteénecessárioexibirum Fragmentporvez.
Emseguida,instanciamoso ViagemListFragmentqueéoprimeiroaser
exibidoparaousuário. Nalinhaseguinte,atribuímosum bundlequeéutili-
zadoparaaconstruç ãoeinicializaç ãodo Fragment. Oqueéfeitoemseguidaé
substituiro FrameLayoutexistentepelorecém-criado ViagemListFragment.
Para isto, utilizamos umaFragmentTransaction que é iniciada através do
FragmentManager.
Por fim, invocamos o métodoreplace da FragmentTransaction in-
formandonoprimeiroparâmetroqualéa viewquedevesersubstituída,eno
segundo, qualéo Fragmentquedevesercolocadoemseulugar. Ométodo
addToBackStackéutilizadoparaincluiratransaç ãona back stack,oquenaprá-
ticaquerdizerqueeste Fragmentestarádisponívelquandoousuárioestiverem
outratelaepressionarobotão“Voltar”.Entãoéfeitoo commitdatransaçãopara
efetivaraoperaç ãodesubstituiç ão.
Quandoaaplicaç ãoestiverexecutandoemum tablet,nadadediferenteprecisa
serfeito,poisno layoutjátemosadeclaraçãodos Fragmentsquedevemserexi-
266

## Página 269

CasadoCódigo Capítulo9. SuporteTabletseoutrosdispositivos
bidos.Paraexecutarestanovafuncionalidade,declarea AnotacaoActivityno
manifestoecrieumanovaop çãona dashboardparainiciá-la.Utilizandooemulador
detabletscriadopreviamenteparaexecutaroaplicativo,oresultadoobtidodeveser
semelhanteaoexibidonaimagem 9.6.
Figura9.6:Fragmentdalistadeviagens
Dandocontinuidade,iremosimplementarosdemais Fragmentseprogramar
acomunicaçãoentreeles. Quandoousuárioselecionarumaviagemdalista,de-
vemosexibirasanotaçõesassociadasàquelaviagemnosegundo Fragment. Ao
selecionarumaanotaç ãodalista,oterceiro Fragmentexibiráasinformaçõesda-
quelaanotação. Esteéofuncionamentodesejadoparao tablet. Casocontrário,
cada Fragmentdeveráserexibidoindividualmenteequemcontrolaráistoseráa
AnotacaoActivity.
Osegundo Fragment,alémdeexibiruma ListViewcomasanotaçõesjá
realizadas,tambémteráumabotãoquepermiteacriaç ãodeumanovaanotaç ão.
Então,precisaremosdeum layoutquepossuaumbotãoeuma ListView.Eleserá
utilizadopelo Fragmentdeanotações,tantopara smartphonescomo tablets.
Crie um novo XML no diretório res/layout com nome de
267

## Página 270

9.4. UtilizeFragmentsparasimplificarseuslayouts CasadoCódigo
lista_anotacoes.xml,dessaforma:
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
android:layout_width="match_parent"
android:layout_height="match_parent"
android:orientation="vertical" >
<Button
android:id="@+id/nova_anotacao"
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:text="@string/nova_anotacao" />
<ListView
android:id="@android:id/list"
android:layout_width="match_parent"
android:layout_height="wrap_content" >
</ListView>
</LinearLayout>
Parautilizarmosum ListFragmentcomum layoutquecontémmais wid-
gets, além daListView, é obrigatório declarar umaListView com o id
@android:id/list.
Como layoutjádefinido,crieumanovaclasseparaalistadeanotações,como
nomede AnotacaoListFragment.Ocódigoinicialdestaclasseseráoseguinte:
public class AnotacaoListFragment extends ListFragment
implements OnItemClickListener, OnClickListener {
@Override
public View onCreateView(LayoutInflater inflater,
ViewGroup container, Bundle savedInstanceState) {
return inflater.inflate(R.layout.lista_anotacoes,
container, false);
}
@Override
public void onStart() {
super.onStart();
268

## Página 271

CasadoCódigo Capítulo9. SuporteTabletseoutrosdispositivos
}
@Override
public void onItemClick(AdapterView<?> parent ,
View view, int position,
long id) {
}
@Override
public void onClick(View v) {
}
}
O layoutqueseráutilizadopelo Fragmentéconstruídono onCreateView,
quecriaa viewatravésdométodo LayoutInflater.inflate.
A AnotacaoListFragment implementa duas interfaces, a
OnItemClickListener para tratar eventos da lista de anotações e a
OnClickListener para tratar o evento do botão que cria uma nova anota-
ção.Quandoestávamoslidandoapenascom activities,nóscolocávamosnoatributo
onClickdoelemento <Button>onomedométodoquedeveriaserinvocado.
Noentanto,esterecursonãoestádisponívelparaos Fragments.
Nométodo onStartalémdecriarumalistaeum adapterparaa ListView,
tambémprecisaremosatribuiro onClickListener,queéopróprio Fragment,
paraobotão R.id.nova_anotacao.Vejacomoficaaimplementaç ãodestemé-
todo:
@Override
public void onStart() {
super.onStart();
List<Anotacao> anotacoes = listarAnotacoes();
ArrayAdapter<Anotacao> adapter =
new ArrayAdapter<Anotacao>(getActivity(),
android.R.layout.simple_list_item_1,
anotacoes);
setListAdapter(adapter);
getListView().setOnItemClickListener(this);
269

## Página 272

9.4. UtilizeFragmentsparasimplificarseuslayouts CasadoCódigo
Button button =
(Button) getActivity().findViewById(R.id.nova_anotacao);
button.setOnClickListener(this);
}
private List<Anotacao> listarAnotacoes() {
List<Anotacao> anotacoes = new ArrayList<Anotacao>();
for (int i = 1; i <= 20; i++) {
Anotacao anotacao = new Anotacao();
anotacao.setDia(i);
anotacao.setTitulo("Anotacao " + i);
anotacao.setDescricao("Descrição " + i);
anotacoes.add(anotacao);
}
return anotacoes;
}
O ArrayAdapterinvoca o métodotoStringdos objetos da lista pas-
sadacomoparâmetro,paraobterovalorquedevesercolocadoemcadalinhada
ListView.Entãosobrescrevemosométodo toStringda Anotacaopararetor-
narodiaeotítulodamesma.
Aclasse Anotacao,querepresentaumaanotaç ãofeitapelausuário,édefinida
como:
public class Anotacao{
private Long id;
private Integer dia;
private String titulo;
private String descricao;
// getters e setters
@Override
public String toString() {
return "Dia " + dia + " - " + titulo;
}
}
270

## Página 273

CasadoCódigo Capítulo9. SuporteTabletseoutrosdispositivos
Paraqueonovo AnotacaoListFragmentsejavisualizado,precisamosincluí-
lono layoutpara tablets. Bastaalteraroarquivo anotacoes.xmldodiretório
layout-large-landparaindicaronovo fragmentcriado:
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
android:layout_width="match_parent"
android:layout_height="match_parent"
android:orientation="horizontal" >
<!-- fragment ViagemListFragment -->
<fragment
android:id="@+id/fragment_anotacoes"
android:name=
"br.com.casadocodigo.boaviagem.fragment.AnotacaoListFragment"
android:layout_width="0dp"
android:layout_height="match_parent"
android:layout_weight="1" />
<!-- FrameLayout FRAGMENT C -->
</LinearLayout>
Aoexecutaraaplicaç ãonoemuladorde tablet,veremosumatelasemelhanteà
apresentadanaimagem 9.7.Noentanto,seo tabletestivernaorientaç ãoretratoou
um smartphoneestiverexecutandooaplicativo,oúnico Fragmentexibidoconti-
nuasendoodalistadeviagens.Antesdenospreocuparmoscomestaquestãovamos
primeirofinalizaroúltimo Fragmentqueexibiráosdetalhesdaanotaç ãoselecio-
nada.
271

## Página 274

9.4. UtilizeFragmentsparasimplificarseuslayouts CasadoCódigo
Figura9.7:Fragmentdalistadeviagens
Mudando a orientação no emulador
Noemulador,paramudaraorientaç ãoentreretratoepaisagemevice-
versabastapressionar Ctrl+F12.
CrieumnovoXMLde layout,comnomede anotacao.xml,nolocalpadrão
paraserutilizadopelo Fragmentdedetalhesdaanotaç ão.Este layoutteráwidgets
básicoscomoTextViewsparaadescriçãodoscampos, EditTextsparaousuário
informarosdados,alémdeum Button,paraconfirmar.
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
android:layout_width="match_parent"
android:layout_height="match_parent"
android:orientation="vertical" >
<TextView
android:layout_width="wrap_content"
272

## Página 275

CasadoCódigo Capítulo9. SuporteTabletseoutrosdispositivos
android:layout_height="wrap_content"
android:text="@string/dia" />
<EditText
android:id="@+id/dia"
android:layout_width="50dp"
android:layout_height="wrap_content"
android:inputType="number" />
<TextView
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:text="@string/titulo" />
<EditText
android:id="@+id/titulo"
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:inputType="text" />
<TextView
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:text="@string/descricao" />
<EditText
android:id="@+id/descricao"
android:layout_width="match_parent"
android:layout_height="0dp"
android:layout_weight="1"
android:inputType="textMultiLine" />
<Button
android:id="@+id/salvar"
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:text="@string/salvar"/>
</LinearLayout>
Comonestecasonãoprecisaremosdeuma ListView,vamoscriarumanova
273

## Página 276

9.4. UtilizeFragmentsparasimplificarseuslayouts CasadoCódigo
classe,queherdade Fragment,comonomede AnotacaoFragment.Também
implementaremos OnClickListenerparatrataraoperaç ãodesalvar.Ocódigo
inicialdessaclasseseráoseguinte:
public class AnotacaoFragment extends Fragment
implements OnClickListener {
private EditText dia, titulo, descricao;
private Button botaoSalvar;
private Anotacao anotacao;
@Override
public View onCreateView(LayoutInflater inflater,
ViewGroup container, Bundle savedInstanceState) {
return inflater.inflate(R.layout.anotacao, container, false);
}
@Override
public void onStart() {
super.onStart();
dia = (EditText) getActivity().findViewById(R.id.dia);
titulo = (EditText) getActivity().findViewById(R.id.titulo);
descricao =
(EditText) getActivity().findViewById(R.id.descricao);
botaoSalvar = (Button) getActivity().findViewById(R.id.salvar);
botaoSalvar.setOnClickListener(this);
}
@Override
public void onClick(View v) {
// salvar Anotacao no banco de dados
}
}
Agorabastaincluiro AnotacaoFragmentno anotacoes.xmlqueficará
assim:
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
android:layout_width="match_parent"
android:layout_height="match_parent"
android:orientation="horizontal" >
274

## Página 277

CasadoCódigo Capítulo9. SuporteTabletseoutrosdispositivos
<fragment
android:id="@+id/fragment_viagens"
android:name=
"br.com.casadocodigo.boaviagem.fragment.ViagemListFragment"
android:layout_width="0dp"
android:layout_height="match_parent"
android:layout_weight="1" />
<fragment
android:id="@+id/fragment_anotacoes"
android:name=
"br.com.casadocodigo.boaviagem.fragment.AnotacaoListFragment"
android:layout_width="0dp"
android:layout_height="match_parent"
android:layout_weight="1" />
<fragment
android:id="@+id/fragment_anotacao"
android:name=
"br.com.casadocodigo.boaviagem.fragment.AnotacaoFragment"
android:layout_width="0dp"
android:layout_height="match_parent"
android:layout_weight="1" />
</LinearLayout>
Aoexecutaraaplicaç ãonovamentejávisualizaremoso layoutcompletocomto-
dosos Fragmentscriados,comomostraaimagem 9.8.
275

## Página 278

9.5. ComunicaçãoentreFragments CasadoCódigo
Figura9.8:Fragmentdalistadeviagens
9.5 Comunicação entre Fragments
Jáconstruímosos Fragmentsnecessáriosparaoregistrodeanotações.Nestase ção
veremoscomotrocarinformaçõesentre Fragmentsparacompletaraimplemen-
taçãodestanovafuncionalidadedoaplicativoBoaViagem.
Paraquepossamosfacilmentereutilizarum Fragmenténecessárioqueeleseja
implementadocomoumcomponentemodular,possuindooseupróprio layoute
comportamento.Dessaforma,podemosutilizaromesmo Fragmentparacompor
telasdistintasquevariamconformeodispositivoemuso.
Um Fragmentsempreestáatreladoauma Activityeéelaquemdeveorques-
traracomunicaç ãoentreseus Fragments,inclusivecontrolarquaisdelesdevem
serexibidos.Jáiniciamosumaimplementaç ãoassimna AnotacaoActivityque
verificaseserãoexibidosvários Fragmentsouapenasum.
Paracompletarafuncionalidadederegistrodeanotações,nesta Activityim-
plementaremosalógicadetrocaro Fragmentexibidoquandooaplicativoestiver
sendoutilizadoemum smartphoneefornecessárioapresentarumporvez. Tam-
bémfaremosacomunicaç ãoeapassagemdedadosdeumparaoutroutilizando
276

## Página 279

CasadoCódigo Capítulo9. SuporteTabletseoutrosdispositivos
esta Activity.
Os Fragmentsnãodevemsecomunicardiretamente,porissoérecomendado
quesejadefinidauma interfacecomasoperaçõesqueoselesdevemnotificar.A
Activityresponsávelporcoordená-losdeveimplementaresta interfaceeto-
marasaçõesnecessárias,geralmenteinvocandoalgummétododeoutro Fragment.
No nosso caso, o ViagemListFragment deve notificar a
AnotacaoActivity quando uma viagem for selecionada na lista. O mesmo
acontececoma AnotacaoListFragment,quealémdeinformarqualitemda
ListViewfoiselecionado,tambémnotificaquandoousuáriopressionaobotão
para criar uma nova anotação. Vamos criar umainterface com nome de
AnotacaoListenerparadefinirestescomportamentos,vejaocódigo:
public interface AnotacaoListener {
void viagemSelecionada(Bundle bundle);
void anotacaoSelecionada(Anotacao anotacao);
void novaAnotacao();
}
No ViagemListFragment, invocaremos o métodoviagemSeleciona
quandoousuárioescolherumitemdalista. Paraisto,precisaremosdeumarefe-
rênciaparaa Activityqueimplementaa AnotacaoListener.Podemosobtê-la
sobrescrevendoométodo onAttachdo Fragment.Naimplementaçãodométodo
onItemClick,recuperaremosoitemselecionadoda ListView,colocando-oem
um Bundle,queserápassadocomoparâmetrodométodo viagemSelecionada.
Vejacomoficou:
public class ViagemListFragment extends ListFragment
implements OnItemClickListener {
// novo atributo
private AnotacaoListener callback;
// códigos existentes
@Override
public void onItemClick(AdapterView<?> parent,
View view, int position,
long id) {
String viagem = (String) getListAdapter().getItem(position);
Bundle bundle = new Bundle();
bundle.putString(Constantes.VIAGEM_SELECIONADA, viagem);
277

## Página 280

9.5. ComunicaçãoentreFragments CasadoCódigo
callback.viagemSelecionada(bundle);
}
@Override
public void onAttach(Activity activity) {
super.onAttach(activity);
callback = (AnotacaoListener) activity;
}
}
public class Constantes {
// nova constante
public static final String VIAGEM_SELECIONADA =
"viagem_selecionada";
}
Naclasse AnotacaoListFragmentprecisaremosdisponibilizarummétodo,
queseráchamadopela AnotacaoActivity,paralistarasanotaçõesdeumavi-
agem,recebendoporparâmetroo bundlequefoipassadopelooutro Fragment
contendoaviagemselecionada.
Criaremosummétodo,chamado listarAnotacoesPorViagem,queverifi-
carásealgumaviagemfoiinformadaatravésdo bundlerecebidocomoparâmetro.
Elecriaumalistadeanotaçõesfictíciasparaalimentara ListView,noentanto,
seriafacilmenteadaptávelpararecuperarasinformaçõesdobancodedados,caso
necessário.
Modificaremos o método onStart, para também utilizar o
listarAnotacoesPorViagem. Dessa forma, quando oFragment for ini-
cializado programaticamente pela AnotacaoActivity, a lista de anotações
tambémserácarregada.
@Override
public void onStart() {
super.onStart();
Button button =
(Button) getActivity().findViewById(R.id.nova_anotacao);
button.setOnClickListener(this);
getListView().setOnItemClickListener(this);
listarAnotacoesPorViagem(getArguments());
}
278

## Página 281

CasadoCódigo Capítulo9. SuporteTabletseoutrosdispositivos
public void listarAnotacoesPorViagem(Bundle bundle) {
if(bundle != null &&
bundle.containsKey(Constantes.VIAGEM_SELECIONADA)){
//utilize a informação do bundle para buscar
// as anotacoes no banco de dados
List<Anotacao> anotacoes = listarAnotacoes();
ArrayAdapter<Anotacao> adapter =
new ArrayAdapter<Anotacao>(getActivity(),
android.R.layout.simple_list_item_1,
anotacoes);
setListAdapter(adapter);
}
}
O próximo passo é alterar a AnotacaoActivity para implementar
AnotacaoListener,destemodo:
public class AnotacaoActivity extends FragmentActivity
implements AnotacaoListener {
// códigos existentes
@Override
public void viagemSelecionada(Bundle bundle) { }
@Override
public void anotacaoSelecionada(Anotacao anotacao) {}
@Override
public void novaAnotacao() {}
}
Nométodo viagemSelecionadairemosverificarseoaplicativoestásendo
executadoemum tablet(ououtrodispositivoquepossuaumatelamaior)ecom
basenestainformaçãoiremosourecuperaro AnotacaoListFragmenteinvocaro
seumétodo listarAnotacoesPorViagecasoseja tablet,ouinstanciarumnovo
AnotacaoListFragmentecolocá-lonolugardo FrameLayoutcasosejaum
dispositivocomtelamenor.
279

## Página 282

9.5. ComunicaçãoentreFragments CasadoCódigo
Obteremosum FragmentManagerqueseráutilizadorealizaroperaçõessobre
os Fragments,atravésdométodo getSupportFragmentManager.
Casoum tabletestejasendoutilizado,recuperamoso Fragmentcomalistade
anotaçõesatravésdo managerenalinhaseguinteinvocamosométodoparalistar
anotaçõesdeumadeterminadaviagemeassimatualizaralistadeanotaçõesexibidas
pelo AnotacaoListFragment.
Casonãosejaum tablet,criamosumnovo AnotacaoListFragment,atri-
buímos a ele umbundle e através de umatransaction substituímos o
FrameLayoutpelo Fragmentrecém-criado.Dessaforma,quandoousuáriose-
lecionarumaviagemhaveráumatransiç ãodo ViagemListFragmentparaeste
novo Fragmentqueseráexibidoindividualmentenatela.
@Override
public void viagemSelecionada(Bundle bundle) {
FragmentManager manager = getSupportFragmentManager();
AnotacaoListFragment fragment;
if(tablet) {
fragment = (AnotacaoListFragment) manager
.findFragmentById(R.id.fragment_anotacoes);
fragment.listarAnotacoesPorViagem(bundle);
} else {
fragment = new AnotacaoListFragment();
fragment.setArguments(bundle);
manager.beginTransaction()
.replace(R.id.fragment_unico, fragment)
.addToBackStack(null)
.commit();
}
}
Osoutrosdoismétodosda%AnotacaoListener serão implementados de
forma bastante similar ao que acabamos de fazer. A próxima
implementação será para tratar a seleção de uma anotação,
cujos detalhes devem ser exibidos no AnotacaoFragment . Na
classe AnotacaoListFragment implementaremos o método onItemClick
280

## Página 283

CasadoCódigo Capítulo9. SuporteTabletseoutrosdispositivos
para recuperar um objeto Anotacao da ListView e passá-lo como
parâmetro para o método anotacaoSelecionada
// novo atributo
private AnotacaoListener callback;
// códigos existentes
@Override
public void onAttach(Activity activity) {
super.onAttach(activity);
callback = (AnotacaoListener) activity;
}
@Override
public void onItemClick(AdapterView<?> parent,
View view, int position,
long id) {
Anotacao anotacao = (Anotacao) getListAdapter().getItem(position);
callback.anotacaoSelecionada(anotacao);
}
Emvezdeutilizarum Bundle,destavezpassamosopróprioobjetorecuperado
dalistacomoparâmetroparaométodo anotacaoSelecionada. Écomumo
usodasduasalternativas,cabeavocêdecidir,deacordocomasuaaplicaç ão,quala
melhorestratégiaaseradotada.
No AnotacaoFragmentcriamosdoismétodospúblicos, umparaatribuir
aanotação, quedeveserexibidapelo Fragmenteoutroparaprepararaedi-
ção de uma anotação selecionada da lista. Veja o código alterado da classe
AnotacaoFragment:
// Novo atributo
private Anotacao anotacao;
@Override
public void onStart() {
super.onStart();
dia = (EditText) getActivity().findViewById(R.id.dia);
titulo = ( EditText) getActivity().findViewById(R.id.titulo);
281

## Página 284

9.5. ComunicaçãoentreFragments CasadoCódigo
descricao = (EditText) getActivity().findViewById(R.id.descricao);
botaoSalvar = (Button) getActivity().findViewById(R.id.salvar);
botaoSalvar.setOnClickListener(this);
if(anotacao != null) {
prepararEdicao(anotacao);
}
}
public void setAnotacao(Anotacao anotacao) {
this.anotacao = anotacao;
}
public void prepararEdicao(Anotacao anotacao) {
setAnotacao(anotacao);
dia.setText(anotacao.getDia().toString());
titulo.setText(anotacao.getTitulo());
descricao.setText(anotacao.getDescricao());
}
Retornando para a AnotacaoActivity, implementaremos o método
anotacaoSelecionadadaseguinteforma:
@Override
public void anotacaoSelecionada(Anotacao anotacao) {
FragmentManager manager = getSupportFragmentManager();
AnotacaoFragment fragment;
if(tablet){
fragment = (AnotacaoFragment) manager
.findFragmentById(R.id.fragment_anotacao);
fragment.prepararEdicao(anotacao);
}else{
fragment = new AnotacaoFragment();
fragment.setAnotacao(anotacao);
manager.beginTransaction()
.replace(R.id.fragment_unico, fragment)
.addToBackStack(null)
.commit();
282

## Página 285

CasadoCódigo Capítulo9. SuporteTabletseoutrosdispositivos
}
}
A implementação é bem parecida com a realizada no método
viagemSelecionada com a diferença apenas doFragment utilizado e dos
métodosinvocados. Paraimplementararegrasassociadasàcriaç ãodeumanova
anotaçãotambémserábastantesimples.Na AnotacaoListFragmentprecisamos
implementarométodo onClickqueiráfazero callbackseminformarnenhum
parâmetro:
@Override
public void onClick(View v) {
callback.novaAnotacao();
}
Criaremosummétodopúblicoem AnotacaoFragmentparaserinvocadopela
AnotacaoActivityquandoousuárioescolheraop çãodecriarumanovaano-
tação. Afunçãodestemétodoébasicamentelimparquaisquerdadosqueestavam
sendoexibidospreviamente.Vejaasuaimplementaç ão:
public void criarNovaAnotacao() {
anotacao = new Anotacao();
dia.setText("");
titulo.setText("");
descricao.setText("");
}
Na AnotacaoActivity,invocaremosométodo criarNovaAnotacaocaso
sejaum tabletquejáestáexibindotodosos Fragments,oucriaremosumnovo
AnotacaoFragmentseminformarumaanotaç ãojáquedesejamoscriarumanova.
Vejacomoficaaimplementaç ãodométodo novaAnotacao.
@Override
public void novaAnotacao() {
FragmentManager manager = getSupportFragmentManager();
AnotacaoFragment fragment;
if(tablet) {
fragment = ( AnotacaoFragment) manager
.findFragmentById(R.id.fragment_anotacao);
fragment.criarNovaAnotacao();
283

## Página 286

9.6. CarreguedadoscomLoaders CasadoCódigo
} else {
fragment = new AnotacaoFragment();
manager.beginTransaction()
.replace(R.id.fragment_unico, fragment)
.addToBackStack(null)
.commit();
}
}
Pronto!Nossos Fragmentsjáestãoimplementadoseinteragementresi.Exe-
cuteaaplicaçãoeconfiraoresultado!
9.6 C arregue dados com Loaders
Outrorecursomuitoútilinseridonaversão3doAndroidedisponívelnopacote
decompatibilidadesãoos Loaders,quepossuemafun çãodecarregardadosde
formaassíncronaemuma Activityou Fragment. Outracaracterísticaéque
um Loaderpodemonitorarumafontededados,comoum ContentProvider,e
automaticamentedisponibilizarosresultadosassimqueainformaç ãoéatualizada.
O Android já disponibiliza oCursorLoader para carregar dados em
cursorese,senecessário,podemosimplementaronossopróprio Loaderes-
tendendode AsyncTaskLoaderparacarregarassincronamenteoutrostiposde
recurso.
Nestase çãofaremosumaimplementaç ãodeexemploparaexploraresterecurso,
utilizandoo ContentProviderquejácriamosparacarregaralistadeviagens
atravésdeum CursorLoader. Aclasse LoaderManageréaresponsávelpor
gerenciarumoumais Loadersemuma Activityou Fragment.Asoperações
devemserrealizadasatravésde callbacks.Paraisto,énecessárioimplementara
interface LoaderCallbacks.Vejaocódigoabaixo:
public class ViagemListFragment extends ListFragment
implements OnItemClickListener,
LoaderCallbacks<Cursor> {
// códigos existentes
@Override
public void onActivityCreated(Bundle savedInstanceState) {
super.onActivityCreated(savedInstanceState);
284

## Página 287

CasadoCódigo Capítulo9. SuporteTabletseoutrosdispositivos
getLoaderManager().initLoader(0, null, this);
}
Override
public Loader<Cursor> onCreateLoader(int id, Bundle args) { }
@Override
public void onLoadFinished(Loader<Cursor> loader, Cursor data) { }
@Override
public void onLoaderReset(Loader<Cursor> loader) { }
}
Para implementar LoaderCallbacks, incluímos o método
onCreateLoader, que é utilizado para criar um novo Loader, o
onLoadFinishede o onLoaderReset, que são chamados, respectivamente,
quandoum Loaderterminoudesercarregadoequandofoiresetado.
Nométodo onActivityCreated,invocadoquandoaatividadequecontém
o Fragmentécriada,recuperamosum LoaderManagerefazemosainicializaç ão
deum Loaderatravésdométodo initLoader.Oprimeiroparâmetroqueeste
métodorecebeéumnúmeroqueidentificao Loaderquesedesejacarregar. No
segundo,podemospassarum Bundlecomdadosnecessáriosparasuaconstruç ão,
eoterceiroargumentoéaimplementaç ãodo callbackquenestecasoéopróprio
Fragment.
Nométodo onCreateLoaderdevemosinstanciareretornaro Loaderque
seráutilizado. Nonossocasoutilizaremosum CursorLoaderparacarregaras-
sincronamenteasviagensobtidasdonosso ContentProvider.Aimplementaç ão
destemétodoéaseguinte:
@Override
public Loader<Cursor> onCreateLoader(int id, Bundle args) {
Uri uri = Viagem.CONTENT_URI;
String[] projection = new String[]{ Viagem._ID, Viagem.DESTINO };
return new CursorLoader(getActivity(),
uri, projection, null, null, null);
}
Porenquantosóestamoscarregandoosdadoseaindanãooscolocamosna
ListView.Opróximopassoéalteraraimplementaç ãodométodo onStartpara
utilizarum CursorAdapter,veja:
285

## Página 288

9.6. CarreguedadoscomLoaders CasadoCódigo
// novo atributo
private SimpleCursorAdapter adapter;
@Override
public void onStart() {
super.onStart();
adapter = new SimpleCursorAdapter(getActivity(),
android.R.layout.simple_list_item_1, null,
new String[] { Viagem.DESTINO },
new int[] { android.R.id.text1 }, 0);
setListAdapter(adapter);
getListView().setOnItemClickListener(this);
}
Quando o carregamento dos dados for finalizado, no método
onLoaderFinisheddevemosalteraro cursorutilizadopelo CursorAdapter
paraexibirosdadosrecuperados. Damesmaforma,devemosalterá-loquandoo
Loaderforreiniciado.Vejacomoficamessasimplementações:
@Override
public void onLoadFinished(Loader<Cursor> loader, Cursor data) {
adapter.swapCursor(data);
}
@Override
public void onLoaderReset(Loader<Cursor> loader) {
adapter.swapCursor(null);
}
Aúltimaalteraçãonecessáriaémodificaraimplementaç ãodo onItemClick
pararecuperaro iddoitemselecionadonalistadeviagens.Este idseráutilizado
posteriormenteparacarregarasanotaçõesassociadascomaviagemselecionada.As
alteraçõessãoasseguintes:
@Override
public void onItemClick(AdapterView<?> parent,
View view, int position,
long id) {
long viagem = getListAdapter().getItemId(position);
Bundle bundle = new Bundle();
bundle.putLong(Constantes.VIAGEM_SELECIONADA, viagem);
286

## Página 289

CasadoCódigo Capítulo9. SuporteTabletseoutrosdispositivos
callback.viagemSelecionada(bundle);
}
Agoraaoexecutaraaplicaç ão,teremoso Loadercarregandoosdadospara
alimentaralistadeviagens.Experimente!
9.7 Conclusão
Nestecapítulovimoscomoprojetarnossoaplicativoparaqueelesejacompatível
com tabletseoutrosdispositivos,comdiversostamanhosdetelaediferentesversões
deAndroid.
Acrescentamosmaisumafuncionalidadeaoaplicativo BoaViagemqueutiliza
osrecursosdaAPIde Fragmentsparaproverumainteraç ãoe layoutdiferenciados
paraousoemum tablet.Porfim,exercitamosautilizaç ãode Loadersparacarregar
dadosdeformaassíncrona.
287

## Página 291

Capítulo10
PublicaçãonoGooglePlay
Chegouahoradepublicarasuaappparaomundo! Pararealizaroregistrocomo
desenvolvedornoGooglePlay,vocêiráprecisardeumacontadoGoogleedeum
cartãodecréditointernacionalpararealizaropagamentodataxadeU$ 25,00. O
processoésimpleseservetantoparapessoafísicacomoparaempresas.Vejaaseguir
comocriarasuacontaerealizarapublicaç ãodeumaapp.
10.1 Prepare a aplicação
Antesdemaisnada,énecessárioprepararasuaaplicaç ãoparaqueelapossaserpu-
blicadaeposteriormenteatualizadanoGooglePlay.Osprimeirositensquedevemos
conferiréno AndroidManifest.xml:
1 <?xml version="1.0" encoding="utf-8"?>
2 <manifest xmlns:android="http://schemas.android.com/apk/res/android"
3 package="br.com.casadocodigo.boaviagem"
4 android:versionCode="1"

## Página 292

10.1. Prepareaaplicação CasadoCódigo
5 android:versionName="1.0" >
6 <!-- demais itens -->
Onomedopacote,especificadonoatributo package(linha3)deveserúnico
paraidentificarasuaaplicaç ãonoGooglePlay,porissoécomumutilizaralgoseme-
lhanteaumdomíniodeInternet.Umavezpublicada,nãoserámaispossívelalterar
estenomedepacote. Oatributo versionCodeéoutroatributoimportanteque
identificaaversãoatualdaaplicaç ão. Esteatributoéutilizadoparaverificarsehá
atualizaçõesaseremrealizadasnoaplicativo.
A cada nova versão esse número deve ser incrementado. Já o atributo
versionName(linha4)édeusolivreparaodesenvolvedornomearaversãoda
formaquequiser.EsteatributoéexibidonoGooglePlayetambémnoprópriodis-
positivoenquantoqueo versionCode(linha5)éinvisívelparaousuário.
Dandocontinuidadeàpreparaç ão,oAndroidexigequetodososaplicativosse-
jamassinadosdigitalmentecomoumaformadeidentificaroautordaaplicaç ão.Du-
ranteodesenvolvimento,opluginADTjácuidadageraç ãoeassinaturado apksem
termosquenospreocupar.Paraapublicaç ãonoGooglePlaycriaremosumcertifi-
cadodigitalautoassinadopararealizaraassinaturado apk.
Paraqueasatualizaçõesdoaplicativopossamseraplicadasdeformatranspa-
renteparaousuário,éimportantesempreassinaraaplicaç ãocomomesmocerti-
ficado.QuandooAndroidatualizaumaplicativo,éverificadoseoscertificadosda
versãonovacoincidemcomaquelesdaversãoinstalada.Seforemidênticos,então
aatualizaçãoérealizada.Casocontrário,nãoserápossívelrealizaraatualizaç ão.A
seguir,vejacomoexportar,gerarocertificadoeassinaro apkparapublicação.
290

## Página 293

CasadoCódigo Capítulo10. PublicaçãonoGooglePlay
Figura10.1:Exportação
Comomostraafigura 10.1,acesseomenu File-> Exporteescolhaaop ção
Export Android Application. Depoisinformeoprojetodesejado(imagem
10.2).Natelaseguinte,mostradanaimagem 10.3,selecioneaop ção Create new
keystore,poiséaprimeiravezqueestamosrealizandoesseprocesso.Napróxima
exportação,vocêpoderáescolheraop çãodeutilizarum keystoreexistente.In-
formeumasenhaseguraesuaconfirmaç ão.
291

## Página 294

10.1. Prepareaaplicação CasadoCódigo
Figura10.2:Exportação
292

## Página 295

CasadoCódigo Capítulo10. PublicaçãonoGooglePlay
Figura10.3:Exportação
Napróximatela,ilustradanafigura 10.4,informaremososdadosdachave. É
recomendadoqueavalidadedocertificadosejasuperiora25anos.Informenova-
menteumasenhasegura,um aliaseaidentificaç ãodoautordaaplicaç ão. Os
demaiscampossãoopcionais.
293

## Página 296

10.1. Prepareaaplicação CasadoCódigo
Figura10.4:Exportaç ão
Parafinalizaraexportaç ão,napróximatelaselecioneolocaldedestinodoar-
quivo apkassinadoecliqueem Finish,comomostraafigura 10.5.
Agoraasuaaplicaç ãoestáprontaparaserpublicada!
294

## Página 297

CasadoCódigo Capítulo10. PublicaçãonoGooglePlay
Figura10.5:Exportação
295

## Página 298

10.2. Crieumacontadedesenvolvedor CasadoCódigo
10.2 Crie uma conta de desenvolvedor
Figura10.6:AndroidDeveloperConsole
Acesseosite https://play.google.com/apps/publish/efaçaologinutilizandoasua
contaGoogle(imagem 10.6). Umatelasemelhanteàexibidanaimagem 10.7será
apresentadaparaopreenchimentodosdadosbásicos.
296

## Página 299

CasadoCódigo Capítulo10. PublicaçãonoGooglePlay
Figura10.7:Informaçõesbásicas
Emseguida,aceiteocontratodedistribuiç ãocomoilustraafigura 10.8
297

## Página 300

10.2. Crieumacontadedesenvolvedor CasadoCódigo
Figura10.8:Contratodedistribuiç ão
Emseguida,énecessáriorealizaropagamentodataxacomumcartãodecrédito
internacionalutilizandooserviçoGoogleWallet,comomostramasimagens 10.9e
10.10.
298

## Página 301

CasadoCódigo Capítulo10. PublicaçãonoGooglePlay
Figura10.9:Pagamentodataxa
299

## Página 302

10.2. Crieumacontadedesenvolvedor CasadoCódigo
Figura10.10:Pagamentodataxa
Apósopagamentotersidorealizadocomsucesso,vocêteráacessoaoconsole
dodesenvolvedor,mostradonaimagem10.11.
300

## Página 303

CasadoCódigo Capítulo10. PublicaçãonoGooglePlay
Figura10.11:AndroidDeveloperConsole
Casoasuaaplicaç ãonãosejagratuita,seránecessáriocriarumacontadecomer-
ciante(Merchant Account)paraquevocêpossareceberosvaloresdasvendas.Para
criarestetipodeconta,utilizeaop çãodisponívelnoprópriositeAndroidDeveloper
Consoleepreenchaasinformaçõesnecessárias.
10.3 Realize a publicação
Parapublicarasuaaplicaç ão,noconsoledodesenvolvedor(imagem 10.11)esco-
lhaaop ção Enviaraplicativo. Umatelaseráabertaparaarealizaç ãodoupload
doarquivo .apkquefoipreviamentepreparado,conformemostraaimagem 10.12.
Depoisdisso,seránecessáriopreencherinformaçõesadicionaissobreoaplicativo,
incluindooíconeemaltaresoluç ão,capturasdetela,imagensetextosdedivulgaç ão
eadescriç ãodoqueaaplicaç ãofaz(imagem 10.13). Sejacaprichosonaprodução
301

## Página 304

10.3. Realizeapublicação CasadoCódigo
destesitenspoiselesserãooprimeirocontatocomousuário.
Figura10.12:Uploaddo.apk
302

## Página 305

CasadoCódigo Capítulo10. PublicaçãonoGooglePlay
Figura10.13:Informaçõesadicionais
Outrosdadostambémdevemserinformados,sigaasorientaçõescontidasna
própriapáginaparaoseucorretopreenchimento.
Pronto!Agoraésóclicarempublicareaguardaroprocessodepublicaç ãoque
geralmentelevapoucashorasparaserconcluído.
303

## Página 307

Capítulo11
Continueosestudos
Ufa!Depoisdeumalongaeboajornadachegamosaofinaldonossolivro.Criamos
umaaplicaçãocheiadefuncionalidadesinteressantesquepoderãoservirdebaseou
inspiraçãoparaquevocêdesenvolvaseusprojetos.
Noentanto,éimportantesaberqueseusestudosnãopodempararporaqui.
Existemuitomaterialbommundoafora,sendoqueaprimeirafontequevocêdeve
sempreirbuscarporinformaçõesénapáginaoficialdoAndroid, http://developer.
android.com.
Fiqueatentoeacompanheolan çamentodasnovasversõesdoAndroidquesem-
prevêmcomnovidades,nãosóparaousuáriofinalcomotambémparaodesenvol-
vedor.Diversosguiasmostrandocomofuncionamosnovosrecursossãopublicados
napáginaoficial.Existemtambémmuitoslivrosbons,comooAndroidinAction,
doW.FrankAbleson,RobiSen,ChrisKingeC.EnriqueOrtiz.
CrietambémohábitodeinvestigarocódigofontedoAndroid,poiseleésem-
preumaboareferênciadeimplementaçãoedescobertas: http://source.android.com.
Outropontoimportanteéconhecereaplicarasguidelinesdedesignrecomendados

## Página 308

CasadoCódigo
peloGoogleem https://developer.android.com/design/. Valorizeaexperiênciado
usuáriopoiselaéumpontochaveparaosucessodasuaaplicaç ão.
Alémdisso,preocupe-secomaqualidadedocódigoproduzidoeutilizeferra-
mentaseframeworksparaauxiliá-loemtarefascorriqueiras. Algunsexemplosde
frameworksquepodemajudarsão:
• ORM Lite -http://ormlite.com - ferramenta para mapeamento objeto-
relacionalcompatívelcomAndroid.
• AndroidQuery-http://code.google.com/p/android-query/-bibliotecacom
funções utilitárias para requisições e tarefas assíncronas, manipulação de
viewseoutrasutilidades.
• AndroidAnnotations-http://androidannotations.org/-frameworkquere-
solvesituaçõesrecorrentescomo bindingde views,recursosdosistemae
criaçãode listeners.
• SpringAndroid-http://www.springsource.org/spring-android-framework
queoferecefacilidadesparacomunicaç ãocomserviçosRESTeautenticaç ão
OAuth.
Porfim,esperoquevocêtenhamuitosucessonassuasaplicaçõesAndroideque
continueaperfeiçoandoseusconhecimentos!
306

## Página 309

CasadoCódigo ReferênciasBibliográficas
ReferênciasBibliográficas
307