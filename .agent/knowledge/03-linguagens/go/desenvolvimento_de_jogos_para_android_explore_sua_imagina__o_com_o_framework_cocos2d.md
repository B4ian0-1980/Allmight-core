---json
{
  "id": "desenvolvimento_de_jogos_para_android_explore_sua_imagina__o_com_o_framework_cocos2d",
  "title": "Desenvolvimento de Jogos para Android Explore sua imaginação com o framework Cocos2D",
  "categoria": "03-linguagens",
  "subcategoria": "go",
  "resumo": "**Arquivo Original:** `Desenvolvimento de Jogos para Android Explore sua imaginação com o framework Cocos2D.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "android",
    "cocos2d",
    "com",
    "desenvolvimento",
    "explore",
    "framework",
    "imagina",
    "jogos"
  ],
  "perguntas_tipo": [
    "Como utilizar Desenvolvimento de Jogos para Android Explore sua imaginação com o framework Cocos2D?",
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

# Desenvolvimento de Jogos para Android Explore sua imaginação com o framework Cocos2D

> **Arquivo Original:** `Desenvolvimento de Jogos para Android Explore sua imaginação com o framework Cocos2D.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 2

© Casa do Código
Todos os direitos reservados e protegidos pela Lei nº9.610, de 10/02/1998.
Nenhuma parte deste livro poderá ser reproduzida, nem transmitida, sem auto-
rização prévia por escrito da editora, sejam quais forem os meios: fotográficos,
eletrônicos mecânicos, gravação ou quaisquer outros.
Casa do Código
Livros para o programador
Rua Vergueiro, 3185 - 8º andar
04101-300 – Vila Mariana – São Paulo – SP – Brasil

## Página 5

CasadoCódigo
Agradecimentos
AgradeçoemespecialaoamigoMauricioTollin,daBivisSoft,comquemtiveaopor-
tunidadedeaprenderosconceitosiniciaisemdesenvolvimentodejogos.
Existemmuitasoutraspessoasquegostariadeagradecer,pormeajudaremde
formadiretaouindiretanesseprojeto:AdrianoAlmeida,AlbertoSouza,ChrisLeite,
DelsonLeite,EdsonSueyoshi,EleniraFerreira,GuilhermeSilveira,KarineHermes,
LuciaHermes,MauricioAniche,PauloSilveira,SheilaPaixaoeVictorHermes.
Obrigadoatodosvocês.
i

## Página 7

CasadoCódigo Sumário
Sumário
1 Introdu ção ao desenvolvimento de jogos no Android 1
1.1 Oquevocêencontraránestelivro ..................... 3
1.2 Quecomeceadiversão! ........................... 7
2 Protótipo de um jogo 9
2.1 Iniciandooprojeto ............................. 1 1
2.2 Criandoabasedojogo ...........................2 0
2.3 Desenhandooobjetoprincipal ...................... 2 5
2.4 Captandooscomandosdousuárioemovendoobjetos ......... 2 9
2.5 Criandooinimigo .............................. 3 3
2.6 Detectandocolisõesemostrandoresultados ............... 3 5
2.7 Adicionandoumplacar ........................... 4 1
2.8 Criandobotõesdeinterfacedousuário .................. 4 3
2.9 Adicionandomaisvida:imagensdanaveedocéu ...........4 6
2.10 Conclusão...................................4 8
3 História do jogo 5 1
3.1 14-bis ..................................... 5 2
3.2 14-bisVS100Meteoros ........................... 5 3
4 T ela inicial: Lidando com Background, logo e botões de menu 5 7
4.1 Iniciandooprojeto ............................. 5 9
4.2 SobreoCocos2D ............................... 6 3
4.3 Background ..................................6 4
4.4 AssetsdaTeladeabertura .........................6 6
iii

## Página 8

Sumário CasadoCódigo
4.5 Capturandoconfigura çõesiniciaisdodevice ............... 6 7
4.6 Logo ......................................7 0
4.7 Botões .....................................7 0
4.8 Conclusão ...................................7 6
5 T ela do jogo e objetos inimigos 79
5.1 GameScene ..................................8 0
5.2 Transiçãodetelas .............................. 8 2
5.3 Engines .................................... 8 2
5.4 Meteor ..................................... 8 5
5.5 Teladogame .................................8 6
5.6 Conclusão ...................................8 8
6 Criando o Player 89
6.1 DesenhandooPlayer ............................9 0
6.2 Botõesdecontrole .............................. 9 2
6.3 Atirando ................................... 9 7
6.4 Movendooplayer ..............................1 0 2
6.5 Conclusão ...................................1 0 4
7 Detectando colisões, pontuando e criando efeitos 107
7.1 Detectandocolisões .............................1 0 8
7.2 Efeitos .....................................1 1 1
7 . 3 P l a y e r m o r r e.................................1 1 6
7.4 Placar .....................................1 1 7
7.5 Conclusão ...................................1 1 9
8 Adicionando sons e música 121
8.1 Executandosons ...............................1 2 2
8.2 Cachedesons ................................1 2 3
8.3 Músicadefundo ...............................1 2 4
8.4 Conclusão ...................................1 2 5
iv

## Página 9

CasadoCódigo Sumário
9 Vo and ocom a gravidade! 127
9.1 UsandooAcelerômetro . . . . . . . . . . . . . . . . . . . . . . . . . . . 128
9.2 Controlandoainstabilidade . . . . . . . . . . . . . . . . . . . . . . . . 136
9.3 Calibrandoapartirdaposiçãoinicialdoaparelho. . . . . . . . . . . . 137
9.4 Desafioscomoacelerômetro . . . . . . . . . . . . . . . . . . . . . . . . 139
9.5 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139
10 Te l afinal e game over 141
10.1 Telafinal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
10.2 TelaGameOver . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145
10.3 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 148
11 Pausando o jogo 149
11.1 Montandoateladepause. . . . . . . . . . . . . . . . . . . . . . . . . . 150
11.2 ControlandooGameLoop. . . . . . . . . . . . . . . . . . . . . . . . . 152
11.3 Adicionandoobotãodepause. . . . . . . . . . . . . . . . . . . . . . . 154
11.4 Ainterfaceentrejogoepause . . . . . . . . . . . . . . . . . . . . . . . 156
11.5 Pausandoojogo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157
11.6 Pausandoosobjetos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 161
11.7 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163
12 Continuando nosso jogo 165
12.1 Utilizandoferramentassociais . . . . . . . . . . . . . . . . . . . . . . . 165
12.2 Highscore. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 166
12.3 Badges. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 167
12.4 Desafiosparavocêmelhorarojogo . . . . . . . . . . . . . . . . . . . . 168
12.5 Comoganhardinheiro?. . . . . . . . . . . . . . . . . . . . . . . . . . . 169
12.6 Conclusão. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170
v

## Página 11

Capítulo1
Intro duçãoaodesenvolvimentode
jogosnoAndroid
RiverRaid,paraAtari,foiprovavelmenteoprimeirojogodevideogamequejoguei.
Nesseclássicogameda Activisioncriadoem1982,ojogadorcontrolavauma
navequesemoviadebaixoparacimanatela,ganhandopontospormatarinimigos,
destruirhelicópteros,navesebalões.Emais:erapossívelencherotanquepassando
porestaçõesdegás.

## Página 12

CasadoCódigo
Figura1.1:RIVERRAIDnoAtari
Incrívelcomoumdesenhosimplese2Dpodiasertãodivertido. Controlara
nave,fazerpontosepassarporobstáculosmegarantiamhorasdediversão.
Comopassardotempo,novosjogosforamsurgindoesetornaramcadavezmais
sofisticados.Apesardetodososconceitosdosjogosantigosteremsidomantidos,um
jogodePlaystation3,porexemplo,podeenvolverdezenasdedesenvolvedores.
Atualmente,comocrescimentodos casual gamers,oscelularesetabletssetor-
naramplataformasdesucessosedisputadas. Comeles,odesenvolvimentodeum
jogonãoprecisamaisdeumaquantidadeenormededesenvolvedores. Umaideia
interessanteebemimplementadapodeserosuficienteparaseujogoobtersucesso.
Sódependedevocê.
2

## Página 13

CasadoCódigo Capítulo1. IntroduçãoaodesenvolvimentodejogosnoAndroid
Figura1.2:CapadojogoRIVERRAIDde1982
1.1 O que você encontrará neste livro
EstelivroéescritoparadesenvolvedoresquejáconhecemalinguagemJavaeobásico
daplataformaAndroid.Eleédivididoem3partesprincipais:
• Umprotótipoinicial
• Umestudodojogoqueserádesenvolvido
• UmjogodesenvolvidocomCocos2D
Aideiaéquesejaumbomguiaparatodosaquelesquequereminiciarnodesen-
volvimentodegames,sejaprofissionalmente,paraevoluirseusconhecimentosou
mesmoporpuradiversão.
3

## Página 14

1.1. Oquevocêencontraránestelivro CasadoCódigo
Um protótipo inicial
Noiníciodolivro,serádesenvolvidoumjogosimples,programadocomapenas
2classes. Oobjetivoésefamiliarizareterumano çãogeraldosconceitosbásicos
nodesenvolvimentodegames.Essesconceitosaparecememquasetodososjogos,
sejamelessimplesouavan çados.
Nessecapítulonãoseráutilizadonenhumframeworkdedesenvolvimento,ape-
nasAndroidpuro. Mesmoassim,chegaremosaumresultadobeminteressante,
comoesse:
Figura1.3:Imagemdonossoprotótipo.
Ocódigodonossoprotótipopodeserencontradoaqui:
https://github.com/andersonleite/jogos_android_prototipo
4

## Página 15

CasadoCódigo Capítulo1. IntroduçãoaodesenvolvimentodejogosnoAndroid
Um estudo do jogo que será desenvolvido
Programaçãoéapenasumapartedodesenvolvimentodegames.Empresasfoca-
dasemdesenvolvimentodejogospossuemroteiristasparacriarahistóriadosgames,
designersparadefiniromelhorvisualdojogo,profissionaisdesomparaatrilhaso-
noraeefeitos,designersdeinterfaceparadefinircomoseráaexperiênciadojogador
nogame,entreoutros.Omarketingedivulga çãosãocasosàparte.
Teremosumcapítuloespecialparaplanejarumpoucoahistóriadojogo,deter-
minarastransi çõesdetelaeestudarovisualdojogoaserdesenvolvido,queserá
nessadireção:
Figura1.4:14bisVS100Meteoros
5

## Página 16

1.1. Oquevocêencontraránestelivro CasadoCódigo
Tambémveremosumpoucosobrecomodeixarojogovicianteepoderganhar
dinheirocomitens,missõeseupgrades.
Um jogo desenvolvido com Cocos2D
Quandoosprincipaisconceitosjátiveremsidopassadoseahistóriaeplaneja-
mentodojogofinalizada,iniciaremosodesenvolvimentodonossojogoprincipal.
Paraele,utilizaremosumframeworkchamado Cocos2D,quefacilitaeotimizadi-
versasquestõesusuaisnodesenvolvimentodejogos.
Figura1.5:14bisVS100Meteoros
OcódigodojogocomCocos2Dcompletoestáaqui:
https://github.com/andersonleite/jogos_android_14bis
6

## Página 17

CasadoCódigo Capítulo1. IntroduçãoaodesenvolvimentodejogosnoAndroid
EojogopodeserinstaladonoseuAndroidpelaGooglePlay:
https://play.google.com/store/apps/details?id=br.com.casadocodigo.bis
Grupo de Discussão
Existeumgrupodediscussãofocadoexclusivamenteparaosexemplosqueserão
desenvolvidosaqui. Casovocêtenhadúvidasemalgumpasso,oumesmovenhaa
implementarmodificaçõesecriaroseuprópriojogocomoqueaprendeu,compar-
tilhe!
https://groups.google.com/group/desenvolvimento-de-jogos-para-android
VocêtambémpodeutilizaroforumdoGUJpararesolverdúvidas:
http://www.guj.com.br/
1.2 Q ue comece a diversão!
Estelivrovaitedarabaseparacriarumjogo!Vocêsaberáporondecome çareterá
osprincipaisconceitoseaformadepensarnecessáriaparadesenvolverumgame2D
aofinaldessaleitura.Apartirdisso,éasuaprópriacriatividadeedetermina çãoque
poderãofazerdassuasideiasonovojogodesucessonomundodosgames!
7

## Página 19

Capítulo2
Protótipodeumjogo
Vamoscomeçaradesenvolverumjogo! Esteseráumcapítulofundamentalpara
todoolivro,focadoemconceitosimportantes,ilustrandocommuitaprática.Nele
percorreremosasprincipaisetapasqueprecisamosteremmenteaodesenvolverum
jogo.
Comosconceitosdessecapítulopoderemosdesenvolverjogosbeminteressan-
tes,porém,oobjetivoagoraéexplorarmosasmecânicasportrásdosgamesesermos
apresentadosàformadepensarnecessária.
Parapercorreressecaminho,inciaremoscriandoumprotótipo.Criarumpro-
tótiposerábompelasseguintesrazões:
• Conseguiremosumrápidoentendimentodavisãogeralnecessáriaparade-
senvolverumgame.
• Nãoprecisaremosnospreocuparcomcriardiversastelasqueumjogopode
ter,permitindofocarapenasnosconceitosimportantes.

## Página 20

CasadoCódigo
• Permitiráentraremdetalhesmaiscomplexosquandodefatoiniciarmosnosso
game.
Nossoprotótipoteráasfuncionalidadesbásicasencontradasnosgames,vamos
conhecerosobjetivos.
Funcionalidades do protótipo
Penseemumjogo2DtradicionalcomoSuperMarioBrosoumesmoStreetFigh-
ter. Elespossuemumasériedesemelhan ças. Emambosvocêcontrolaalgumele-
mento,quepodemoschamardePlayer. Oplayerrecebealgumtipodeestímulo
(i n p u t)paraexecutarmovimentosnatela,comoteclado,joystickoumouse.Apósos
inputsoplayerpodeganharpontossealgoacontecer,normalmenteassociadoaen-
costaremoutroobjetodojogo,oquefazcomquealgumplacarsejaatualizado.Em
determinadomomentooplayerpodeganharouperderojogo,pordiversosmotivos,
comosuperarumtempo,ultrapassarumamarcadepontosouencostaremalgum
outroobjetodogame.
Essassãoasmecânicasbásicasdequalquerjogo. Penseemoutrojogocomas
característicassemelhantesetentefazeresseparalelo.Noprotótipoquecriaremos
nessecapítulo,implementaremosessasmecânicas,entendendocomodesenvolvê-
lasemumaplicativoAndroid.
Nossojogoteráasseguintesfuncionalidades:
• Umplayerqueserárepresentadoporumacircunferênciaverde,posterior-
mente,anave.
• Moveroplayerdeacordocomumestímulo,nocaso,otoquenatela(input).
• Uminimigoqueserárepresentadoporumacircunferênciaqueaumentará
comopassardotempo.
• Umplacarqueseráatualizadodeacordocomotemponoqualoplayernãoé
capturadopeloinimigo.
• GameOverquandooinimigoencostarnoplayer
• Opçõesderestarteexit
Aofimdessecapítulo,teremosoprotótipoabaixo.
10

## Página 21

CasadoCódigo Capítulo2. Protótipodeumjogo
Figura2.1:Imagemdojogo.
Temosmuitoparapercorrernesseprotótipo. Reparequeaoentenderalógica
portrazdeumjogo,poderemoscriarqualquertipodegame.Vamosaoprotótipo!
2.1 I niciando o projeto
VamosiniciarcriandoumprojetocomumdeAndroid.Comovocêjácrioualgum
aplicativoAndroid,perceberáqueoprocedimentoéomesmo.Nãoénecessáriocon-
figurarnadaespecíficoparajogosaocriaroprojeto.Lembre-sequevocêprecisater
oEclipseeoSDKdoAndroidinstalados,quepodemserbaixadosrespectivamente
em:
http://www.eclipse.org/http://developer.android.com/sdk/
11

## Página 22

2.1. Iniciandooprojeto CasadoCódigo
PelapáginadedesenvolvedoresdoAndroid,háapossibilidadedebaixarum
bundlequejátrazoEclipsejuntoaoplugin,numúnicodownload.
EsseéumlivrofocadoemquemjáconheceobásicododesenvolvimentoAn-
droid,masmesmoassimpassaremospassoapassoemalgunspontoserevisaremos
conceitoschave,parafacilitarseuacompanhamento.
No Eclipse vá emFile acesse as opçõesem New e selecione Android
Application Project.Criaremosumprojetochamado Impossible.Porqueesse
nome?Sevocêreparounalistadefuncionalidades,nossoprotótiponuncatemum
finalfeliz!
Coloqueonomedopacotecomo br.com.casadocodigo.impossible:
Figura2.2:Criandooprojeto.
Nopasso2,deixeselecionadasasop çõespadrão.
12

## Página 23

CasadoCódigo Capítulo2. Protótipodeumjogo
Figura2.3:Configura çõesopcionais.
Damesmaforma,mantenhaasop çõespadrãonaterceiratela.
13

## Página 24

2.1. Iniciandooprojeto CasadoCódigo
Figura2.4:Configura çõesopcionais.
Naquartatela,selecioneaop ção BlankActivity.
14

## Página 25

CasadoCódigo Capítulo2. Protótipodeumjogo
Figura2.5:Configura çõesopcionais.
NaúltimatelacrieaActivitycomname Gameecliqueem Finish.
15

## Página 26

2.1. Iniciandooprojeto CasadoCódigo
Figura2.6:Configura çõesopcionais.
Opcional: Configurando o Emulador
V o c ê t e m a o pçãoderodarosprojetosdolivroemumaparelhocomAndroid
ouutilizandooemuladordoEclipse. Éfortementerecomendadoquevocêutilize
umaparelho,poisutilizaroemuladorpodeserbemlento,alémdenãodisporde
funcionalidadescomooacelerômetroqueutilizaremosmaisparafrente.
Paraconfigurarumnovoemulador,noEclipseselecioneomenu Windowede-
pois Android Virtual Device Manager .
16

## Página 27

CasadoCódigo Capítulo2. Protótipodeumjogo
Figura2.7:Configurandooemulador.
Vocêdeveveratelaaseguir:
Figura2.8:Configurandooemulador.
17

## Página 28

2.1. Iniciandooprojeto CasadoCódigo
Cliqueem Neweconfigureoemuladorcomascaracterísticasabaixo:
Figura2.9:Configurandooemulador.
Aorodaroprojetoutilizandooemulador,clicandocomobotãodadireitano
projeto, R u n A seescolhendo Android Application.Vocêteráumatelacomoessa:
18

## Página 29

CasadoCódigo Capítulo2. Protótipodeumjogo
Figura2.10:Configurandooemulador.
Verificando o projeto
Nessemomentotemosoprojetoiniciado.Vocêjápodeexecutá-lo:cliquecom
obotãodadireitanele, R u n A seescolha Android Application.Aoexecutá-lo,atela
doemuladordeveapresentaralgoassim:
19

## Página 30

2.2. Criandoabasedojogo CasadoCódigo
Figura2.11:Verificandooprojeto.
Vamosfazeresseprimeirojogoutilizandoposi çõesfixasdeXeY.Paraquevocê
obtenhaoresultadocorretonesseprimeirocapítulo,certifique-sedeescolherum
dispositivocomlarguraealturagrandedetela.Noscapítulosposterioresaprende-
remosalidarcomachamadafragmenta çãodoAndroid,possibilitandorodarojogo
emdispositivosdediversostamanhosdetela.
2.2 C riando a base do jogo
Horadecome çar!Paraesseprotótipotentaremosmanterascoisassimplesediretas,
semprepensandoemaplicarosconceitosnecessáriosparacriarojogonospróximos
capítulos.
Teremosapenasduasclasses. Umaactivity,naqualconfiguraremosasop ções
voltadasasconfigura çõesdoAndroideumaclassequeteráalógicadojogo.
ÉbemcomumqueatelainicialdequalquerjogoemAndroidsejaumaActivity,
emqueteremosasconfigura çõesiniciaiscomodeterminarostamanhosdetela,de-
20

## Página 31

CasadoCódigo Capítulo2. Protótipodeumjogo
finiroqueocorrequandoousuáriodapauseoumesmoqueprocessosdevemser
paradosquandoousuáriosairdojogo.
Alógicadeumjogonormalmenteédivididaemdiversasclasses. Aquiaori-
entaçãoaobjetosefazrealmentenecessáriaparaumboautiliza çãodoselementos
dogame. Nesseprimeirocapítulo,manteremosascoisassimples,concentrandoa
lógicaemapenasumaclasse.Nospróximoscapítulos,quandojátivermospassado
pelosconceitosimportantes,definiremosaarquiteturadonossojogo,assimcomo
dividiremosasresponsabilidadesemdiversasclasses.
Game Activity
Aactivity Gamecomeçarásimples.Essaclasseéaportadeentradadonossojogo,
porondeidentificamosascaracterísticasdeaplicativosAndroid,como inputsdo
usuário. VamosremoveroqueoEclipsegeroudecódigopadrãoedeixaraclasse
assim:
package br.com.casadocodigo.impossible;
import android.app.Activity;
import android.os.Bundle;
public class Game extends Activity {
@Override
protected void onCreate(Bundle savedInstanceState ) {
super.onCreate(savedInstanceState);
}
}
Vocêpode,opcionalmente,usaratelacheiadoaparelho( Fullscreen)adicio-
nandoasop çõesabaixonométodo onCreatedaGameActivity:
requestWindowFeature(Window.FEATURE_NO_TITLE);
getWindow().setFlags(
WindowManager.LayoutParams.FLAG_FULLSCREEN,
WindowManager.LayoutParams.FLAG_FULLSCREEN);
A lógica do Impossible: criando um loop infinito
Aclassequeconteráalógicasechamará Impossible.Essaclassedeveherdar
de SurfaceView,ealémdissoimplementar Runnable.Dessaformapoderemos
21

## Página 32

2.2. Criandoabasedojogo CasadoCódigo
executaralógicadojogoemumathreadseparadaeanalisarqualquerestímulo,como
porexemplo,osinputvindospelotoquenatela.
package br.com.casadocodigo.impossible;
import android.content.Context;
import android.view.SurfaceView;
public class Impossible extends SurfaceView implements Runnable {
public Impossible(Context context ) {
super(context);
}
@Override
public void run() {
// TODO Auto-generated method stub
}
}
No Androidumobjetodotipo SurfaceViewpermitequedesenhossejam
executadossobreasuperfícieemvezdetrabalharcomumXMLdeapresenta ção.
Agoraquejátemosa Activity Game,queéaportadeentrada,eaclasse
Impossible,querepresentaalógicadojogo,vamoscriarolinkentreelas. Para
isso,naactivity Gameiniciaremosumavariáveldalógicadojogo,quechamaremos
de view.Alémdisso,passaremosessavariávelnométodo setContentView()
da Game Activity,pararenderizá-la.
package br.com.casadocodigo.impossible;
import android.app.Activity;
import android.os.Bundle;
public class Game extends Activity {
Impossible view ;
@Override
protected void onCreate(Bundle savedInstanceState ) {
super.onCreate(savedInstanceState);
22

## Página 33

CasadoCódigo Capítulo2. Protótipodeumjogo
// Lógica do jogo
view = new Impossible(this);
// Configura view
setContentView(view);
}
}
Poderodarseuprojetonovamente,masaindanãotemosbonsresultados!Parece
queumjogoaindaestálongedeseconcretizar,masatéofinaldocapítulovocêjá
teráumprotótipoparamostrar.
G a m e Lo o p
Normalmente os jogos têm um primeiro conceito importante:um loop
infinito,conhecidocomo game loopou main loop.
Ojogoéumasériedeintera çõesnesseloopinfinito. Nele,ojogodefineposi-
çõesdeelementos,desenha-osnatela,atualizavalorescomoplacar,verificacolisões
entreelementos.Issotudoérealizadodiversasvezesporsegundo,emquecadatela
desenhadaéchamadadeframe.Umaboaanalogiasãoosdesenhosfeitosemblo-
cosdepapel,ondecadadesenho( fr a me)éumpeda çodaanima ção.Aopassartudo
rapidamentetemosaimpressãodemovimento.
23

## Página 34

2.2. Criandoabasedojogo CasadoCódigo
Figura2.12:Desenhoanimadoemblocodepapel.
Esseconceitoéextremamenteimportantee,comopassardotempo,difícilde
lidarnodesenvolvimentodeumjogo. Comváriosobjetostendodiversaspossibi-
lidadesnatelaachancedeperderocontroleégrande.Porisso,tentesemprecriar
métodospequenos,compoucaresponsabilidade.Dessaforma,encontraroquepode
estarerradoficamuitomaisfácil.
Vamoscolocaronossoloopinfinitodentrodo rundaclasse Impossible:
public class Impossible extends SurfaceView implements Runnable {
boolean running = false;
Thread renderThread = null;
public Impossible(Context context ) {
super(context);
}
@Override
public void run() {
while(running) {
24

## Página 35

CasadoCódigo Capítulo2. Protótipodeumjogo
System.out.println("Impossible Running...!" );
}
}
}
Masinicialmenteesse boolean running éfalso. Quemvaideixá-lo true
ecriarumathreadparaexecutaronosso Runnable? Vamoscriarumtrechode
códigodentrodaprópriaclasse Impossible.Jáprevendofuturaspausasdojogo,
daremosonomede resumeaestemétodo.Adicionenaclasse:
public void resume() {
running = true;
renderThread = new Thread(this);
renderThread.start();
}
Virouoproblemadoovoedagalinha. Queminvocaessemétodo? Devemos
fazerissologonoiníciodaaplica ção.
Apósocarregamentobásicodaactivitynométodo onCreate,oAndroid,por
causadociclodevidadaactivity,invocaométodo onResume. Vamosinvocaro
resumedanossa Impossiblenessemétododaactivity Game:
protected void onResume() {
super.onResume();
view.resume();
}
Rodeoprojetonovamente. Temosnossaprimeirasaída,aindanãomuitoem-
polgante.Oconsoleimprime Impossible Running...! interminavelmente.
2.3 D esenhando o objeto principal
Omotordonossojogojáestáligado,funcionandoatodovapor,porémnadaacon-
tecenatela.Nossopróximopassoserádefiniroobjetoprincipal,quechamaremos
dePlayer.Nossoplayerserábemsimples,apenasumelementográfico,nocasoum
círculo. Podeparecersimplesmasjogos2Dsãoobjetostriviaisquesãoanimados
muitasvezesporsegundo. Nonossocasotemosumcírculo,maspodemostrocar
porqualquerrecursoouimagemmelhortrabalhadoparadefinirumpersonagem
interessante.
25

## Página 36

2.3. Desenhandooobjetoprincipal CasadoCódigo
Comapopulariza çãodossmartphonesedosjogoscasuais,essetipodeplayer
simplesdejogos2Dreapareceucommuitafor ça.Onomeatribuídoaessesobjetos
é Sprite,quenadamaissãoqueimagens,normalmenteretangularesoumesmo
quadradas,comfundostransparentes.
Vocêpodeencontrar Spritesdediversosjogosclássicosnainternet.Procure
nogooglepor‘sprites’maisonomedeumjogoquevocêgoste.Comeceaimaginar
comoessejogofuncionacomoquefalamosatéaqui.
Figura2.13:SpritesdofamosoMarioBros.
Utilizando Android Canvas, Paint e a SurfaceView
ParadesenharelementosnateladojogonoAndroid,temosalgumasop ções.
Quandodesenhamosnavidareal,precisamosdeferramentascomopincéiseum
lugarparautilizá-las,comopapeloutelas.Oelemento CanvasnoAndroidrepre-
sentaessatela,naqualpodemosdesenhardiversasformasoumesmoSprites.Para
teracessoaesseelemento,podemosdeclararnossaclassecomosendoumatela,por
meioda SurfaceView.
Aoutilizaruma SurfaceView,temosumtipode Viewespecializadoemde-
26

## Página 37

CasadoCódigo Capítulo2. Protótipodeumjogo
senharnatela.Oprincipalpropósitoda SurfaceViewéforneceroqueprecisamos
paraqueumasegunda Threadpossarenderizarasatualiza çõesdojogoatodomo-
mento.Aúnicarestri çãoaoutilizaressaclasseésecertificardequeessasuperfície
outelajáestápreparadaparareceberosdesenhos. Paraessaverifica çãopodemos
utilizaro SurfaceHolder.
Paradesenharvamosusaraclasse Paint.Comelaconseguiremosdefinirele-
mentoscomotextos,linhas,figurasgeométricas,coresetudoqueforreferentea
colocaroselementosdojogonatela.Inicializaremostambémumavariáveldotipo
SurfaceHolder,queutilizaremoslogoemseguida.
Vamos começar configurando nossos primeiros elementos na classe
Impossible,declarandodoisatributosepopulando-osnoconstrutor:
SurfaceHolder holder ;
Paint paint ;
public Impossible(Context context ) {
super(context);
paint = new Paint();
holder = getHolder();
}
Eentãopodemoscriara Threadqueteráacessoaoselementosnecessáriospara
renderizarastelasdojogo. Reparequeaquiverificamosseasuperfíciejáfoipre-
parada,einiciaremososdesenhosnocanvas. ImportanteperceberqueoCanvas
devesersempretravadoedestravadoacadarenderiza ção,dessaformanãotemos
oefeitode flickeringnaanimação,comoqualficavisívelospassosintermediários
dela(apagatela,redesenhacadaelemento,etc).
Alémdisso,comoa SurfaceViewnecessitaquearenderiza çãodosdesenhos
nocanvassejafeitaporumaoutra Thread, oSurfaceHolderpodenosajudara
verificarseatelajáestáprontaepreparadaparareceberosframesdojogo.
public void run() {
while(running) {
// verifica se a tela já está pronta
if(!holder.getSurface().isValid())
continue;
// bloqueia o canvas
Canvas canvas = holder.lockCanvas();
27

## Página 38

2.3. Desenhandooobjetoprincipal CasadoCódigo
// desenha o player
// o que fazer aqui??? já vamos aprender
// atualiza e libera o canvas
holder.unlockCanvasAndPost(canvas);
}
}
Finalmentevamosdesenharoplayer! Utilizaremosnossospincéis,nocaso,a
classe Paint.Paranãodeixarométodo runmuitolongo,vamoscriarumoutro
método:
private void drawPlayer(Canvas canvas ) {
paint.setColor(Color.GREEN);
canvas.drawCircle(100, 100, 100, paint);
}
Agorabastainvocarométodo drawPlayerdedentrodonosso run.Repare
quesóprecisamosalterarumaúnicalinha,aqueestavacomumcomentário:
public void run() {
while(running) {
// verifica se a tela já está pronta
if(!holder.getSurface().isValid())
continue;
// bloqueia o canvas
Canvas canvas = holder.lockCanvas();
// desenha o player
drawPlayer(canvas);
// atualiza e libera o canvas
holder.unlockCanvasAndPost(canvas);
}
}
Rodenovamenteoseuprojeto.Obtivemosnossoprimeiroresultado!
28

## Página 39

CasadoCódigo Capítulo2. Protótipodeumjogo
Figura2.14:PlayernoCanvas.
2.4 C aptando os comandos do usuário e movendo
objetos
Existemdiversasmaneirasdeinteragircomumjogoecomoplayerprincipal.Mover
omouseeclicar,utilizaroteclado,tocaratelaoumesmocapturaromovimento
deumaparelho,usandoporexemplo,oacelerômetro. Noprotótipo,utilizaremos
otoquenatelaparamoveroplayer. Vamoscapturarcadatoquecomosendoum
inputsdousuário,e,acadavezqueissoocorrer,iremosdarumcomandoaonosso
jogo.
NessemomentovamosexploraresseconceitodeinputsdousuárionoAn-
29

## Página 40

2.4. Captandooscomandosdousuárioemovendoobjetos CasadoCódigo
droid, e novamente reparar na importância da Activity principal como porta
de entrada do jogo. Utilizaremos uma interface do próprio Android chamada
OnTouchListener,quetemométodo onTouchaserimplementado. Todavez
queumtoquefordetectado,oAndroidochama,passandoascoordenadastocadas
nasuperfíciedatela.Edepossedessascoordenada,podemostomara çõessobreos
objetosnateladojogo.
Nessemomento,aodetectarumtoque,moveremosparabaixonossoplayer.Re-
parequeaqui,poderíamosutilizarainforma çãoquerecebemosparatomara ções
interessantesnojogo,comomoverparaumladoouparaououtro,movermaisrá-
pido,etc. Parafimdeentendimentodeconceitoeprototipa ção,seremossimples
nessaimplementação.
Antesdemaisnada,precisamossaberemqueposi çãonossoplayerestá.Declare
oatributo playerYno Impossible:
private int playerY = 300;
E,todavezqueinvocaremo drawPlayer,vamosdesenhá-lonessaaltura,em
vezdaquelenúmerofixo.Altere:
private void drawPlayer(Canvas canvas ) {
paint.setColor(Color.GREEN);
canvas.drawCircle(300, playerY, 50, paint);
}
Eteremosummétodoquepodeserinvocadoparamoveroplayerparabaixo(a
teladoAndroidpossuiaposi ção 0,0nocantosuperioresquerdo):
public void moveDown(int pixels) {
playerY += pixels;
}
publicclassGameextendsActivityimplementsOnTouchListener{...}[/code]
Aclassenãovaicompilarpoisestáfaltandoométododecallback, queéo
onTouch.ValelembrarqueoEclipsefacilmenteescreveaassinaturadessemétodo
pravocê,clicandonobotãodequickfix(éalâmpadaamarelaaoladodalinhado
erro).Vamosimplementá-lo:
@Override
public boolean onTouch(View v, MotionEvent event) {
view.moveDown(10);
30

## Página 41

CasadoCódigo Capítulo2. Protótipodeumjogo
return true;
}
PrecisamosavisaroAndroiddequegostaríamosdereceberosinputsdetouch.
Nãobastaimplementarainterface OnTouchListener.Vamos,no onCreateda
Game,avisaraoAndroidquequeremosreceberessasnotifica çõesdaviewdentroda
própriaclasse Game:
@Override
protected void onCreate(Bundle savedInstanceState ) {
super.onCreate(savedInstanceState);
// Lógica do jogo
view = new Impossible(this);
view.setOnTouchListener(this);
// Configura view
setContentView(view);
}
Reparequeondeolistenervaificaréumadecisãodedesigndoseucódigo.Por
organização,poderíamostercriadoumaclasseespecíficaparalidarcomosinputs
dodispositivo.
Rodeojogo. Algojádeveocorreraotocarnatela. Nossoplayerdevetersua
posiçãoalterada. Mastemosumproblema,vejacomooplayersemovimentaeo
queacontececomatela:
31

## Página 42

2.4. Captandooscomandosdousuárioemovendoobjetos CasadoCódigo
Figura2.15:Playermovendonocanvas,mastemosumproblema.
Importante: Limpando a tela
Lembradarela çãodeumjogocomosdesenhosemblocosdepapel?Oquedáa
impressãodemovimentoemumblococomoesseéquecadaimagemédesenhada
comumapequenavaria çãodesuaposi çãoanterior.Nenhumdesenho,sevistoin-
dividualmente,daaimpressãodemovimentooucontinuidadedodesenhoanterior.
Écomosecadapapeldoblocofossetotalmenteredesenhadoacadaframe.
Oquefaremosparaqueoplayersemovanatelaézeraratelatodavezque
formosrenderizarumnovoframe.Comonossoprotótipoésimplesenãotemum
fundocomimagenssemovendo,podemosapenasiniciaroframecomumfundo
preto.Parajogoscombackgroundsmaiscomplexosaestratégiadelimparatelaserá
32

## Página 43

CasadoCódigo Capítulo2. Protótipodeumjogo
maiscomplexa.
Na classeImpossible,altereométodo runparapintarateladepreto,adici-
onandoalinha canvas.drawColor(Color.BLACK):
// bloqueia o canvas e prepara tela
Canvas canvas = holder.lockCanvas();
canvas.drawColor(Color.BLACK);
Rodeagoraetoquenatela.Acadatoqueseuplayersemoverá!
2.5 C riando o inimigo
Chegamosàparteperigosa!Sãoosinimigosquefazemumjogosermaisdesafiador,
quenosinstigamasuperaralgo.Oinimigoemumjogopodeestarrepresentadode
diversasmaneiras.Podeserotempo,podeserumalógicacomplexaaserresolvida
oumesmooutrosobjetosepersonagens.
Apartirdosinimigospodemosconhecerdiversosconceitosimportantespara
umjogofuncionar.Assimcomooplayerprincipal,osinimigospossuemseuspró-
priosmovimentos,porém,diferentedoplayer,osmovimentosdoinimigocostumam
serdefinidosporlógicasinternasdojogo.Ointeressanteéque,pormaisqueosin-
putsdousuárionãodeterminemdiretamenteomovimentodoinimigo,quantomais
inteligenteelefordeacordocomamovimenta çãodoplayer,maisinteressanteede-
safiadorpodeserojogo.
Paraoprotótipodojogo,nossoinimigoseráumoutrocírculo,porém,como
faladoacima,essecírculoterásuapróprialógica. Elecrescerácomotempo,ou
seja,deacordocomopassardojogo,seuraioiráaumentandoeconsequentemente,
ocupandocadavezmaisaregiãodojogo.
Vamoscriar,naclasse Impossible,umavariávelquerepresentaoraiodoini-
migo:
private float enemyRadius;
Assimcomotemosummétodoseparadoquedesenhaoplayer,teremosumque
desenhaoinimigo.Sóquenessecasoespecial,queremosqueacadanovoframe,o
raiodoinimigocres çaem1:
private void drawEnemy(Canvas canvas ) {
paint.setColor(Color.GRAY);
enemyRadius++;
33

## Página 44

2.5. Criandooinimigo CasadoCódigo
canvas.drawCircle(100, 100, enemyRadius, paint);
}
Altereoseu runeincluaainvoca çãoparadesenharoinimigo:
// desenha o player e o inimigo
drawPlayer(canvas);
drawEnemy(canvas);
Aorodarojogo,nossoinimigocrescesozinhoeoplayerseafastacomotouch
natela!
Figura2.16:Playeraparecenatela.
Nessemomentoconseguimosmoveroplayerprincipaletentarseafastardoini-
34

## Página 45

CasadoCódigo Capítulo2. Protótipodeumjogo
migoquecrescecadavezmaiscomopassardotempo.Agoraprecisamosdetectara
colisão!
2.6 D etectando colisões e mostrando resultados
Jápassamospeloconceitodemoverobjetos,nocaso,pelotoquenatelaejátambém
porterumoutroobjetoquerepresentaoinimigoetemsuaprópriainteligência.
Agra çadojogoagoraéconseguiridentificarquandoumadeterminadasitua ção
acontece,situaçãoessaqueoplayerestá“lutandocontra”.
Nonossocasooplayernãopodeencostarnocírculoquecrescecadavezmais.
Reparequeaquiaindanãotemosumahistóriaparaqueessacolisãofa çarealmente
sentidoemserevitadanojogo,porém,éaiqueaimagina çãofazojogosetornar
divertido. Jogosantigos,em2D,nãopossuíamgráficosincríveis,massim,ideias
interessantesrepresentadasporobjetossimplesnatela.
Nonossocaso,poderíamosestardesenvolvendoumjogonoqualoplayerestá
fugindodealgo.Umexemplo,umvulcãoentrouemerup çãoenossoherói(player)
devesalvaroshabitantesdessavila. Ouseja,sabendoosconceitos,iremosincre-
mentarovisualparaquerepresenteumahistóriainteressante.
Detectando colisões
Precisamosentãoreconhecerqueocirculomaior,querepresentaoinimigo,con-
seguiuencostarnocirculomenor,movidopelousuário,querepresentaoplayer.De-
tectarcolisõeséumassuntomuitoamplo. Existemdiversostiposdedetec çãode
colisõespossíveis.
Umamaneirabemtradicionaléconsiderarquecadaelementoéumquadrado
ouretângulo,verificaratravésdegeometriaseumelementosobrepõeooutro.Essa
formaconsideramesmoelementosquenãocontornamumobjetocomopartedo
mesmo.Naimagemabaixo,umanavedejogosdetiro.Paradetectarquealgocolide
comela,aáreaanalisadapodesergeneralizadaparaumquadradoaoredordela.
35

## Página 46

2.6. Detectandocolisõesemostrandoresultados CasadoCódigo
Figura2.17:Regiãodetectadapelojogo.
Pode-sequestionarseessemétodoébom.Seráque,sealgoencostarnaquinado
quadrado,quenãofazpartedanave,umacolisãoserádetectada?Emmuitoscasos
essaaproximaçãoéfeitapordoismotivos.
• Simplificaçãoparadetectaracolisão.
• Menorexigênciacomputacional.
Simplificaradetec çãoporcontadesimplificaroalgoritmodacolisãoéumaprá-
ticabemcomum,alémdisso,ébemmaisbaratocomputacionalmentedoqueterque
analisarcadarealitemdeumaimagemdeumplayer.
Colisões no protótipo
Chegamosaumdosconceitosmaisimportantesnodesenvolvimentodeum
game! Precisamosidentificaracolisãoentreoplayereoinimigo. Esseéoitem
36

## Página 47

CasadoCódigo Capítulo2. Protótipodeumjogo
chavedonossoprotótipoenormalmentenamaioriadosjogos. Existemdiversas
formasdepontuar,emuitasdelasutilizamacolisãoentredoisoumaisobjetospara
isso. Jogosdetiropontuampelacolisãodotirocomoobjetoatirado. Jogoscomo
SuperMarioBroseStreetFighterpontuampelascolisõesdoplayercommoedasou
cominimigos.
Existemdiversasformasdedetectarcolisões,algumasmaiscomplexasoutras
maissimples.Paraonossoprotótipo,utilizaremosacolisãodeduascircunferências.
Acolisãodedoiscírculoséumadasmaissimples,porém,érelacionadaaalguns
conceitosmatemáticoscomoo Teorema de Pitágoras .
Figura2.18:TeoremadePitágoras.
Nafiguraanterior,existeumamaneirasimplesmatematicamentededeterminar
37

## Página 48

2.6. Detectandocolisõesemostrandoresultados CasadoCódigo
seascircunferênciasestãosobrepostas.Precisamosidentificarosvaloresaseguir:
• Somadosraiosdasduascircunferências
• Valordahipotenusa,oudistânciaentreosdoisraios
Depossedasduasinforma çõesacima,conseguimosidentificarseasomados
raiosémaiorqueahipotenusagerada.Seformaior,nãoexistecolisão.
Vamosaocódigo!
Primeirocriaremosalgumasvariáveisparaessecálculo.Asvariáveissereferem
àsposiçõesXeYdeambasascircunferências,tantodoplayerquantoadoinimigo.
Ahipotenusaseráchamadade distance.Tambémteremosmaisumavariável, game-
o v e r,casoacolisãosejadetectada.
Altere sua classeImpossible para ter todos esses atributos. Repare que
enemyRadiuse playerYjápossuíamos:
private int enemyX, enemyY, enemyRadius = 50;
private int playerX = 300, playerY = 300, playerRadius = 50;
private double distance;
private boolean gameover;
Refatoreosmétodoscriadosanteriormenteparaqueutilizemasvariáveisque
foramcriadas:
private void drawEnemy(Canvas canvas ) {
paint.setColor(Color.GRAY);
enemyRadius++;
canvas.drawCircle(enemyX, enemyY, enemyRadius, paint);
}
private void drawPlayer(Canvas canvas ) {
paint.setColor(Color.GREEN);
canvas.drawCircle(playerX, playerY, 50, paint);
}
Ométodoqueidentificaacolisãosegueamatemáticaquejávimoseutilizaa
classe Mathpararaizepotencia ção.
private void checkCollision(Canvas canvas ) {
// calcula a hipotenusa
38

## Página 49

CasadoCódigo Capítulo2. Protótipodeumjogo
distance = Math.pow(playerY - enemyY, 2)
+ Math.pow(playerX - enemyX, 2);
distance = Math.sqrt(distance);
// verifica distancia entre os raios
if (distance <= playerRadius + enemyRadius) {
gameover = true;
}
}
Adicioneachamadaaométodoquedetectaráacolisão,dentrodonossoloopdo
run:
// desenha o player e o inimigo
drawPlayer(canvas);
drawEnemy(canvas);
// detecta colisão
checkCollision(canvas);
Rodeojogo,oqueacontecequandohouvercolisão? Nada! Poisapenasmu-
damosavariável gameoverpara true.Precisamosverificarissoemnossoloop!
Devemosconfirmarseojogoterminou,nãoapenaschecaracolisão:
// desenha o player e o inimigo
drawPlayer(canvas);
drawEnemy(canvas);
// detecta colisão
checkCollision(canvas);
if(gameover) {
break;
}
Ecomissosaímosdomainloop,congelandoatelaeoprocessamentodosobje-
tos.Testeojogo!
Seriamaisbonitoumgameovermaisconvincente,não?Vamoscolocarnatela
umamensagemdeGameOver.Crieométodo stopGamequevaiutilizarfun ções
básicasdocanvasqueaindanãovimos.Oobjeto Paintpossuiocontroledecor,
tamanhoeestilo.Utilizaremosométodo drawTextparaescreveramensagem:
39

## Página 50

2.6. Detectandocolisõesemostrandoresultados CasadoCódigo
private void stopGame(Canvas canvas ) {
paint.setStyle(Style.FILL);
paint.setColor(Color.LTGRAY);
paint.setTextSize(100);
canvas.drawText("GAME OVER!" , 50, 150, paint);
}
Agoraaltereo ifdo gameover:
if(gameover) {
stopGame(canvas);
break;
}
Apartirdaqui,ojogojádetectaascolisõeseparaemGameOvercasooinimigo
alcanceoplayer. Essaéumamaneiradesepensaremgamesquefoiutilizadapor
muitotempo. Atualmente,comoavan çodohardwareecomvelocidadesdepro-
cessamentocadavezmaiores,detec çõesdecolisõesmuitomaiscomplexasforam
criadas.
40

## Página 51

CasadoCódigo Capítulo2. Protótipodeumjogo
Figura2.19:Playeraparecenatela.
2.7 A dicionando um placar
Vamosveragoraumpróximoconceitoimportanteparaamaioriadosjogos,aatuali-
zaçãodoplacar.Amaioriadosjogosatualizaalgumaformadepontua çãodetempos
emtempos.Essaatualiza çãodeplacarpodeocorrerdediversasformas,porexemplo
peladetecçãodecolisõesentreobjetos. Noprotótipooplacarserásimples,acada
movimentodoplayerganharemospontos.
Aideiaésimples,acadatoquenatelaoplayerseafastadoinimigoe,comisso,
ganhamospontos.
Crieocampo scorena Impossible,alémdeummétodoqueaumentao
41

## Página 52

2.7. Adicionandoumplacar CasadoCódigo
score:
private int score;
public void addScore(int points) {
score += points;
}
Nométodoquerecebeoeventodetoque,incrementaremosospontos.Atualize
ométodo onTouchdaclasse Game:
view.moveDown(10);
view.addScore(100);
Crieométodo drawScore.Nele,atualizaremosumcamponatelacomovalor
atualdavariável score.
private void drawScore(Canvas canvas ) {
paint.setStyle(Style.FILL);
paint.setColor(Color.WHITE);
paint.setTextSize(50);
canvas.drawText(String.valueOf(score), 50, 200, paint);
}
Nométodo run,apósdetectarofimdojogo,fa çaainvoca çãoao drawscore:
// detecta colisão
checkCollision(canvas);
if(gameover) {
stopGame(canvas);
break;
}
// atualiza o placar
drawScore(canvas);
Ojogodeveestarassim:
42

## Página 53

CasadoCódigo Capítulo2. Protótipodeumjogo
Figura2.20:Playeraparecenatela.
2.8 C riando botões de interface do usuário
Outroconceitoimportanteemjogoséapossibilidadedeinteragircomelementos
deconfiguraçãodogame.Poderpausarojogo,entraremumatelaparamudar,por
exemplo,adificuldadeoumesmofecharesairdojogosãopartesimportantedo
desenvolvimento.
Noprotótipo,ilustraremosesseconceitocomduasop çõesnatela,pararestarte
exit.Simplificaremosparaentenderoconceito,edepois,poderemosconverterpara
botõesmaisinteressantes.
Na classeImpossiblecrieométodo drawButtonsparadesenharoRestart
43

## Página 54

2.8. Criandobotõesdeinterfacedousuário CasadoCódigo
eExit:
private void drawButtons(Canvas canvas ) {
// Restart
paint.setStyle(Style.FILL);
paint.setColor(Color.WHITE);
paint.setTextSize(30);
canvas.drawText("Restart", 50, 300, paint);
// Exit
paint.setStyle(Style.FILL);
paint.setColor(Color.WHITE);
paint.setTextSize(30);
canvas.drawText("Exit", 50, 500, paint);
}
Comosmétodosprontos,fa çaachamadaparadesenharosbotõesnométodo
rundaclasse Impossible.
// atualiza o placar
drawScore(canvas);
// Restart e Exit
drawButtons(canvas);
Agoraprecisaremosdeumaformadereinicializaraspropriedadesdogame.
Aindanaclasse Impossiblecrieométodoquereinicializaasvariáveis. Repare
que,paraorestart,utilizaremosumaabordagemsimplesdereinicializa ção.
Crieométodo initnaclasse Impossible:
public void init() {
enemyX = enemyY = enemyRadius = 0;
playerX = playerY = 300;
playerRadius = 50;
gameover = false;
}
Precisamosagorareconhecerotouchemdeterminadapartedatelaefazera
chamadaparaométodoquecriamos.
Para o botãoExitutilizaremosocomando System.exit(0);quefechao
programa.
44

## Página 55

CasadoCódigo Capítulo2. Protótipodeumjogo
Na Game Activity,verifiquequandoosbotõesrecebemotouchnométodo
onTouch:
@Override
public boolean onTouch(View v , MotionEvent event ) {
if(event.getX() < 100 && event.getY() > 290 && event.getY() < 310) {
view.init();
}
// Exit
if(event.getX() < 100 && event.getY() > 490 && event.getY() < 510) {
System.exit(0);
}
// Incrementa em 10 pixels a posição
// vertical do player e o placar
view.moveDown(10);
view.addScore(100);
return true ;
}
Atelafinaldoprotótipodeveestarassim:
45

## Página 56

2.9. Adicionandomaisvida:imagensdanaveedocéu CasadoCódigo
Figura2.21:Protótipofinal.
2.9 A dicionando mais vida: imagens da nave e do céu
Temostodaalógicadoprotótiporodandoejápodemos,finalmente,alteraralguns
elementosvisuaisparafinalizaroprotótipodojogoefecharosconceitosbásicos.
Vamosdesenharumbackgroundquesimulaumcéuescurocomestrelas.Para
isso,utilizaremosaimagem sky.png.Umpontoimportanteérepararquequanto
maisspritesforemadicionadosaojogo,maisesfor çocomputacional,oquepode
tornarojogomaislento.Maisafrente,utilizaremosframeworksqueotimizamessa
questão.
Adicioneosarquivos sky.pnge nave.pngnodiretório assetsdoprojeto.
46

## Página 57

CasadoCódigo Capítulo2. Protótipodeumjogo
Vamosalteraralgumaslinhasparautilizarasimagens.Nométodo rundaclasse
Impossibleadicioneumalinhaquefuncionarácomobackgrounddogame.
// canvas.drawColor(Color.BLACK);
canvas.drawBitmap(BitmapFactory.decodeResource(getResources(),
R.drawable.sky), 0, 0, null);
Altereométodo drawPlayerpararenderizaraimagemdanave.
private void drawPlayer(Canvas canvas ) {
paint.setColor(Color.GREEN);
canvas.drawBitmap(BitmapFactory.decodeResource(getResources(),
R.drawable.nave), playerX-50, playerY-50, null);
// canvas.drawCircle(playerX, playerY, 50, paint);
}
Altereaacordoinimigoparavermelho.
private void drawEnemy(Canvas canvas ) {
paint.setColor(Color.RED);
enemyRadius++;
canvas.drawCircle(enemyX, enemyY, enemyRadius, paint);
}
Poderodarojogo,oprotótipoestácomsprites,erodaosconceitosfundamentais
deumjogo!
47

## Página 58

2.10. Conclusão CasadoCódigo
Figura2.22:Imagemdojogo.
2.10 C onclusão
Umjogopossuidiversosconceitosbemespecíficos,quenãosãocomunsemoutros
tiposdeprojetosdesoftwarecomoweboudesktop. Paradesenvolverumjogoé
interessanteterbemesclarecidasaspartesprincipaisquecompõemoquebra-cabe ça
domundodaprograma çãoparagames.
Umjogoocorrenormalmenteemum loop infinito,noqual inputs,ou
seja,entradasdecomandos,sãointerpretadoseutilizadosparaexecutaraslógicas
dogame. Omovimentodoplayer,normalmenteumaimagemchamada sprite
costumaserdadoapartirdessesinputs,assimcomoomovimentodosinimigos,
48

## Página 59

CasadoCódigo Capítulo2. Protótipodeumjogo
queindiretamente,tambémécalculado.
Conceitosperiféricoscomo atualização da tela , limpeza da tela e
botões de comandos tambémsãoimportantesedevemsertodosmuitobem
pensadosnaexecu çãodojogo.
Comissoemmente, podemosplanejarnossojogoeiniciarseudesenvolvi-
mento.
49

## Página 61

Capítulo3
História do jogo
Jogossãofeitosdemagia,deilusão,defantasia.Sãohistóriasqueenvolvemaspes-
soasdeumaformapoderosa,naqualousuáriosesenteoprotogonistaestandono
comandodasa ções.
No começodolivrofalamossobreumjogofantásticochamado River Raid,
alémdedesenvolverumprotótipodejogodeaviãonocapítuloanterior.Poisbem,
chegouahora!
Massecriarmosumjogodenave,qualapeloeleterá?Oqueodiferenciarádos
miloutrosjogosquepodemosencontrarnaPlayStore?Oquefaráprenderaaten ção
dojogador?
Oenredo,ospersonagenseacarismasãope çasfundamentaisquevestemum
jogo.Érealmenteimportanteconsiderarumtemachamativoquesejadiferentedo
quejáestamosacostumados.Comofazeralgoumpoucodiferenteemumjogode
naves?Comotrazerissoparaumcontextocomoqualosnossosjogadoresestejam
familiarizados?
Criaremosumjogotambémcomatemáticadeaviões,comoumahomenagem

## Página 62

3.1. 14-bis CasadoCódigo
aumimportantebrasileiroqueparticipoudoiniciodessarevolu çãoaérea.
Em1873nasciaAlbertoSantosDumont,umpiloto,atletaeinventorbrasileiro.
Figura3.1:AlbertoSantosDumont
SantosDumontprojetou,construiuevoouosprimeirosbalõesdirigíveiscom
motoragasolina,conquistandooPrêmioDeutschem1901,quandocontornoua
TorreEiffel. Setornouentãoumadaspessoasmaisfamosasdomundoduranteo
séculoXX.
3.1 14- bis
Em1906,SantosDumontcriouumaviãohíbridochamado14bis,consideradoo
primeiroobjetomaispesadoqueoarasuperaragravidadeterrestre.
52

## Página 63

CasadoCódigo Capítulo3. Históriadojogo
Figura3.2:14-bisdobrasileiroSantosDumont
O pesadelo de Santos Dumont
Emagostode1914come çavaaPrimeiraGuerraMundialeosaviõescome çaram
aserutilizadosemcombatesaéreos. Aguerraficoucadavezmaisviolenta,com
metralhadorasebombas.SantosDumontviuseusonhosetransformarempesadelo.
Em1932,umconflitoentreoestadodeSãoPauloeogovernodeGetúlioVargas
foiiniciadoeaviõesatacaramacidade. EssavisãocausoumuitaangustiaaSantos
Dumont,quesesuicidou.
3.2 14- bisVS 100 Meteoros
SantosDumontinventouo14-bisnãocomointuitodeguerra.Nessejogo,homena-
gearemosDumontesuainven çãoutilizandosuaaeronaveparasalvaroplaneta!
DepoisdometeoroShoemaker-Levy-9quecaiuemJúpiter,depoisdometeoro
quecaiunaRússiaem2013,tudoindicavaqueofimestavapróximo. Oexército
brasileirodetectouapresen çade100meteorosentrandonaórbitaterrestre! Esses
meteorosacabarãocomaexistênciadetodaformadevidaqueconhecemoscasonão
sejamdetidosurgentemente.
53

## Página 64

3.2. 14-bisVS100Meteoros CasadoCódigo
Figura3.3:14-bisVS100Meteoros
Oplanetaestáemapuros!Todasaspartesdomundosófalamnesseassuntoe
buscamformasdeevitarofim.Eisquesurgeumbrasileiro,comseuinvento14-bis,
paraenfrentaroperigoetentarsalvaratodosnós.Munidodeumaarmapoderosa
paradestruirosmeteorosquecaemsobreaterra,vocêcomandaráaaeronave14-bis
nessaaventura!
54

## Página 65

CasadoCódigo Capítulo3. Históriadojogo
Figura3.4:Fluxodogame14-bisVS100Meteoros
55

## Página 67

Capítulo4
Telainicial:Lidandocom
Background,logoebotõesdemenu
Horadecome çarojogodeverdade!Agoraquejápassamospelosconceitosbásicos
dedesenvolvimentodejogoscomogameloop,sprites,colisõeseinputs,podemosir
umpoucomaisafundonodesenvolvimento.
Vamoscriarumjogobaseadonogamedocapítuloanterior,porémdessavezuti-
lizandoumframeworkdedesenvolvimentodejogoschamadoCocos2D.Omotivo
deutilizarumframeworkdaquiprafrenteéotimizardiversosaspectos,entreeles:
• Nãosepreocuparcomaposiçãoexataempixelsdosobjetos,comobotões,
porexemplo
• UtilizarcomportamentosjáimplementadosparaSprites,paranãoterproble-
mascomposicionamentodasimagens
• Eliminardalógicaaquestãodalimpezadetela,deixandoissocomorespon-
sabilidadedoframework

## Página 68

CasadoCódigo
• ConseguirefeitosinteressantesjáimplementadospeloCocos2D
• Trabalharmaisfacilmentecomsonseefeitos
Nessecapítulocriaremosatelainicial. Essatelaserácompostaporumlogo,
umbackground,equatrobotões. Veremosaquicomoposicionarcadaumdesses
elementosnatelaecomodetectarosinputsdosbotõesutilizandooCocos2D.Ao
fimdocapítulo,devemosteratelainicialcomoaseguir:
Figura4.1:Teladeabertura.
Vocêpoderáencontrarocódigocompletodojogo,juntocomalgumasmelho-
rias,nomeuGitHub:
https://github.com/andersonleite/jogos_android_14bis
58

## Página 69

CasadoCódigo Capítulo4. Telainicial:LidandocomBackground,logoebotõesdemenu
Masprefiravocêmesmoescrevê-lo!Serámenostrabalhosodoquevocêimagina,
ecertamenteajudarámuitonoseuaprendizado.
4.1 I niciando o projeto
No Eclipse vá emFile acesse as opções em New e selecione Android
Application Project. Criaremos um projeto chamado B i s. Os pa-
cotes ficarão a seu critério, mas você pode seguir a sugestão de usar
br.com.casadocodigo.bis. Dessa forma você poderá sempre acom-
panhar com facilidade o código fonte completo que está no github em
https://github.com/andersonleite/jogos_android_14bis.
Figura4.2:Criandoojogo14bis.
Nopasso2,deixeselecionadasasop çõespadrão.
59

## Página 70

4.1. Iniciandooprojeto CasadoCódigo
Figura4.3:Criandoojogo14bis.
Naterceiratelavocêpodeconfiguraroíconedogame. Vocêencontraráes-
sasimagensem https://github.com/andersonleite/jogos_android_14bis/tree/master/
res/
60

## Página 71

CasadoCódigo Capítulo4. Telainicial:LidandocomBackground,logoebotõesdemenu
Figura4.4:Criandoojogo14bis.
Naquartatela,selecioneaop ção BlankActivity.
61

## Página 72

4.1. Iniciandooprojeto CasadoCódigo
Figura4.5:Criandoojogo14bis.
NaúltimatelacrieaActivitycomname MainActivityecliqueem Finish.
62

## Página 73

CasadoCódigo Capítulo4. Telainicial:LidandocomBackground,logoebotõesdemenu
Figura4.6:Criandoojogo14bis.
4.2 S obre o Co c o s2D
OCocos2Déframeworkopensourcededesenvolvimentodejogos.Aversãoorigi-
nalfoicriadaemPythonedesdeentãofoiportadaparadiversaslinguagenscomo
C++,JavaScript,Objective-CeJava.Émuitopoderosoesimples.Comosetratade
umframeworkportadodeoutralíngua,suadocumenta çãonãoestábemorganizada
evocêpodesofrerumpoucoparaencontraralgumasinforma ções.
ParautilizaraversãoJava,bastabaixaroarquivo cocos2D-android.jarno
seguinterepositório:
https://code.google.com/p/cocos2d-android-1/downloads/list
Ouépossívelbaixaraversãojátestadacomojogonogithubdolivro,em:
https://github.com/andersonleite/jogos_android_14bis/tree/master/libs
Depois,adicioneojarao Build Path doseuprojeto.Lembradecomofazer
issonoEclipse?Casosuaview Package Explorerestejaaberta,bastadarumcliqueda
direitanojaredepoisescolher A d d t o B u i l d P a t h.Sepreferir,dêumcliquedadireita
63

## Página 74

4.3. Background CasadoCódigo
noseuprojeto,escolha B u i l d P a t he Configure Build Pathparaescolhereadicionaro
Cocos2D.
4.3 B ackground
Aprimeirateladogameéateladeabertura,enoCocos2D,utilizamosumaclasse
chamada CCLayerparaidentificarcadateladojogo. Aoherdardessaclassedo
framework,ganhamosalgunsreconhecimentosdoCoco2D,comoconseguirfazera
transiçãoentreastelascomapenasumalinhadecódigo.
U m a c l a s s e q u e h e r d a d eCCLayernãoprecisatermuitoscódigosdoframework,
podemoscriarnossatelainicialcomobementendermos,apenasutilizandoesse
comportamentoparainformaraoframeworkquetipodeobjetosestamosrepresen-
tando.
L a y e r s
Criartelascomo CCLayerdoCocos2Décriartelaspensandoemcamadasque
sesobrepõem.Essascamadassãotransparentes,amenosquandodefinidasdeoutra
forma,equandocolocadasumasobreasoutrasdefinematelafinal.
Nateladeabertura,podemospensaremcamadasparaaimagemdebackground,
paraologoeparaomenu.
Criaremos uma classe chamada TitleScreen. Você pode
criá-la no pacote que desejar. No nosso projeto, utilizamos
br.com.casadocodigo.meteoros.scenes. Lembre-se de organizar suas
classesempacotessignificativos.
Nestaclasse,utilizaremosumsegundocomponentedoCocos2D.Parainstanciar
umatelanoframework,utilizamosaclasse CCScene,queédevolvidajáprontapara
utilizarmosquandoinvocamosométodo node().
Scenes
OutroobjetoimportantedoCocos2Dsãoas Scenes.Comelas,conseguimos
inicializartelasdojogo.Umjogopodeterquantas Scenesforemnecessárias,po-
rémapenasumaestaráativaporvez.
Porexemplo,nonossojogoteremosateladeabertura,ateladojogo,atelade
ajuda,ateladepause,etc.Cadaumadelaséum Scene.
Vamosaocódigoinicialdateladeabertura. Precisamosdeumaclasseque
saiba trabalhar com camadas, e precisamos de uma tela. Criaremos a classe
64

## Página 75

CasadoCódigo Capítulo4. Telainicial:LidandocomBackground,logoebotõesdemenu
TitleScreenquereceberáessasdefiniçõesdecamadas,eaadicionaremosemuma
Scene,formandoabasedatelainicial.
public class TitleScreen extends CCLayer {
public CCScene scene() {
CCScene scene = CCScene.node();
scene.addChild(this);
return scene;
}
}
Ocódigoanteriorpreparaatelaparautiliza çãoeposicionamentodoselementos,
nonossocaso,esseselementosserãobackground,logo,ebotões.
Vamosiniciarconfigurandoobackgrounddogame.Assimcomobotõesoulogo,
obackgroundtambéméumobjetorepresentadoporumaimagem.Lembre-seque
paramanipularimagenstemosoconceitode Sprites,quebasicamenteéumob-
jetoassociadoaumafigura.
Sprites
U mSpritenoCocos2DécomoqualqueroutroSprite,ouseja,umaimagem
2Dquepodesermovida,rotacionada,alterarsuaescala,animada,etc. Umasdas
vantagensdeutilizar SpritescomoobjetosdoCocos2Déqueganhamosalgumas
possibilidadesdeanima ção,queveremosmaisàfrente.
Criaremosentãoaclasse ScreenBackgroundeparainformaraoCocos2D
quetipodeobjetoestamosrepresentando,nocasoum Sprite,herdaremosde
CCSprite.
Ganhamosaquiumafacilidademuitoimportanteaotratardeimagens,queé
oposicionamentoautomáticodoCocos2D,comoqualapenasprecisamospassaro
assetdesejado.
public class ScreenBackground extends CCSprite {
public ScreenBackground(String image ) {
super(image);
}
}
65

## Página 76

4.4. AssetsdaTeladeabertura CasadoCódigo
Umavezconfiguradooobjetoquerepresentaobackground,adicioná-loàtela
deaberturaésimples.Instanciamosumobjetodotipo ScreenBackgroundecon-
figuramossuaposi ção.Aqui,utilizaremosotamanhodatela,tantolarguraquanto
altura,paraposicionarobackgrounddeformacentralizada.Faremosissocomum
elementomuitoimportantedo Cocos2D,o CCDirector,queseráaprofundado
maisàfrente.Bastaadicionarobackgroundnateladeabertura,emanteremosum
atributoparaele:
public class TitleScreen extends CCLayer {
private ScreenBackground background ;
public TitleScreen() {
this.background = new ScreenBackground("background.png");
this.background.setPosition(
screenResolution(CGPoint.ccp(
CCDirector.sharedDirector().winSize().width / 2.0f,
CCDirector.sharedDirector().winSize().height / 2.0f
)));
this.addChild(this.background);
}
// restante do código
Precisamosentãodo background.pngdonossojogo.Criamosalgumasima-
genseutilizamosoutrasdefontesgratuitasparanossojogo. Vocêdevebaixarum
zipqueascontémnesseendere ço:
https://github.com/andersonleite/jogos_android_14bis
Coloqueoarquivo background.jpgdentrododiretório assetsdoseupro-
jeto.Vocêprecisarárepetiresseprocedimentoparaoutrasimagens,sonsearquivos
dosquaisprecisaremosnodecorrerdodesenvolvimentodenossojogo.
4.4 A ssets da Tela de abertura
Ateladeaberturadogameterá6assets(arquivoscomoimagensefiguras)queserão
utilizadosparacomporlogoemenus.
Paracomeçar,vamosorganizarnaclasse Assetsessesarquivosdeimagensdo
game. Assim,podemosfazerchamadasasimagensqueestãonapastademesmo
nome, Assetsnoprojeto.
66

## Página 77

CasadoCódigo Capítulo4. Telainicial:LidandocomBackground,logoebotõesdemenu
public class Assets {
public static String BACKGROUND = "background.png";
public static String LOGO = "logo.png";
public static String PLAY = "play.png";
public static String HIGHSCORE = "highscore.png";
public static String HELP = "help.png";
public static String SOUND = "sound.png";
}
Alterealinhada TitleScreenquechamavao background.pngparautilizar
aclasse Assets:
this.background = new ScreenBackground(Assets.BACKGROUND);
Utilizaremosessaclasseparaadicionaroutrosassetsmaisprafrente,quandoos
objetosinimigoseoplayerforemdesenhados. Éimportanteterumaclassecomo
essaparanãoespalharsuasimagenspelocódigo. Porexemplo,imaginequevocê
queralteraraimagemdanaveprincipal.Émelhoralterá-laemapenasumlugar,e
fazerreferênciaaessavariávelnasclassesnecessárias.
4.5 C apturando configurações iniciais do device
DiversosdevicesrodamAndroidatualmente,oquefazcomqueotamanhodatela
nãosejaumpadrãocomlarguraealturasfixas.Existemalgumastécnicasparatentar
limitaresseproblemaduranteodesenvolvimentodojogo. Utilizaremosaquiuma
técnicasimplesparaadaptarnossoconteúdoaosdiversosdispositivos,capturando
asmedidaseutilizando-ossemprequefornecessáriolidarcomessaquestão.
Parainiciarasconfigura çõesdetelaecriaratelainicial,criaremosalgunsméto-
dos:
• screenResolution:RecebeaposiçãodoobjetocomoumtipodoCocos2D,o
GCPoint
• screenWidth:Retornaalarguradatela
• screenHeight:Retornaaalturadatela
OCocos2Dnosajudanessemomento,poisjápossuiobjetospreparadospara
executaressafun ção. Podemosutilizaraclasse CCDirectorparaconseguiros
parâmetrosdatela.
67

## Página 78

4.5. Capturandoconfiguraçõesiniciaisdodevice CasadoCódigo
Director
OCCDirectoréumcomponentequecuidadastransi çõesentre scenes,ou
seja,transiçõesdetelasdojogo.Eleéum Singletonquesabequaltelaestáativa
nomomentoegerenciaumapilhadetelas,aguardandosuaschamadasparafazeras
transições.
Vamos implementar a classeDeviceSettings, responsável por acessar o
CCDirectoreretornarasmedidaseconfigura çõesdodevice.
public class DeviceSettings {
public static CGPoint screenResolution(CGPoint gcPoint ) {
return gcPoint;
}
public static float screenWidth() {
return winSize().width;
}
public static float screenHeight() {
return winSize().height;
}
public static CGSize winSize() {
return CCDirector.sharedDirector().winSize();
}
}
Comisso,podemosrefatoraroconstrutordaclasseTitleScreenparaficarcomo
aseguir.
import static
br.com.casadocodigo.nave.config.DeviceSettings.screenHeight;
import static
br.com.casadocodigo.nave.config.DeviceSettings.screenWidth;
public TitleScreen() {
this.background = new ScreenBackground(Assets.BACKGROUND);
this.background.setPosition(
screenResolution(CGPoint.ccp(
screenWidth() / 2.0f,
screenHeight() / 2.0f
68

## Página 79

CasadoCódigo Capítulo4. Telainicial:LidandocomBackground,logoebotõesdemenu
)));
this.addChild(this.background);
}
O CCDirectorétambémresponsávelpelainicializaçãodateladeabertura.
Iniciando a tela de abertura
Telainicialpreparada!Agoraprecisamosfazeratransi ção,ouseja,aochegarna
Activity,queéaportadeentradadogame,devemosinformaraoCocos2Dpara
iniciarateladeabertura.
UmobjetomuitoimportantedoCocos2Dseráutilizadoparaessecontrole.Uti-
lizaremoso CCDirectornovamente,dessavezpararodarumanovatela,apartir
dométodo runWithScene()passandocomoparâmetroa TitleScreen,queé
ateladeabertura.
public class MainActivity extends Activity {
@Override
protected void onCreate(Bundle savedInstanceState ) {
super.onCreate(savedInstanceState);
// definindo orientação como landscape
setRequestedOrientation(
ActivityInfo.SCREEN_ORIENTATION_PORTRAIT);
requestWindowFeature(Window.FEATURE_NO_TITLE);
getWindow().setFlags(
WindowManager.LayoutParams.FLAG_FULLSCREEN,
WindowManager.LayoutParams.FLAG_FULLSCREEN);
// configura a tela
CCGLSurfaceView glSurfaceView = new CCGLSurfaceView(this);
setContentView(glSurfaceView);
CCDirector.sharedDirector().attachInView(glSurfaceView);
// configura CCDirector
CCDirector.sharedDirector().setScreenSize(320, 480);
// abre tela principal
CCScene scene = new TitleScreen().scene();
CCDirector.sharedDirector().runWithScene(scene);
69

## Página 80

4.6. Logo CasadoCódigo
}
}
Jáépossívelrodaroprojetoeverateladeaberturacomobackgroundconfigu-
rado!Façaoteste.
4.6 L o g o
Vamosutilizaramesmaideiaecolocarumlogodojogonotopodatela.
Ologoéumaimagemsimples.Eimagenssãocoordenadasporobjetosquecha-
mamosde Sprites.Criaremosum Spritedeformasimplesparaposicionaro
logoeutilizaremosométodo setPositionparaqueoCocos2Dsaibaondecolocar
oelemento.
Prafinalizar,bastaadicionarologoatelainicialpelométodo addChild().
Mudeoconstrutordasua TitleScreen:
public TitleScreen() {
// código atual
...
CCSprite title = CCSprite.sprite(Assets.LOGO);
title.setPosition(screenResolution(
CGPoint.ccp( screenWidth() /2 , screenHeight() - 130 )));
this.addChild(title);
}
Aorodaroprojetojátemosimagemdebackgroundelogodojogoposicionados.
4.7 B otões
Osbotõessãopartesimportantíssimasdojogo.Épartirdelesqueousuáriointerage
comogameequerecebemoscomandosparatransicioná-lase,maisàfrente,mover
oplayer,atirar,etc.
Paracolocarosbotõesnatelainicial,utilizaremosconceitosdoCocos2Decon-
ceitosdeOrienta çãoaObjetos,alémdeDesignPatterns,comoDecoratoreObser-
vable.
70

## Página 81

CasadoCódigo Capítulo4. Telainicial:LidandocomBackground,logoebotõesdemenu
UtilizandooCocos2Dotrabalhocominputsdebotõesficabemmaissimples,
nãoprecisandodetectaraposi çãodotoquenatelaecompararcomoposiciona-
mentodos Sprites. Essetrabalhoseráfeitopeloframework,eojogopodese
preocuparcomalógicaemsi.
Vamosaocódigo.Parainformaraoframeworkqueoobjetoqueestamosrepre-
sentandoéumbotãoquepodeserpressionadoeprecisaresponderaeventos,her-
daremosdaclasse CCLayer.OCocos2Dreconheceráoobjetocomoumacamada
enosdaráoscomportamentosdereconhecimentodeinputqueprecisamos.
Aoconstruirumbotão,precisamospassarumaimagem.Nocasodatelainicial
asimagensserãoosbotõesdePlay,HighscoreeHelp,alémdobotãodesom.
Um ponto importante para trabalhar com o evento de toque em um
dos botões é habilitar o evento deTouch para isso, usamos o comando
this.setIsTouchEnabled(true).
public class Button extends CCLayer {
private CCSprite buttonImage ;
private ButtonDelegate delegate ;
public Button(String buttonImage ) {
this.setIsTouchEnabled(true);
this.buttonImage = CCSprite.sprite(buttonImage);
addChild(this.buttonImage);
}
}
OquefoifeitoatéaquiéinformaraoCocos2Dqueteremosobjetosdotipobotão,
quereceberãoumaimagemesãohabilitadosparaseremtocados.
Oqueprecisamosagoraé:
• Criaros4botões:Play,Highscore,HelpeSound.
• Configurarsuasposições
• Adicioná-losnatelainicial
Criaremosumanovaclassecomaresponsabilidadedeorganizarosbotõesdo
Menu. A classeMenuButtonsherdade CCLayerparaquepossamosmaispra
frentedetectareventosdetoques.
71

## Página 82

4.7. Botões CasadoCódigo
public class MenuButtons extends CCLayer {
private Button playButton ;
private Button highscoredButton ;
private Button helpButton ;
private Button soundButton ;
public MenuButtons() {
this.setIsTouchEnabled(true);
this.playButton = new Button(Assets.PLAY);
this.highscoredButton = new Button(Assets.HIGHSCORE);
this.helpButton = new Button(Assets.HELP);
this.soundButton = new Button(Assets.SOUND);
// coloca botões na posição correta
setButtonspPosition();
addChild(playButton);
addChild(highscoredButton);
addChild(helpButton);
addChild(soundButton);
}
private void setButtonspPosition() {
// Buttons Positions
playButton.setPosition(
screenResolution(
CGPoint.ccp( screenWidth() /2 , screenHeight() - 250 ))
);
highscoredButton.setPosition(
screenResolution(
CGPoint.ccp( screenWidth() /2 , screenHeight() - 300 ))
);
helpButton.setPosition(
screenResolution(
CGPoint.ccp( screenWidth() /2 , screenHeight() - 350 ))
);
soundButton.setPosition(
72

## Página 83

CasadoCódigo Capítulo4. Telainicial:LidandocomBackground,logoebotõesdemenu
screenResolution(
CGPoint.ccp( screenWidth() /2 - 100,
screenHeight() - 420 ))
);
}
}
Faltaapenasinformaràtelainicialqueméoresponsávelpelogerenciamentodos
botões. Criaremosentãoumainstânciade MenuButtonseadicionaremosnela.
Adicionenovamenteaoconstrutorda TitleScreen:
MenuButtons menuLayer = new MenuButtons();
this.addChild(menuLayer);
Rodeseuaplicativo!Tenteclicarnosbotões,oqueacontece?
A v a nçamosbemcomosbotões,posicionandoepreparando-oscomoelementos
quepodemrecebereventosdetoque.Porém,nãoexisteaindaumrelacionamento
entrenossatelainicialenossocontroledebotões.
Essaéumapartecomplexadodesenvolvimentodegames.Nãoésimplescoor-
denarobjetoscomciclosdevidadiferentesquerodampelaaplica ção.Oquefaremos
aquiéutilizarumDesignPatternparaauxiliarnacomunica çãoentreosobjetos.
Paracomeçar,definiremosumnovotiponoprojeto,responsávelporgarantir
queinstânciasdeletenhamummétodoquereconheceeventosdetipoemobjetos
dotipo Button. Issoéimportanteparagarantirqueapenasreceberemosobjetos
quepodemseranalisadoseresponderaoeventodesejado.
public interface ButtonDelegate {
public void buttonClicked(Button sender );
}
Aclasse MenuButtonsimplementaráessecomportamento:
public class MenuButtons extends CCLayer implements ButtonDelegate {
Paracomplementar,precisamosdaralgumarespostaeverificarseoseventosde
toqueemcadaumdosbotõesestásendocorretamentecapturado. Comoutiliza-
mosumobjetodotipo CCLayerdoCocos2D,podemossobrescreverométodo
buttonClicked,queenviaumareferênciadoobjetodetipo Buttonquefoipres-
sionado.
73

## Página 84

4.7. Botões CasadoCódigo
Comessainforma çãoemmãos,podemosverificarqualbotãofoipressionadoe
executarocódigocorrespondente.Porenquanto,faremosumlogdopróprioconsole
paraidentificaressaintera ção.
@Override
public void buttonClicked(Button sender ) {
if (sender.equals(this.playButton)) {
System.out.println("Button clicked: Play" );
}
if (sender.equals(this.highscoredButton)) {
System.out.println("Button clicked: Highscore" );
}
if (sender.equals(this.helpButton)) {
System.out.println("Button clicked: Help" );
}
if (sender.equals(this.soundButton)) {
System.out.println("Button clicked: Sound" );
}
}
Mascomofazercomqueosbotõesinvoquemométodo buttonClickeddo
nossolistener,o MenuButtons? Vamoscriarummétodonaclasse Buttonque
definequemdeveráseravisado:
public void setDelegate(ButtonDelegate sender ) {
this.delegate = sender;
}
Agoraqueobotãosabequemdeveavisar,devemosfazercomqueo delegate
sejaavisadoquandoessebotão(queéum CCLayer)fortocado.
Primeirodevemossobrescreverométodo registerWithTouchDispatcher
paradizerqueopróprioobjetobotãorecebaasnotifica çõesdetoque:
@Override
protected void registerWithTouchDispatcher() {
CCTouchDispatcher.sharedDispatcher()
.addTargetedDelegate(this, 0, false);
}
7 4

## Página 85

CasadoCódigo Capítulo4. Telainicial:LidandocomBackground,logoebotõesdemenu
Agora,todavezquealguémtocarnesselayer,receberemosumainvoca çãopara
ométodo ccTouchesBegan. Precisamosreescrevê-loeverificarseomenuem
questãofoitocado.Faremosissoatravésdométodo CGRect.containsPoint,que
verificaráseolocaltocado( touchLocation)estádentroda“caixa”queaimagem
domenuforma( buttonImage.getBoudingBox()):
@Override
public boolean ccTouchesBegan(MotionEvent event ) {
CGPoint touchLocation = CGPoint.make(event.getX(), event.getY());
touchLocation = CCDirector.sharedDirector()
.convertToGL(touchLocation);
touchLocation = this.convertToNodeSpace(touchLocation);
// Verifica toque no botão
if (CGRect.containsPoint(
this.buttonImage.getBoudingBox(), touchLocation)) {
delegate.buttonClicked(this);
}
return true ;
}
Sófaltaadicionarmos,naclasse MenuButtons,ainforma çãodequeodelegate
dosbotõesdeveavisaraprópriaclasse MenuButtons,jáqueéelaquetemométodo
buttonClicked:
public MenuButtons() {
this.playButton.setDelegate(this);
this.highscoredButton.setDelegate(this);
this.helpButton.setDelegate(this);
this.soundButton.setDelegate(this);
}
Rodeoprojetoeconfiraosbotõesrecebendoosinputsnoconsole.
Aquicriamosnossaprópriaclassede Button,maspoderíamosterusadooutras
classesjáprontasdoCocos2D,como Menue MenuItem.Tercriadouma Button
nosajudaránoscapítulosseguintes,noqualteremosbotõesdentrodoprópriojogo,
alémdetermosaprendidoumpoucomaisdosdetalhesinternosdoframework.
75

## Página 86

4.8. Conclusão CasadoCódigo
4.8 C onclusão
Ojogodeveestarcomomostradonatelaabaixo,combackgroundelogoconfigura-
dos.Alémdisso,4botõesforamimplementados,oPlay,Highscore,Helpecontrole
deSom.
Figura4.7:Teladeabertura.
Ocoredodesenvolvimentodeumjogonãoéfácil.Reparenaevolu çãodopro-
tótipoparaojogorealqueestamosfazendoeperceberáquepartescomplexasforam
encapsuladaspeloCocos2D.
Nessecapítulo,fomosumpoucomaisafundoemquestõescomotelas( Scenes)
ecamadas( Layers).UtilizamostambémumimportanteelementodoCocos2D,o
Director.
76

## Página 87

CasadoCódigo Capítulo4. Telainicial:LidandocomBackground,logoebotõesdemenu
Aseguir,faremosatransi çãoparaateladojogoeteremosnossosprimeiros
elementosdogame.
77

## Página 89

Capítulo5
Teladojogoeobjetosinimigos
Horadeadicionarperigoaonossogame! Nessecapítuloiremosentrarnatelado
jogodefato,ondetodaaa çãoocorrerá.Essaseráaprincipalpartedojogoeporisso
trataremosemalgunscapítulos.
Parainiciar,passaremospelatransi çãodateladeaberturaparaateladejogo.
Alémdisso,colocaremososinimigosaparecendonatela.Algunsconceitosimpor-
tantesdoCocos2Dserãoutilizadosnessecapítulo,cujoobjetivoéterateladogame
rodando,comalgunsinimigossurgindo.
Utilizaremosmuitodoquejáfoivistoatéaqui,como CCLayerspararepresen-
tarcamadasdeumatela, CCSpritesparacontrolarobjetose CCSceneparacriar
ateladojogo.Alémdissoo CCDirectorseráutilizadonovamente.
Nofimdessecapítuloteremosatransi çãoentreteladeaberturaeteladogame,
alémdosobjetosinimigosaparecendonatela.

## Página 90

5.1. GameScene CasadoCódigo
Figura5.1:Meteorosinimigos.
5.1 G ame Scene
Precisamosdeumatelaparaojogo,paraconteroselementosprincipaisdeintera ção
dogamecomoplayer,inimigosecontroles.Assimcomoanteriormente,criaremos
umatelaherdandodaclasse CCLayerdoCocos2D,paraquepossamosterdiversas
camadasatuantes,comobotões,inimigos,player,score,etc.
Tambémcomoanteriormente,adefini çãodeumatelaécriadaatravésdeum
CCScene,quesaberálidarcomascamadasdanossaclasse.
80

## Página 91

CasadoCódigo Capítulo5. Teladojogoeobjetosinimigos
O Maestro
Idealmente,essaclassenãodevetermuitasresponsabilidades,massim,funci-
onarcomoumorquestradordetodososelementos,ouseja,ummaestroemuma
orquestra,quedirigeecomandaoquetodososoutroselementosfazemecomoeles
interagementresi.
Elaseráaclassequeinicializaobjetosnojogo,quecolocaobjetosnatela,porémo
comportamentodecadaumdelesserárepresentadoindividualmenteemcadaclasse
correspondente.
Algumasdasresponsabilidadesda GameScene,aclassemaestrodojogo,devem
ser:
• Iniciarateladogameeorganizarascamadas
• Adicionarobjetoscomoplayer,inimigosebotõesaessascamadas
• Inicializarcadaumdessesobjetos
• Checarcolisõesentreobjetos
Aclasse GameScenetemmuitaresponsabilidade,porémnãodetémregrase
lógicasdecadaelemento. Outrafun çãoimportantedessaclasseéaplicarumdos
conceitosvistosanteriormente,do game loop.
Vamosentãocriaraclasse GameScenejácolocandoumbackgroundcomofi-
zemosanteriormentenateladeabertura:
public class GameScene extends CCLayer {
private ScreenBackground background ;
private GameScene() {
this.background = new ScreenBackground(Assets.BACKGROUND);
this.background.setPosition(
screenResolution(
CGPoint.ccp(screenWidth() / 2.0f, screenHeight() / 2.0f)));
this.addChild(this.background);
}
public static CCScene createGame() {
CCScene scene = CCScene.node();
GameScene layer = new GameScene();
81

## Página 92

5.2. Transiçãodetelas CasadoCódigo
scene.addChild(layer);
return scene;
}
}
5.2 T ransição de telas
Paraqueojogocomece,precisamosfazerolinkentreateladeaberturaeatelado
game!
Aquiutilizaremoso CCDirectorquesabemanteruma CCSceneativaporvez.
Alémdetrocardeumatelaparaoutra,oCocos2Dnospermiteescolhereconfigurar
detalhesdessatransi ção.
Utilizaremosométodo replaceScenequefaráumatransi çãocomotempo
depausaentreumatelaeoutro,gerandoumefeitosuave.
Paraisso,naclasse MenuButtons,mudamoso buttonClickedparaqueo
ifdobotãodeplaycomeceojogo:
@Override
public void buttonClicked(Button sender ) {
if (sender.equals(this.playButton)) {
System.out.println("Button clicked: Play" );
CCDirector.sharedDirector().replaceScene(
CCFadeTransition.transition(1.0f,
GameScene.createGame()));
}
//...
}
}
Rodeojogoecliquenomenudeplay.Oqueacontece?Porenquanto,sótemos
ateladebackground!
5.3 E ngines
Temosaclassequeorquestraráosobjetosdogame,ecriaremosagoraclassesres-
ponsáveisporgerenciaroutroselementos.Oprimeiroelementoqueteremosserão
osinimigos.Nossosinimigosserãometeorosquecairãoeprecisarãoserdestruídos
peloplayer.
82

## Página 93

CasadoCódigo Capítulo5. Teladojogoeobjetosinimigos
Criaremos uma nova camada, um novo layer para representar esses inimi-
gos. Comoutilizadoanteriormente,camadassãorepresentadasporheran çasao
CCLayerdoCocos2D.
Paramanterolinkentreatelaprincipaleessacamada,utilizaremosomesmo
conceitode delegatesvistoanteriormente,ouseja,atelatojogoeacamada
dosmeteorosinimigosserãolinkadosatravésdessadelega ção,paraseremchamadas
quandoprecisaremfazerentresi.
Engine de objetos inimigos
Nossacamadadeobjetosinimigos,osmeteoros,seráresponsávelporcriarini-
migoseenviaràteladojogo.Essaenginedemeteorosnãoéresponsávelpelomovi-
mentodometeoroemsi,massimdecontrolaraapari çãodelesnatelaefazerolink
entreobjeto MeteoroeteladoGame.
Éimportantequeuma Enginesaibaquandoéomomentodecolocarumnovo
elementonojogo. Muitasvezes,principalmenteparaobjetosinimigos,utilizamos
númerosrandômicosparadefinirahoradecolocarumnovoinimigonatela.
Essaideiafoimuitoutilizadaporjogosemqueonívelmaisdifícileraapenasuma
equaçãonaqualonúmerorandômicogeradosatisfaziaumacondi çãodeentradaem
um if.Nocódigodanossaengineabaixo,faremosexatamenteisso.
Valecitarqueaengineéocódigoresponsávelpormanteroloopdeobjetos,e
comoCocos2D,utilizamosmétodosdeagendamentoparaisso.Ouseja,criaremos
um scheduleparaqueaengineanalisesedeveounãoatualizareincluirumnovo
objetoinimigonatela.
Abaixo,ocódigodaprimeiraEnginedogame,aclasse MeteorsEngine.
public class MeteorsEngine extends CCLayer {
private MeteorsEngineDelegate delegate ;
public MeteorsEngine() {
this.schedule("meteorsEngine", 1.0f / 10 f);
}
public void meteorsEngine(float dt) {
// sorte: 1 em 30 gera um novo meteoro!
if(new Random().nextInt(30) == 0){
this.getDelegate().createMeteor(
new Meteor(Assets.METEOR));
}
83

## Página 94

5.3. Engines CasadoCódigo
}
public void setDelegate(MeteorsEngineDelegate delegate ) {
this.delegate = delegate;
}
public MeteorsEngineDelegate getDelegate() {
return delegate;
}
}
Parafecharolinkentreambasascamadas,criaremosumainterfacequeobrigará
ateladojogoaterummétodoparareceberosobjetoscriadosporessa Enginee
colocá-losnatela.
public interface MeteorsEngineDelegate {
public void createMeteor(
Meteor meteor , float x, float y, float vel,
double ang, int vl);
}
Implementeainterface MeteorsEngineDelegatenaclasse GameScenee
crieométodoqueseráresponsávelpelosmeteorosquecriaremosemseguida.Apro-
veitaremosparafazeracamadadosmeteorosnateladogame.
Mantendo as referências
Umoutropontoimportanteparaocontroledojogoetodaaorquestra çãoéman-
tertodososobjetoscriadosdeumaformafácilparaquepossamseranalisadosde-
pois. Umexemplonessecasoéacompara çãocomotirooucomopróprioplayer
paradetectarcolisões,queserãotratadosmaisàfrente.
Vamosguardarareferênciadecadameteorocriadoemumacole çãonaclasse
GameScene:
public class GameScene extends CCLayer implements MeteorsEngineDelegate {
private ScreenBackground background ;
private MeteorsEngine meteorsEngine ;
private CCLayer meteorsLayer ;
private List meteorsArray ;
@Override
84

## Página 95

CasadoCódigo Capítulo5. Teladojogoeobjetosinimigos
public void createMeteor(Meteor meteor , float x, float y, float vel,
this.meteorsLayer.addChild(meteor);
meteor.start();
this.meteorsArray.add(meteor);
}
}
5.4 M eteor
Chegamosaoobjetoinimigopropriamentedito. Asprincipaisresponsabilidades
desseobjetosão:
• Carregarimagem(Sprite)
• Posicionarelementonatela
• Guardaraposiçãodoobjetoparaquepossasermovimentadocomotempo
Esseéoprimeiroobjetodejogorealmentequecriaremos.Atéomomento,cria-
mostelaspreenchendocomelementos,botõesdemenueclassesdeengineparadar
abaseaesseselementosprincipaisdojogo.
Aprimeiracoisaasefazeréadicionaroassetdometeoronaclasse Assets.
public class Assets {
public static String METEOR = "meteor.png";
// outros assets
}
Vamoscriaraclasse Meteor.Inicialmente,cadameteoronascenotopodatela
(éovalorde screenHeight),enumaposi ção xrandômica:
public class Meteor extends CCSprite {
private float x, y;
public Meteor(String image ) {
super(image);
x = new Random().nextInt(Math.round(screenWidth()));
y = screenHeight();
}
}
85

## Página 96

5.5. Teladogame CasadoCódigo
Reparequeoobjetometeoropermanecevivonamemóriaporumbomtempo.
Eleécriadoe,acadaframe,renderizadoemumaposi çãodiferente,dandoaimpres-
sãodemovimento.
Aquimaisumavezoframeworknosajuda.Paraquecadaframesejarenderizado
duranteojogo,eaposi çãodoobjetomudecomopassardotempo,oCocos2D
nospermiteescolherummétodoqueseráinvocadodetempoemtempo.Issoserá
definidono start,fazendo schedule("nomeDoMetodo"). Nonossocaso,o
métodoseráupdate:
public void start() {
this.schedule("update");
}
public void update(float dt) {
y -= 1;
this.setPosition(screenResolution(CGPoint.ccp(x, y )));
}
Variável dt dos updates
OCocos2Dvai tentarinvocaroseumétodo updatedexemxmilis-
segundos,issoé,emcadaframe.Mas,porumasériedemotivos,opro-
cessadorpodeestarocupadocomoutrascoisas,fazendocomqueessa
chamadaagendadanãoocorraquandovocêqueria. Elepodedemorar
mais.Nessecaso,vaidarumaimpressãoqueseujogoestálento,jáque
atelaserárenderizadacomosesótivessepassadootempodeumframe,
masnaverdadepodeterpassadoalgunssegundos.
Numjogoprofissional,vocêdeveguardaressainforma çãoparadeci-
dircorretamentequantospixelscadaobjetodevemudar.Nonossocaso,
seo dtformaiorqueode1frame,deveríamosdescerometeoromais
que1pixel,fazendoaregrade3.
5.5 T ela do game
Parafecharelinkaraclassedateladojogo,comaenginedemeteorosecomos
objetosmeteoroscriados,modificaremosaclasse GameScene.
Primeiramente,vamoscriarummétodoqueconteráainicializa çãodosobjetos
dejogo.Crieométodo addGameObjects:
86

## Página 97

CasadoCódigo Capítulo5. Teladojogoeobjetosinimigos
private void addGameObjects() {
this.meteorsArray = new ArrayList();
this.meteorsEngine = new MeteorsEngine();
}
Noconstrutor,criaremosumlayerespecialmenteparaosmeteoroseadicionare-
mosateladojogovia addChild.Alémdisso,invocaremoso addGameObjetos.
Nossoconstrutorficaráassim:
private GameScene() {
this.background = new ScreenBackground(Assets.BACKGROUND);
this.background.setPosition(
screenResolution(CGPoint.ccp(screenWidth() / 2.0f,
screenHeight() / 2.0f)));
this.addChild(this.background);
this.meteorsLayer = CCLayer.node();
this.addChild(this.meteorsLayer);
this.addGameObjects();
}
}
Ummétodoimportantequeutilizaremosaquiéo onEnter().Eleéinvocado
peloCocos2Dassimqueateladogameestáprontaparaorquestrarosobjetosdo
jogo.Eleseráaportadeentradadojogo.Porenquantosimplesmenteadicionaremos
o meteorsEngineesetaremoso delegatecomo this,parasermosavisados
dosnovosmeteoros:
@Override
public void onEnter() {
super.onEnter();
this.startEngines();
}
private void startEngines() {
this.addChild(this.meteorsEngine);
this.meteorsEngine.setDelegate(this);
}
87

## Página 98

5.6. Conclusão CasadoCódigo
5.6 C onclusão
Temosagoraateladeaberturaeateladejogo,ondeogameloopérodado,em
funcionamento.Nossogameloopinicializaosinimigos.Precisamosdeumplayer
parajogarcontraeles,éoqueveremosaseguir!
Figura5.2:Meteorosinimigos.
88

## Página 99

Capítulo6
CriandooPlayer
Teladojogopreparadaeinimigosaparecendo!Cenárioperfeitoparainiciarmoso
desenvolvimentodoplayer!Essaéumapartebeminteressantenodesenvolvimento
dejogos,poisprogramaremosoobjetoqueserácontroladopelosinputsdousuário.
Paraisso,utilizaremosamaioriadoselementosdoframework Cocos2dque
vimosatéagoraparatrabalharcomoplayer.Utilizaremoscamadas,spriteseoscon-
ceitosvistosanteriormente.
Nossateladejogoprecisarádemaisumacamada,utilizaremos Spritespara
oPlayeredetectaremosinputsdousuárioparamovê-lo.
Resumidamente,nessecapítulofaremos:
• Colocaroplayernatela
• Movimentaroplayer
• Eatirar!

## Página 100

6.1. DesenhandooPlayer CasadoCódigo
Daremosumpassoimportantenaconstru çãodojogonessecapítulo,oobjetivo
finaléteracenaaseguir,aindasemdetectarcolisões.
Figura6.1:14bisatirandocontraosmeteoros.
6.1 D esenhando o Player
Iniciaremospelaimagem,adicionandoafiguradoplayernaclasse Assets.
public class Assets {
public static String NAVE = "nave.png";
}
90

## Página 101

CasadoCódigo Capítulo6. CriandooPlayer
Criaremosoobjetoprincipale,comoanteriormente,controlamosfiguraseima-
gensherdandodo CCSpritedo Cocos2D.
UtilizaremosométodoqueretornaalarguradatelaparacentralizaroPlayer.
Precisamosdevariáveisqueguardemessasposi çõespoisprecisaremosalterá-las
maisàfrente.
Comojáutilizadopelasoutrasclasses,manteremosolinkentreteladeabertura
eplayerutilizandoumdelegate.
Aclasse Playerseráiniciadadamaneiraaseguir.
public class Player extends CCSprite{
float positionX = screenWidth()/2;
float positionY = 50;
public Player(){
super(Assets.NAVE);
setPosition(positionX, positionY);
}
public void setDelegate(ShootEngineDelegate delegate ) {
this.delegate = delegate;
}
}
OobjetoPlayerjáestáprontoparaserinicializado,masaindanãoexisteuma
camadanotaledojogoresponsávelpormostrá-lo. Paraqueoplayerapare çana
teladojogo,temosqueadicionarmaisumacamada. Essacamadateráonomede
playerLayer.
Na classe GameScene é necessário adicionar a variável de layer, e iniciá-
la no construtor. Após isso, adicione a camada criada através do método
addGameObjects.
private CCLayer playerLayer ;
private Player player ;
private GameScene(){
this.playerLayer = CCLayer.node();
this.addChild(this.playerLayer);
}
91

## Página 102

6.2. Botõesdecontrole CasadoCódigo
private void addGameObjects() {
this.player = new Player();
this.playerLayer.addChild(this.player);
}
Figura6.2:14bisprontoparaa ção.
6.2 B otões de controle
Játemosoplayeraparecendonatela.Alémdisso,elejáestáemumacamadadatela
dogame,oquefazcomquesejarenderizadoduranteojogo.
Vamosagoraadicionaroutroselementosàtela,paraqueoplayerpossaserco-
mandadopelosinputsdousuário. Paraisso,precisaremosdenovasimagenspara
92

## Página 103

CasadoCódigo Capítulo6. CriandooPlayer
essescontroleseumanovaclasseresponsávelporessacamadanojogo.
Iniciaremosadicionando3imagens,duasparamovimentaroplayerentredi-
reitaeesquerdaeoutraqueseráobotãodeatirar.Essasimagensserãoincluídasno
arquivo Assets.
public class Assets {
public static String LEFTCONTROL = "left.png";
public static String RIGHTBUTTON = "right.png";
public static String SHOOTBUTTON = "shootButton.png";
}
Aclassedebotõesdecontrolenãoécomplexa,porémtemalgumascaracterísti-
casimportantesaseremressaltadas.
Essaclassedevesertratadacomomaisumacamadanateladejogo,porisso,
seráutilizadacomoum CCLayer. Alémdisso,essacamadadeveexecutara ções
quandoreceberotoquenatela,ouseja,precisamosdeumcódigoqueidentifiqueo
inputdousuárioeexecutealgumalógicadojogo.Paraisso,utilizaremosnovamente
ainterface ButtonDelegate.
Começaremosaclasse GameButtonsdefinindo3botõescomovariáveisdotipo
Button. Noconstrutorhabilitaremosotoquenatela,inicializandoosbotões,e
mantendoolinkcomateladejogo,pelodelegate.Porfim,adicionaremososbotões
criadosnateladejogo.
public class GameButtons extends CCLayer implements ButtonDelegate {
private Button leftControl ;
private Button rightControl ;
private Button shootButton ;
public static GameButtons gameButtons() {
return new GameButtons();
}
public GameButtons() {
// Habilita o toque na tela
this.setIsTouchEnabled(true);
// Cria os botões
this.leftControl = new Button(Assets.LEFTCONTROL);
93

## Página 104

6.2. Botõesdecontrole CasadoCódigo
this.rightControl =
new Button(Assets.RIGHTCONTROL);
this.shootButton = new Button(Assets.SHOOTBUTTON);
// Configura as delegações
this.leftControl.setDelegate(this);
this.rightControl.setDelegate(this);
this.shootButton.setDelegate(this);
// Adiciona os botões na tela
addChild(leftControl);
addChild(rightControl);
addChild(shootButton);
}
}
Não esqueça de adicionar o delegate, fazendo o link entre as telas: Na
GameSceneadicioneocódigoabaixonoconstrutor.
gameButtonsLayer.setDelegate(this);
Quasetudoprontoparaqueoscontrolesapare çamnateladojogo,porém,ainda
énecessárioconfiguraroposicionamentodeles.CadaobjetodotipoButtontemum
método setPosition()queutilizaremosparaessafun ção.
Comotemos3botõesparaconfigurarposicionamentos,separaremosemum
métodoapartechamado setButtonspPosition().Faremosachamadaaesse
métodonoconstrutor,antesdeadicioná-losnatela.
public GameButtons() {
//...
// Configura posições
setButtonspPosition();
// Adiciona botões na tela
addChild(leftControl);
addChild(rightControl);
addChild(shootButton);
94

## Página 105

CasadoCódigo Capítulo6. CriandooPlayer
}
private void setButtonspPosition() {
// Posição dos botões
leftControl.setPosition(screenResolution(
CGPoint.ccp( 40 , 40 ))) ;
rightControl.setPosition(screenResolution(
CGPoint.ccp( 100 , 40 ))) ;
shootButton.setPosition(screenResolution(
CGPoint.ccp( screenWidth() -40 , 40 )));
}
Nessemomentooscontrolesjáestãonateladojogo.Reparequeodesenvolvi-
mentodejogosno Cocos2Dvaisendoemfun çãosemprede Spritese Camadas
atéaqui.Apartirdeagoraentraremosmaisnaquestãoderesponderaosinputcom
mudançasnatela.Écomonoprotótipocriadonoiníciodolivro,noqualmovimen-
tamosoplayerapartirdotouch.Porémnessecaso,ocódigoseráumpoucomais
aprofundado.
Paraprepararessecenário,criaremosummétodo buttonClicked.Paraesse
momento,apenasfaremosologdadire çãorecebidapeloinputedodocliqueno
botãodeatirar.
@Override
public void buttonClicked(Button sender ) {
if (sender.equals(this.leftControl)) {
System.out.println("Button clicked: Left" );
}
if (sender.equals(this.rightControl)) {
System.out.println("Button clicked: Right" );
}
if (sender.equals(this.shootButton)) {
System.out.println("Button clicked: Shooting!" );
}
}
95

## Página 106

6.2. Botõesdecontrole CasadoCódigo
Porfim,énecessárioadicionaressacamadadebotõesàteladojogo,ouseja,na
classe GameScene.
private GameScene(){
GameButtons gameButtonsLayer = GameButtons.gameButtons();
this.addChild(gameButtonsLayer);
this.addChild(gameButtonsLayer);
}
Figura6.3:Controlesdedire çãoetiro.
Imagensposicionadasepreparadas.Horadecome çaraa ção!
96

## Página 107

CasadoCódigo Capítulo6. CriandooPlayer
6.3 A tirando
Falaremosagoradeumapartedojogoquepodeparecersimplesaprincípio,mas
temimpactoemmuitaspartesdojogoparaquefuncione,otiro! Paraqueanave
atire,precisaremosdeumasériedecoisas,portanto,vamosprimeirolistaroque
seránecessárioparaorganizaropensamentoantesdeirparaocódigo.
• Umnovoasset,ouseja,imagemdotiro
• Umaclassequerepresenteotirocomoum Sprite
• Definiroposicionamentodotironatela
• Umaengineresponsávelporcriarumtiro
• Umacamadanateladojogoparaostiros
•Associarotiroeoplayer,paraqueotirosaiadoplayer
Hámuitacoisaparaqueotirodefatoaconte ça,porém,selistarmoscadauma
dessasdependênciaspodemossimplificarodesenvolvimento. Iniciaremosadicio-
nandoafiguradotironaclasse Assets.
public class Assets {
public static String SHOOT = "shoot.png";
}
Podemosiniciaraprograma çãodotiro.Antesdepensaremfazeranaveatirar
oualgoassim,vamostentarpensaremprograma çãooqueéotiro. Otiroéum
sprite,ouseja,umaimagem,queandapelateladebaixoparacima. Ouseja,uma
vezqueumtiroaparecenatela,precisamosmovimentá-loparacimacomopassar
dotempo.
Parageraressasensa çãodemovimentoecontrolaresses updatesdoposiciona-
mentodotironoeixovertical,criaremosummétodocomonome update{}.Esse
métodoseráexecutadopelo Cocos2Dacadaintera ção.Oframeworkmandacomo
parâmetroumtempodeexecu ção,paraquepossaseranalisadosealgodeveserou
nãoexecutadodesdeaúltimavezqueeleinvocouessemétodo.Nonossocaso,esse
parâmetronãoseráutilizado,poisalógicadotiroépelotoquenobotãoenãopor
umaregradetempo.
Aclassedetiroprecisamanterolinkcomateladejogo,entãoutilizaremoso
delegate. Criaremostambémummétodochamado start(),queseráutilizado
paraverificarqueotiroestáfuncionando.
97

## Página 108

6.3. Atirando CasadoCódigo
public class Shoot extends CCSprite{
private ShootEngineDelegate delegate ;
float positionX, positionY;
public Shoot(float positionX, float positionY){
super(Assets.SHOOT);
this.positionX = positionX;
this.positionY = positionY;
setPosition(this.positionX, this.positionY);
this.schedule("update");
}
public void update(float dt) {
positionY += 2;
this.setPosition(screenResolution(
CGPoint.ccp(positionX, positionY )));
}
public void setDelegate(ShootEngineDelegate delegate ) {
this.delegate = delegate;
}
public void start() {
System.out.println("shoot moving!" );
}
}
Assimcomofizemoscomosmeteoros,teremosumaclasseresponsávelporco-
locarotironojogo.Essaresponsabilidadenãoédateladejogoenemdopróprio
tiro.Aclasse ShootEngineDelegatefaráessepapel. Paraisso,criaremosuma
interfacequedizoqueumaenginedetirodevesaberfazer.Nessecaso,criarostiros.
public interface ShootEngineDelegate {
public void createShoot(
Shoot shoot );
}
98

## Página 109

CasadoCódigo Capítulo6. CriandooPlayer
Tiro e tela de jogo
Atéaqui,aclassedetirofoidefinida.Agoravamosàteladojogoparaadicionar
essenovoelemento. Duascoisassãonecessáriasnessemomento. Aprimeiraéa
camadado Cocos2Dparaqueostirosapare çam.Asegundaéumarrayqueguardará
ostirosparaqueadetec çãodacolisãocomosmeteorossejafeita.
private CCLayer shootsLayer ;
private ArrayList shootsArray ;
Alémdecriarasvariáveis,énecessárioinicializá-las.Noconstrutorcriaremosa
camada.
private GameScene(){
this.shootsLayer = CCLayer.node();
this.addChild(this.shootsLayer);
this.setIsTouchEnabled(true);
}
Enométodo addGameObjects()criaremosoarray.Aproveitaremosessemo-
mentoparafecharolinkdo delegateentretiroeteladejogo.
private void addGameObjects() {
this.shootsArray = new ArrayList();
this.player.setDelegate(this);
}
Atirando!
játemosaclassedotiroetambémaprepara çãonateladejogoparaolinkentre
essesdoisobjetos.Oquefizemosatéaquifoiprepararainfraparaqueotiroaconte ça.
Vamosnosconcentraragoranarela çãoentreotiroeoPlayer.
Nessemomento, implementaremosainterface ShootEngineDelegatena
GameScene.Dessaforma,ateladejogosaberáoquedevefazerquandoforrequi-
sitadaparaatirar.Ainterfaceobrigaacria çãodométodo createShoot().Nele,
umnovotiro,queérecebidocomoparâmetro,éadicionadoàcamadaeaoarrayde
tiros.Alémdisso,chamaométodo start()daclasse Shoot,permitindoqueela
controleoquefornecessárioládentro.
@Override
public void createShoot(Shoot shoot ) {
99

## Página 110

6.3. Atirando CasadoCódigo
this.shootsLayer.addChild(shoot);
shoot.setDelegate(this);
shoot.start();
this.shootsArray.add(shoot);
}
Criaremostambém,aindana GameScene,ummétodochamado shoot(),que
chamaoplayer.Precisamosdissoporumfatomuitoimportante,queéoposiciona-
mentoinicialdotiro.Lembre-sequeotirodevesairdanave,portantooPlayereseu
posicionamentosãomuitoimportantes.Ométodo shootéummétododaclasse
Player,quecontémtodasasvariáveisdeposicionamentodanavenahoradotiro.
public boolean shoot() {
player.shoot();
return true ;
}
Apertando o botão!
Aclasse GameButtonséacamadaquerecebeoinputdousuário,ouseja,o
momentoemqueobotãoépressionado,econsequentementeotirodisparado.
Elaprecisaterumlinkcomateladejogo,paraqueapósumtoquenobotãoser
identificadoumaa çãoocorra. Nessecasoobotãochamarámétodo shoot()da
teladejogo,queseencarregarádedarsequênciaaotiro.
Ocódigodolinkentrecamadadebotõeseteladejogoficacomoaseguir.
private GameScene delegate ;
public void setDelegate(GameScene gameScene ) {
this.delegate = gameScene;
}
Ocódigoquedetectaotoquenobotãodetiroechamaodisparoficaassim:
if (sender.equals(this.shootButton)) {
this.delegate.shoot();
}
100

## Página 111

CasadoCódigo Capítulo6. CriandooPlayer
Player atirando
Tudoprontoparaatirarapartirdobotãodetiropressionado!Temosaclassede
tirodefinida,obotãodetiroprogramadoeateladejogocomacamadaemétodos
necessáriosprontos.precisamosquealguémdêocomandodeatirarenadamelhor
queopróprioPlayerparafazerisso!OPlayerteráométodo shoot()quecaptura
oposicionamentodanaveechamaa enginedecriaçãodotiro.Bang!
public class Player extends CCSprite{
private ShootEngineDelegate delegate ;
float positionX = screenWidth()/2;
float positionY = 50;
public Player(){
super(Assets.NAVE);
setPosition(positionX, positionY);
}
public void shoot() {
delegate.createShoot(
new Shoot(positionX, positionY));
}
public void setDelegate(ShootEngineDelegate delegate ) {
this.delegate = delegate;
}
}
101

## Página 112

6.4. Movendooplayer CasadoCódigo
Figura6.4:Playeratirando.
6.4 M ovendo o player
Vamosfecharessecapítulocomumadaspartesmaisimportantesdojogo. Após
atirar,moveremosoPlayerparaesquerdaedireita.Utilizaremosamesmaestratégia
deatirar,masagoraascoisasserãomaissimples.
Parainiciar,o Playerdevesabersemover.Movimentaroplayeréfazercom
quesuaposi çãoYsejaatualizadaquandoumeventofordetectado.
Na classePlayer.javaadicionaremosdoisnovosmétodos,quequandocha-
mados,mudamaposi çãohorizontaldanave.
public void moveLeft() {
102

## Página 113

CasadoCódigo Capítulo6. CriandooPlayer
if(positionX > 30){
positionX -= 10;
}
setPosition(positionX, positionY);
}
public void moveRight() {
if(positionX <screenWidth() - 30){
positionX += 10;
}
setPosition(positionX, positionY);
}
Na GameScenecriaremosmétodosparaqueessasa çõessejamchamadaspelos
botões.
public void moveLeft() {
player.moveLeft();
}
public void moveRight() {
player.moveRight();
}
Eporfim,na GameButtons,invocamososmétodosparaqueaposi çãodanave
sejaalterada.
@Override
public void buttonClicked(Button sender ) {
if (sender.equals(this.leftControl)) {
this.delegate.moveLeft();
}
if (sender.equals(this.rightControl)) {
this.delegate.moveRight();
}
if (sender.equals(this.shootButton)) {
this.delegate.shoot();
}
}
103

## Página 114

6.5. Conclusão CasadoCódigo
Aorodaroprojeto,devemosteranavesemovimentandoapartirdostoquesno
comandodecontroledanave. Alémdissoelajáatiradeacordocomaposi çãodo
Player.
6.5 C onclusão
Esseéumcapítulomuitoimportanteparaodesenvolvimentodojogo. Alémde
usardiversoselementosdoframework Cocos2D,comocamadas,spriteseagen-
damento(update),diversosconceitosdejogosforamusados,alémdepráticascomo
delegateseengines.
Ojogodeveestarcomonafiguraabaixo.
Figura6.5:14bisatirandocontraosmeteoros.
104

## Página 115

CasadoCódigo Capítulo6. CriandooPlayer
Éhoradeverificarascolisões!
105

## Página 117

Capítulo7
Detectandocolisões,pontuandoe
criandoefeitos
Colisõessãoocora çãodosgames.Sejaumsocodeumpersonagemnooutro,seja
opersonagemprincipalcapturandoalgumelemento,oucomonojogoqueestamos
programando,umtiroqueatingeummeteoro.
Detectarqueumelementoencostouemoutroéumassuntoquepodesermuito
complexo.Comomostradonocapítulodoprotótipoquedesenvolvemos,podemos
detectarcolisõesconsiderandofigurasgeométricasemvoltadoselementosparafa-
cilitar.
Nocapítuloatual,detectaremoscolisõesemduassitua ções.
• Quandoumtiroatingeummeteoro
• Quandoummeteoroatingeoavião(gameover)
Veremosaquiquemaisumavezutilizarumframeworkdedesenvolvimentode
jogoscomoo Cocos2Dajudamuitonessetrabalho.

## Página 118

7.1. Detectandocolisões CasadoCódigo
Umavezdetectadasascolisões,utilizaremososefeitosdo Cocos2Dparagerar
umaanimaçãoquandoadetec çãoocorrer. Emoutraparteimportantedessecapí-
tulo,falaremossobreaatualiza çãodoplacar.Essadeveserumapartetranquilapois
utilizaráconceitosjávistosanteriormente,como camadase sprites.
Essecapítulotraránovoscódigosemaisutiliza çãodoframework Cocos2D,
sendoumcapítulochaveparaodesenvolvimentodojogo.
7 . 1 D etectando colisões
Aprimeiracoisaqueprecisamosparaidentificaracolisãoentreobjetosnogameé
definirumaestratégiaparaisso.Nessejogo,aestratégiaseráanalisarumgrupode
objetosemumarray,comcadaobjetodeumoutrogrupo.Ouseja,dadosdoisarrays,
verificarsealgumelementodeumarraysobrepõeoutro.
Criaremosumarrayparaoplayerque,inicialmente,teráumúnicojogador.
private List playersArray ;
Eadicionaremosesseplayernoarraydeobjetos. Maisprafrentevocêpoderá
evoluirojogoecontrolarmaisdeumplayer.
private void addGameObjects() {
this.playersArray = new ArrayList();
this.playersArray.add(this.player);
}
Definindo as bordas
Precisamosagoradeumaformadedefinirasbordasoulimitesdotiro,danave
edosmeteoros,paraquesejapossívelfazeradetec çãodacolisão.
Noprotótipo,utilizamosaestratégiadecírculos.Paraojogoatual,utilizaremos
umaestratégiadequadradosouretângulos.
Comoestamosutilizandoo Cocos2Deseus Spritespodemosmaisfacil-
menteconseguiressasinforma ções.
Criaremosummétodoquereceberáum Spriteedevolveráumretângulo,
queconteráasbordasdoelemento. Paraisso,utilizaremosummétodoqueexiste
nospróprios Spriteschamado getBoundingBox().Essemétododevolveumtipo
CGRect,tambémdo Cocos2D,querepresentaoscontornosdafiguramapeados
emformaretangular.
108

## Página 119

CasadoCódigo Capítulo7. Detectandocolisões,pontuandoecriandoefeitos
Paratrabalharcomessainforma ção,precisaremostambémsaberaposi çãodo
elementonatela,eentãoutilizaremosoutrotipochamado CGPoint.
Comessemétodo,teremostodasascoordenadasdoposicionamentodoobjeto
aseranalisado.
public CGRect getBoarders(CCSprite object ){
CGRect rect = object.getBoundingBox();
CGPoint GLpoint = rect.origin;
CGRect GLrect = CGRect.make(GLpoint.x, GLpoint.y, rect.size.width,
rect.size.height);
return GLrect;
}
Checando a colisão
Umavezquejáconseguimososvaloresdeumelementodojogo,suasbordas
eposiçãonatela,podemosutilizaraestratégiaquefalamosnocome çodocapítulo
paraidentificarseumelementocolidecomoutroduranteojogo.
Criaremosummétodoimportanteparachecarascolisões,queprecisadealguns
parâmetrosparafuncionar. Osdoisprimeirossãoarraysdeobjetosaseremveri-
ficados. Ouseja,sequeremoschecarseostirosestãocolidindocomosmeteoros,
passaremosessesdoisarrays. Outropontoimportanteépassarumareferênciada
teladejogo,nocasoa GameSCene. precisamosdissoparapoderexecutaralgum
métodocasoacolisãosejadetectada,porémcomodiversascolisõespodemserde-
tectas,comonavecomtirooutirocommeteoro,issoserádecididoemtempode
execução. Éexatamenteporissoqueprecisamos,porúltimo,deumparâmetroa
mais,querecebeonomedométodoaserexecutadonocasodeacolisãoacontecer.
Oqueteremosentãoéumaverifica çãodecadaelementodoprimeiroarray,com
cadaelementodosegundoarray. Casoadetec çãoaconte ça,faremosumlogpor
enquanto,emostraremosquaiselementostiveramacolisão.
Na GameSceneteremosocódigoaseguir.
private boolean checkRadiusHitsOfArray(List<? extends CCSprite> array1,
List<? extends CCSprite> array2, GameScene gameScene , String hit ) {
boolean result = false;
for (int i = 0; i < array1.size(); i++) {
109

## Página 120

7.1. Detectandocolisões CasadoCódigo
// Pega objeto do primeiro array
CGRect rect1 = getBoarders(array1.get(i));
for (int j = 0; j < array2.size(); j++) {
// Pega objeto do segundo array
CGRect rect2 = getBoarders(array2.get(j));
// Verifica colisão
if (CGRect.intersects(rect1, rect2)) {
System.out.println("Colision Detected: " + hit);
result = true;
}
}
}
return result;
}
Tendoométodoqueidentificaacolisãocomofizemos,podemosutilizá-loparaa
verificaçãodedoisarraysquaisquer.Faremosachamadaaeleparadetectarcolisões
entretirosemeteoroseentremeteoroseanave.Essemétododeveserchamadode
temposemtempospelo Cocos2D,portanto,utilizaremosmaisumavezoagenda-
mentodoframework,passandoessemétodoparao schedule.
Aindana GameScenefaremosessaschamadas.
public void checkHits(float dt) {
this.checkRadiusHitsOfArray(this.meteorsArray,
this.shootsArray, this, "meteoroHit");
this.checkRadiusHitsOfArray(this.meteorsArray,
this.playersArray, this, "playerHit");
}
Comocitadoanteriormente,agendaremosométododechecagemdecolisões.
Paraisso,ométodo schedulereceberáométodocheckHitscomoparâmetro.
public void onEnter() {
super.onEnter();
this.schedule("checkHits");
this.startEngines();
}
110

## Página 121

CasadoCódigo Capítulo7. Detectandocolisões,pontuandoecriandoefeitos
Rodeojogoagorareparenoconsole(LogCat)doEclipse.Acolisãojáestásendo
detectada,eportanto,podemospartirparaatualizaroplacarefazerosefeitosne-
cessários!
7 . 2 E feitos
Nomomentoquedetectamosquedoisobjetosdojogocolidiram,algumascoisas
devemserfeitas.Vamoslistarparafacilitarofluxoaseguir.
• Executarumaanimação,comoexplosãoousimilares
• Removeroselementosdosarrays
• Atualizaroplacaroumostrarteladegameover
Vamoscomeçarpelaanima ção. Existemdiversaspossibilidadesdeanima ção
utilizandoo Cocos2D.Oframeworkoferecealgunsefeitostradicionaiscomo f a d e
e scale.Aideiaéconfigurarumasériedea ções,quejuntaseemumespa çocurtode
tempo,criamumaanima ção.
Paraoprimeiroexemplo,vamosanimarometeoroquandoéatingidopelotiro.
Nessemomento,animaremosometeoroparaquefiquepequeno,dandoaimpressão
quesumiuporseratingido.
Oquefaremosabaixoé:
• Reduziraescaladetamanhodaimagem
• Retirardatelacomumefeitoleve,chamadofade out
• Rodarambasemsequência
Apósrodarasequênciadeanima ções,precisamosretirardoarrayometeoroda
memória,poiselenãoexistemais.Precisamostambémpararoagendamentodesse
objeto,querodadetemposemtemposatualizandoaposi çãoegerandoomovi-
mento.
Primeiramente,vamosalterarnossainterface MeteorsEngineDelegatepara
queelarecebaanotifica çãodequandoummeteorocolidiu:
111

## Página 122

7.2. Efeitos CasadoCódigo
public interface MeteorsEngineDelegate {
public void createMeteor(
Meteor meteor , float x, float y, float vel,
double ang, int vl);
public void removeMeteor(Meteor meteor );
}
Na nossa classeMeteor,definimosqueelapoderáterumdelegate,queserá
avisadodascolisões:
public class Meteor extends CCSprite {
private MeteorsEngineDelegate delegate ;
public void setDelegate(MeteorsEngineDelegate delegate ) {
this.delegate = delegate;
}
// restante do código
}
Agora,nanossa GameScene,todavezquecriarmosumnovo Meteor,quere-
mosqueeleaviseaprópria GameScenedequeelefoiremovido.Emoutraspalavras,
a GameSceneseráodelegatedo Meteor.Altereo createMeteorparaqueele
invoqueo setDelegate:
@Override
public void createMeteor(Meteor meteor , float x, float y, float vel,
double ang, int vl) {
meteor.setDelegate(this);
this.meteorsLayer.addChild(meteor);
meteor.start();
this.meteorsArray.add(meteor);
}
Teremosumnovométodona Meteor,queseráinvocadoquandohouveraco-
lisão:
public void shooted() {
this.delegate.removeMeteor(this);
// para de ficar chamando o update
this.unschedule("update");
112

## Página 123

CasadoCódigo Capítulo7. Detectandocolisões,pontuandoecriandoefeitos
float dt = 0.2f;
CCScaleBy a1 = CCScaleBy.action(dt, 0.5f);
CCFadeOut a2 = CCFadeOut.action(dt);
CCSpawn s1 = CCSpawn.actions(a1, a2);
CCCallFunc c1 = CCCallFunc.action(this, "removeMe");
this.runAction(CCSequence.actions(s1, c1));
}
Nométodoacimaretiramosolinkentreoobjetoeateladejogo,cancelamoso
agendamentodaatualiza çãodeposi çãoecriamosasa çõesquejuntasfarãooefeito
desumirdometeoro.
O Cocos2Dpossuiaindaummétodoquepodeserinvocadoparaqueoobjeto
sejaliberadoecoletado.Essemétodoéo removeFromParentAndCleanup()e
seráinvocadologoapósaanima çãoacabar. Fazemosissovia CCCallFuncpois
queremosqueométodo removeMesejainvocadodepoisdeaanima çãoterminar.
public void removeMe() {
this.removeFromParentAndCleanup(true);
}
Animando o tiro
Utilizaremosomesmopensamentoparaanimarotiroquandocolidircomum
meteoro.Paraisso,criaremosométodo explode()naclasse Shoot.java,alte-
randoapenasalgunsparâmetros.
Essemétodoteráqueexecutaralgumasa ções:
• Retiraroobjetometeorodoarray
• Pararoagendamentodamovimentaçãodometeoro
• Animaraexplosãodometeoro
• Limparoobjetodamemória
Faremosissonométodoaseguir:
public void explode() {
// Remove do array
113

## Página 124

7.2. Efeitos CasadoCódigo
this.delegate.removeShoot(this);
// Para o agendamento
this.unschedule("update");
// Cria efeitos
float dt = 0.2f;
CCScaleBy a1 = CCScaleBy.action(dt, 2 f);
CCFadeOut a2 = CCFadeOut.action(dt);
CCSpawn s1 = CCSpawn.actions(a1, a2);
// Função a ser executada após efeito
CCCallFunc c1 = CCCallFunc.action(this, "removeMe");
// Roda efeito
this.runAction(CCSequence.actions(s1, c1));
}
Para limpar o objeto da memória, chamaremos novamente o método do
Cocos2Dchamado removeFromParentAndCleanup. Reparequeelefoicha-
madonocódigoacima,naformadestring.
public void removeMe() {
this.removeFromParentAndCleanup(true);
}
Játemosocódigoqueometeorodeveexecutarquandoumacolisãofordetec-
tada. Agoraprecisamosfazerachamadaaelenosmomentodecolisão. Voltando
àclasse GameScenetemosométodo checkRadiusHitsOfArray,quepercorre
doisarrayseverificaintersec ções.
Nessemétodo,quandodoisobjetosestiveremcolidindo,algodeveserfeito.Essa
éumaparteimportantedojogoeprecisademuitocuidado. Reparequeonosso
métododedetecçãoégenérico,ouseja,elerecebedoisarraysdeobjetoseanalisa
seocorrecolisãoentreeles.Nomomentoqueessacolisãoédetectada,eleprecisará
executaralgoquepodeseraexplosãodanave,ouaexplosãodeummeteoro.
Éimportanteperceberqueadecisãodequalmétodorodarapósdetectadaaco-
lisãoéemtempodeexecu ção,eprecisaremosinvocá-lovia reflection.
Na classeGameScenealtereométodo checkRadiusHitsOfArray:
114

## Página 125

CasadoCódigo Capítulo7. Detectandocolisões,pontuandoecriandoefeitos
if (CGRect.intersects(rect1, rect2)) {
System.out.println("Colision Detected: " + hit);
result = true;
Method method ;
try {
method = GameScene.class.getMethod(hit,
CCSprite.class, CCSprite.class);
method.invoke(gameScene, array1.get(i),
array2.get(j));
} catch (SecurityException e1 ) {
e1.printStackTrace();
} catch (NoSuchMethodException e1 ) {
e1.printStackTrace();
} catch (IllegalArgumentException e ) {
e.printStackTrace();
} catch (IllegalAccessException e ) {
e.printStackTrace();
} catch (InvocationTargetException e ) {
e.printStackTrace();
}
}
Apartirdaqui,bastafazeraschamadasaosmétodos shootede explode.Na
classe GameSceneadicioneométodo meteoroHit():
public void meteoroHit(CCSprite meteor , CCSprite shoot ) {
((Meteor) meteor).shooted();
((Shoot) shoot).explode();
}
Rodeoprojetoetesteoquefizemosatéaqui!
Removendo objetos
Precisamoslembrarqueemboraosobjetosnãoestejammaisaparecendonatela
elescontinuamalocadosnamemória,ouseja,aindanãoforamremovidos. Cria-
remosagoraocódigoqueeliminaráosobjetosdosarraysapóscolisãoentretiroe
meteoro.
115

## Página 126

7.3. Playermorre CasadoCódigo
Iniciaremosadicionandoduasdeclara çõesnasinterfaces. Aprimeiraseráa
MeteorsEngineDelegate,ondeadicionaremosométodo removeMeteor:
public interface MeteorsEngineDelegate {
public void createMeteor(
Meteor meteor , float x, float y, float vel, double ang,
int vl);
public void removeMeteor(Meteor meteor );
}
Easegundaéainterface ShootEngineDelegatequeteráadefini çãodo
removeShoot:
public interface ShootEngineDelegate {
public void createShoot(
Shoot shoot );
public void removeShoot(Shoot shoot );
}
Feitoisso,bastafazeraremo çãodosobjetosnaclasse GameScene,criandoos
métodos removeMeteore removeShoot:
@Override
public void removeMeteor(Meteor meteor ) {
this.meteorsArray.remove(meteor);
}
@Override
public void removeShoot(Shoot shoot ) {
this.shootsArray.remove(shoot);
}
7 . 3 P layer morre
Utilizandoamesmaestratégiavamosanimaroplayerquandoummeteorocolidir
comele.Paraisso,naclasse Playerteremosométodo explodecomoabaixo:
public void explode() {
// Para o agendamento
116

## Página 127

CasadoCódigo Capítulo7. Detectandocolisões,pontuandoecriandoefeitos
this.unschedule("update");
// Cria efeitos
float dt = 0.2f;
CCScaleBy a1 = CCScaleBy.action(dt, 2 f);
CCFadeOut a2 = CCFadeOut.action(dt);
CCSpawn s1 = CCSpawn.actions(a1, a2);
// Roda os efeitos
this.runAction(CCSequence.actions(s1));
}
Paraquesejaexecutado,crieométodo playerHitnaclasse GameScene:
public void playerHit(CCSprite meteor , CCSprite player ) {
((Meteor) meteor).shooted();
((Player) player).explode();
}
Rodeoprojetoeverifiqueateladojogo!
7 . 4 P lacar
Parafecharessecapítulovamosadicionarumapontua çãoparacadameteorodes-
truídoapósseratingidoporumtiro.Utilizaremosalgunsconceitosjávistosanteri-
ormente.
Primeiramente,trataremosovalordepontosqueaparecenatelacomoumanova
camada,ecamadasparao Cocos2Dsãoclassesqueherdamde CCLayer.
Essacamadaapresentaráospontosemnúmeroparaojogador.paraisso,preci-
samosdeduasvariáveis.Aprimeiraédotipointeiro,queguardaospontosatuais.
Asegundaéumcampodetextoparacolocaressevalornatela.
Alémdisso,veremoscomoutilizarumtipodeletra( font type)diferentepara
fazerisso.Existeno Cocos2Dumaclassechamada CCBitmapFontAtlas.Essa
classepossuiummétodochamado bitmapFontAtlasque recebe uma string e
umafonteaserusada.
Depoisdisso,bastaconfigurarotamanhodaletraeposicionamento.Crieaclasse
Score.
public class Score extends CCLayer {
private int score;
117

## Página 128

7.4. Placar CasadoCódigo
private CCBitmapFontAtlas text ;
public Score(){
this.score = 0;
this.text = CCBitmapFontAtlas.bitmapFontAtlas(
String.valueOf(this.score),
"UniSansSemiBold_Numbers_240.fnt");
this.text.setScale((float) 240 / 240);
this.setPosition(screenWidth()-50, screenHeight()-50);
this.addChild(this.text);
}
}
Alteraremosovalordavariável scorecomummétodochamado increase.
Essemétodopoderáserchamadosemprequeumacolisãoentretiroemeteorofor
detectada.
Seucódigoésimples,apenasincrementaavariável scoreeconfiguranova-
menteotextodoplacar.
public void increase() {
score++;
this.text.setString(String.valueOf(this.score));
}
Invoque oincreasetodavezqueummeteoroforatingindo,modificandoo
meteoroHit:
public void meteoroHit(CCSprite meteor , CCSprite shoot ) {
((Meteor) meteor).shooted();
((Shoot) shoot).explode();
this.score.increase();
}
Agoraquetemosacamadadoplacarpreparada,vamosadicioná-laàtelaprinci-
pal.Paraisso,criaremosdoisobjetos,umdotipo CCLayereoutrodotipo Score.
Na classeGameSceneadicione:
private CCLayer scoreLayer ;
private Score score ;
118

## Página 129

CasadoCódigo Capítulo7. Detectandocolisões,pontuandoecriandoefeitos
Énecessárioiniciaracamadaeadicioná-laatela. Noconstrutordaclasse
GameSceneadicione:
this.scoreLayer = CCLayer.node();
this.addChild(this.scoreLayer);
Faça a chamada ao método increase ná última linha do método
meteoroHit,naclasse GameScrene:
public void meteoroHit(CCSprite meteor , CCSprite shoot ) {
((Meteor) meteor).shooted();
((Shoot) shoot).explode();
this.score.increase();
}
Parafinalizar,bastacriaroobjetodotipo Scoreeadicionaracamadacorres-
pondente.
Ainda na classe GameScene adicione essa chamada ao método
addGameObjects:
private void addGameObjects() {
//...
// placar
this.score = new Score();
this.scoreLayer.addChild(this.score);
}
7 . 5 C onclusão
Detectarcolisõesdeformamanual,comofeitonocapítulodoprotótipo,nãoétão
simpleseenvolvemuitoscálculosmatemáticos. Porém,utilizandoumframework
comoo Cocos2Dascoisassãofacilitadas.
Nessecapítulopassamospeloquepodeserconsideradoocora çãodojogo,a
detecçãodecolisões.Apartirdelas,executamosefeitoseatualizamosatelaparao
jogador.
Opróximocapítulotratarádeumapartemuitoimportanteparadarvidaaos
jogos,ossonseefeitos.
119

## Página 131

Capítulo8
Adicionandosonsemúsica
Ossonssãodefundamentalimportâncianodesenvolvimentodeumgame. Hoje
existemprofissõescomo sound designersquetrabalhamespecificamentecriandoos
sonsdosgames.Muitosjogosutilizamorquestrasparaexecutarsuatrilhasonora.
Amúsicadávidaaojogo,torna-omaisdivertidoedárespostasaojogadorpara
aspartesimportantes.
Existemduasformasprincipaisdesonsnomundodosgames:músicaeefeitos.
Quandoojogocome çaumamúsicadefundonormalmentedáoclimadojogo.
Essamúsicaénormalmenteexecutadaembackgroundeserepeteinúmerasvezesao
longodogame.Alémdela,existemosefeitosdesomgeradosemmomentosimpor-
tantes,comoquandoumacolisãoédetectadaouquandooplacaréalterado
Paraonossojogo,utilizaremossonsencontradosgratuitamentenosite http://
www.freesound.org/.Vocêpodebuscardiversostiposdesonsnessesiteparaoseu
próximogame!

## Página 132

8.1. Executandosons CasadoCódigo
8.1 E xecutando sons
Nessaprimeiraetapautilizaremosoframework Cocos2Dparaadicionarsoma3
eventosdojogo.Utilizaremos3arquivosdesonsdiferentes:
• Disparodeumtiro
• Colisãodotirocomummeteoro
• Colisãoentremeteoroeavião
Podemosutilizarosformatosmaiscomunsparaadicionarsonsaonossojogo,e
aquioformatoescolhidoserá wav.Colocaremosossonsnodiretório res/rawdo
nossoprojeto.
Vocêpodeencontrartodosossonsqueserãoutilizadosnessecapítulonesselink:
https://github.com/andersonleite/jogos_android_14bis/tree/master/res/raw
SoundEngine
Para lidar com sons, o Cocos2D disponibiliza uma classe chamada
SoundEngine.Essaclassepossuidiversosmétodosparatrabalharcomsonsemú-
sicanogame. Paratrabalharcomessaclassenãoénecessáriocriarumainstância
massim,utilizarum Singletondisponibilizadopeloframework. Paraissoexecu-
tamos SoundEngine.sharedEngine()tendoacessoàsop çõesdesonsdeque
precisamos.
Comesseacesso,podemosexecutarmúsicasesons,parareiniciararquivosde
áudio,aumentarediminuirovolumeetc.Nessemomento,iniciaremosexecutando
3sonsutilizandoométodo playEffect().
Essemétodorecebecomoparâmetroareferênciaaoarquivodeáudiododire-
tório res/rawquepodeseracessadautilizandoo CCDirector.
Oprimeiroefeitodesom,otiro,serácolocadonaclasse Shoot. Adicioneo
códigoabaixoaométodo start():
public void start() {
SoundEngine.sharedEngine().playEffect(
CCDirector.sharedDirector().getActivity(), R.raw.shoot);
}
Opróximosomseráexecutadoquandodacolisãoentremeteoroetiro.Naclasse
Meteoradicioneocódigoabaixoaométodo shooted:
122

## Página 133

CasadoCódigo Capítulo8. Adicionandosonsemúsica
public void shooted() {
SoundEngine.sharedEngine().playEffect(
CCDirector.sharedDirector().getActivity(), R.raw.bang);
// ...
}
Parafinalizar,adicionaremosumsomquandoummeteoroatingiroavião.Na
classe Playeradicioneocódigoabaixoaométodo explode:
public void explode() {
SoundEngine.sharedEngine().playEffect(
CCDirector.sharedDirector().getActivity(), R.raw.over);
// ...
}
Agoraogamejáexecutaráossonsquandoumdos3eventosacima,tiroecoli-
sões,acontecerem!
8.2 C ache de sons
Vimoscomoexecutarsonsutilizandoo Cocos2D.Porém,vocêdeveterreparadoem
umproblemagrave.Aprimeiravezqueumdossonsprecisasertocado,eledemora
muito.Issosedeveaofatodoframeworkinicializarosomapenasnomomentoque
foinecessário.Existeumaestratégiaeboapráticaparasolucionaresseproblema,o
cachedesons.
Paracolocarumsomnocachedevemosiniciá-lojánoiníciodogame.Criare-
mosentãoummétodocomessaresponsabilidadenaclasse GameScenechamado
preloadCache. Essemétodofaráocachedos3sonsqueestamosutilizandoaté
aqui.
private void preloadCache() {
SoundEngine.sharedEngine().preloadEffect(
CCDirector.sharedDirector().getActivity(),
R.raw.shoot);
SoundEngine.sharedEngine().preloadEffect(
CCDirector.sharedDirector().getActivity(),
R.raw.bang);
123

## Página 134

8.3. Músicadefundo CasadoCódigo
SoundEngine.sharedEngine().preloadEffect(
CCDirector.sharedDirector().getActivity(),
R.raw.over);
}
Adicioneachamadadométodo preloadCachenoconstrutorda GameScene,
naúltimalinhadométodo:
preloadCache();
Rodenovamenteoprojetoeverifiquequeagoraossonsrespondemperfeita-
menteaomomentodostirosecolisões!
8.3 M úsica de fundo
Agoraquejátrabalhamoscomossonsdogame,vamosvercomolidarcomamúsica
dojogo.Amúsicaseráiniciadaquandoojogadorentrarnateladejogo.Paraisso,
usaremosamesmaclasse SoundEngineporémcomométodo playSound.
Noconstrutorda GameSceneadicioneachamadaamúsica.
SoundEngine.sharedEngine().playSound(
CCDirector.sharedDirector().getActivity(),
R.raw.music, true);
Outrométodoimportanteéométodoqueparaamúsica. Essemétodoécha-
mado pauseSound().Faremosissologoapósoefeitodeexplosãoentremeteoro
eaviãonaclasse Player:
public void explode() {
SoundEngine.sharedEngine().playEffect(
CCDirector.sharedDirector().getActivity(), R.raw.over);
SoundEngine.sharedEngine().pauseSound();
}
Rodeoprojetoevejacomoosomadicionavidaaojogo.Tiro,colisõesemúsica
devemestarfuncionandonessemomento!
124

## Página 135

CasadoCódigo Capítulo8. Adicionandosonsemúsica
8.4 C onclusão
Sonsemúsicasãomuitoimportanteparaosjogos. Reparenosjogosfamososou
mesmoosquevocêmaisgostaereparenatrilhasonora. Mesmoosjogosantigos
possuíamsonsmuitoespeciaisparacadajogo.
Éimportantíssimodefinirumaboatrilhasonoraeefeitosparaoseupróximo
game!
125

## Página 137

Capítulo9
Voandocomagravidade!
Omundodosgamesfoitotalmenterevitalizadocomos smartphones.Jogosque
atéentãoeramsimplesejánãoatraiammaistantoaaten çãodosjogadoresforam
remodeladoscomasnovaspossibilidadesdeexperiênciaqueosaparelhosmodernos
podemproporcionar.
Amaioriadosjogosquefazemsucessonoscelulareshojefazusodealgumre-
cursodoaparelho,como touch screen,arrastandoobjetosnatema,ouutilizando
agravidadecomoacelerômetro,emovimentandooselementosdeumamaneiradi-
ferentedosjogosparaconsoles.
Nessecapítulotrocaremosamovimenta çãodoaviãofeitaporbotõespelocon-
trolemovimentandoocelular! Aexperiênciaserálevadaaoutronível,nãomais
sendoumsimplesjogocombotões,massim,utilizandoumrecursonativodoapa-
relhoquefazaquelejogoganhemuitajogabilidade!
Aofimdocapítulo,nossoaviãopoderápercorreratela,ficandocomonafigura
aseguir:

## Página 138

9.1. UsandooAcelerômetro CasadoCódigo
Figura9.1:Controleporacelerômetro.
9.1 U sando o Acelerômetro
Vamosiniciarplanejandoousodoacelerômetroesabendoondequeremoschegar.
Nossoobjetivoéretirarosbotõesquemovimentamoaviãoparaesquerdaedireita.
Semessesbotões,moveremosoaviãoapartirdascoordenadasqueocelularcaptar
demovimentonoaparelho.Dividiremosessetrabalhoem3partesprincipais.
• Capturarascoordenadasdemovimentaçãohorizontaleverticaldoaparelho
• Controlarainstabilidadedomovimentodoavião
• Calibraressascoordenadasparaocontrolefuncionaremposiçõesdiferentes
128

## Página 139

CasadoCódigo Capítulo9. Voandocomagravidade!
Capturando as coordenadas
Aprimeiracoisaqueprecisamossaberécomoo Androidpodenosenviarinfor-
maçõesdoacelerômetro.Issoéfeitoatravésdainterface SensorEventListener.
Oqueocorrequandoumaclasseimplementaessainterface?
Toda classe que implementaSensorEventListener é obrigada a im-
plementar seus métodos, dentre eles oonSensorChanged(SensorEvent
acceleration). Oqueocorreaquiéqueacadamovimenta çãododevice,esse
métodoéchamadopelo Android.Reparequeaochamaressemétodo,o Android
passacomoparâmetroumobjetodotipo SensorEvent, quechamaremosde
acceleration.
Essaéumapartemuitoimportante,evocêdeverepararquecomesseobjetoque
chamamosde accelerationtemososvaloresdeposi çãodoaparelho.Essesvalo-
resserãoinformadosem3variáveis,querepresentamoseixosX,YeZdoaparelho,
comodemostradonafiguraaseguir.
Figura9.2:EixosX,YeZ.
Depossedessasinforma ções,conseguiremossaberseoaparelhosemoveupara
umdeterminadoladoeatualizaraposi çãodoavião.Essaéumaconclusãoimpor-
tante,ouseja,quandopercebemosqueocelularestáinclinadoparaumdeterminado
lado,atualizamosessaposi çãodoavião.
129

## Página 140

9.1. UsandooAcelerômetro CasadoCódigo
A classe Accelerometer
Vamosimplementaraclasseresponsávelporcapturaressesvalores.Maisàfrente
veremoscomofazerolinkentreelaeamovimenta çãodoavião.
Paracomeçarcriaremosaclasse Accelerometerqueimplementaainterface
SensorEventListener.Essainterfacenosobrigaaimplementar2métodos.Te-
remosocódigoabaixo:
public class Accelerometer implements SensorEventListener {
@Override
public void onAccuracyChanged(Sensor sensor , int accuracy) {
// TODO Auto-generated method stub
}
@Override
public void onSensorChanged(SensorEvent acceleration ) {
}
}
Vamos agora ver como capturar as posiçõe sXeYd oa pa r e lh o .P a r ai s so ,
criaremos2variáveisquevãoguardaressainforma çãoeatualizaremosométodo
onSensorChanged:
private float currentAccelerationX;
private float currentAccelerationY;
@Override
public void onSensorChanged(SensorEvent acceleration ) {
this.currentAccelerationX = acceleration.values[0];
this.currentAccelerationY = acceleration.values[1];
}
Oquetemosatéaqui? Umaclassequerecebeinforma çõesdemovimenta ção
doaparelho.Elanãofoiinicializadaainda,maslogomaispoderáserutilizadapara
atualizaraposi çãodanave.
Paracontinuar,faremosqueessaclassesecomportecomoum Singleton,
tendoapenasumobjetodotipo Accelerometernojogo. Paraisso,naprópria
classe Accelerometeradicioneoseguintecódigo:
130

## Página 141

CasadoCódigo Capítulo9. Voandocomagravidade!
static Accelerometer sharedAccelerometer = null;
public static Accelerometer sharedAccelerometer() {
if (sharedAccelerometer == null) {
sharedAccelerometer = new Accelerometer();
}
return sharedAccelerometer;
}
Dessaforma,nãocorremosriscosdemaisdeumobjetosdessetiposerinstan-
ciadonojogo.Agora,jápodemospensaremfazerolinkcomaclasse Player.
Configurando o player
Todavezqueoacelerômetroatualizarasposi çõesdevemosmoveroavião.Isso
ocorreráemumaquantidademuitograndedevezesporsegundo,dandoaimpres-
sãodemovimento. Comoemoutrasclasses,fazemoslinkentreelasutilizandoos
delegates,porémaquiteremosquecolocarmaisumacoisa.Todavezqueomé-
todo onSensorChangeddaclasse Accelerometerforexecutado,elechamaráa
classe PlayerinformandoascoordenadasXeY.
Paragarantirqueessemétodoexistanaclasse Playerumainterfaceserácriada.
Chamaremosessainterfacede AccelerometerDelegate.
public interface AccelerometerDelegate {
public void accelerometerDidAccelerate(float x , float y);
}
Eimplementaremosométodo accelerometerDidAcceleratena classe
Playerparareceberasatualiza çõesdoacelerômetro.Essemétodorecebecomopa-
râmetrosascoordenadasXeY,queiremosguardarnasvariáveis currentAccelXe
currentAccelX.Reparequeaoimplementá-lodeixaremosumlogparaentender
otipodevaloremqueascoordenadassãoenviadas.
public class Player extends CCSprite implements AccelerometerDelegate {
@Override
public void accelerometerDidAccelerate(float x, float y) {
System.out.println("X: " + x);
System.out.println("Y: " + y);
// Leitura da aceleracao
131

## Página 142

9.1. UsandooAcelerômetro CasadoCódigo
this.currentAccelX = x;
this.currentAccelY = y;
}
}
Vocêpodeexecutaroprojetoagoraeolharnoconsole(logcat)ascoordenadas
sendoimpressas.
Oquetemosnestemomento?Aclasse Accelerometerquerecebecoordena-
dasdoaparelhoeaclasse Playerpreparadaparareceberessesvaloresearmazená-
losemvariáveis.
Mas quando a classe Accelerometer chama o método
accelerometerDidAccelerate da classe Player? Para que isso ocorra
precisamosdeduascoisas. Aprimeiraéconfigurarodelegateentreelas,eentão
fazerachamadaaométodoemquestão.
Na classeAccelerometercrieodelegateeseu gettere setter:
private AccelerometerDelegate delegate ;
public void setDelegate(AccelerometerDelegate delegate ) {
this.delegate = delegate;
}
public AccelerometerDelegate getDelegate() {
return delegate;
}
Na classePlayercriaremosumareferênciaao Accelerometer:
private Accelerometer accelerometer ;
Temosabaseparafazerolinkentreasclasseseestamosquaseprontospara
inicializaroAcelerômetro.
Iniciando o Acelerômetro
Sabemosnessemomentocomoutilizaroacelerômetro,porém,paraterminaro
linkentreaclasse Accelerometerquerecebeascoordenadaseaclasse Player
quemoveráoavião,temosqueinicializaroacelerômetronojogo.
A dificuldade aqui é que o acelerômetro só pode ser inicializado por uma
Activity,eassimcomofizemosparautilizaro touch screen,teremosque
inicializá-loatravésda MainActivity.
132

## Página 143

CasadoCódigo Capítulo9. Voandocomagravidade!
Nela,inicializaremosoacelerômetroedeixaremosguardadasuareferênciana
classe DeviceSettings.
Paraisso,naclasse DeviceSettingsocódigoabaixo:
public class DeviceSettings {
private static SensorManager sensormanager ;
public static void setSensorManager(SensorManager sensormanager ) {
this.sensormanager = sensormanager;
}
public static SensorManager getSensormanager() {
return sensormanager;
}
}
Ena MainActivityfaçaaconfigura çãocriandoométodoaseguir:
private void configSensorManager() {
SensorManager sensorManager =
(SensorManager) getSystemService(Context.SENSOR_SERVICE);
DeviceSettings.setSensorManager(sensorManager);
}
Ométodo onCreateda MainActivitydeveiniciaressaconfigura ção:
@Override
protected void onCreate(Bundle savedInstanceState ) {
super.onCreate(savedInstanceState);
// orientacao vertical
setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_PORTRAIT);
requestWindowFeature(Window.FEATURE_NO_TITLE);
getWindow().setFlags(
WindowManager.LayoutParams.FLAG_FULLSCREEN,
WindowManager.LayoutParams.FLAG_FULLSCREEN);
// tela
CCGLSurfaceView glSurfaceView = new CCGLSurfaceView(this);
setContentView(glSurfaceView);
CCDirector.sharedDirector().attachInView(glSurfaceView);
133

## Página 144

9.1. UsandooAcelerômetro CasadoCódigo
// sensor
configSensorManager();
}
Link entre classes
Tendoaclasse Accelerometer,quecapturaascoordenadasconfiguradas,
aclasse Playerprontaparareceberosvaloreseoacelerômetroinicializadona
MainActivity,podemosfazerolinkentreelas.
Iniciaremoscriandoummétodoque,aoinicializaraclasse Accelerometer
buscaareferênciaaoacelerômetro.
Na classeAccelerometercrieocódigoabaixo:
private SensorManager sensorManager ;
public Accelerometer() {
this.catchAccelerometer();
}
public void catchAccelerometer() {
sensorManager = DeviceSettings.getSensormanager();
sensorManager.registerListener(this,
sensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER),
SensorManager.SENSOR_DELAY_GAME);
}
Aqui, buscamos o acelerômetro, e deixamos a classe pronta para ser cha-
mada pelo Android a cada movimentação do aparelho. Repare que a in-
terface SensorEventListener é genérica, ela pode também receber avisos
de outros sensores. Nesse caso, pedimos apenas o acelerômetro através do
sensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER). Há
diversosoutrossensorescomosquaisvocêpodeadicionarnovasfuncionalidades
aosseusjogos.
Jápodemosfazerachamadaàclasse Player,queéodelegate,epassarascoor-
denadas.Altereométodo onSensorChangednaclasse Accelerometercomoa
seguir:
@Override
public void onSensorChanged(SensorEvent acceleration ) {
this.currentAccelerationX = acceleration.values[0];
134

## Página 145

CasadoCódigo Capítulo9. Voandocomagravidade!
this.currentAccelerationY = acceleration.values[1];
// Envia leitura do acelerometro
if (this.delegate != null) {
this.delegate.accelerometerDidAccelerate(
currentAccelerationX, currentAccelerationY);
}
}
Na classePlayer,adicioneodelegatecomonocódigoaseguir:
public void catchAccelerometer() {
Accelerometer.sharedAccelerometer().catchAccelerometer();
this.accelerometer = Accelerometer.sharedAccelerometer();
this.accelerometer.setDelegate(this);
}
Quasetudopronto.Temosaquiaconfigura çãodo Androidparautilizaroace-
lerômetro,umaclasseresponsávelporbuscaressareferênciaeconseguirascoorde-
nadas,eolinkfeitoentreaclasse Playerparaquepossamosmovimentaroavião.
Masqueminicializoutudoisso?Ninguémainda,eutilizaremosnosso GameScene,
queéacentralizadora,parainiciaressanova feature.
Na classeGameSceneadicioneachamadaaométodo catchAccelerometer
nométodo startGame:
public void startGame() {
// Captura o acelerometro
player.catchAccelerometer();
}
Movendo o player
Agoraquejáestamosrecebendoascoordenadasdoacelerômetroeguardando-
asemvariáveisnaclasse Playerjápodemosmovimentá-lo.Ométodo updateé
quealteraaposi çãodoavião,então,vamosalterá-lo.
Aideiaaquiserámoverumadasquatropossíveiscoordenadasdoavião,sejaho-
rizontal(direitaouesquerda)ouvertical(paracimaeparabaixo). Ascoordenadas
enviadaspeloacelerômetroseguemopadrãodoseixos,fazendocomquemovimen-
taçõesparaumladosejamnúmerospositivoseparaoladoopostonúmeronegativo.
OmesmoocorreparaoeixoX,enviandonúmerospositivosparaumadire çãoene-
gativosparaaposi çãooposta.
135

## Página 146

9.2. Controlandoainstabilidade CasadoCódigo
Combasenessainforma ção,analisaremosascoordenasqueoacelerômetroen-
viouealteraremosaposi çãodoavião.
Na classePlayeraltereométodo update:
public void update(float dt) {
if(this.currentAccelX< 0){
this.positionX++;
}
if(this.currentAccelX> 0){
this.positionX--;
}
if(this.currentAccelY< 0){
this.positionY++;
}
if(this.currentAccelY> 0){
this.positionY--;
}
// Configura posicao do aviao
this.setPosition(CGPoint.ccp(this.positionX, this.positionY));
}
Jáépossívelrodarojogoeveroaviãosemovendoapartirdamovimenta çãodo
aparelho!Façaoteste.
Experimentedeixaratelaparalelaaumamesa.Algoestranho,não?Pareceque
eleestáenfrentandoumcerta“turbulência”.
9.2 C ontrolando a instabilidade
Vocêdeveterpercebidoqueocontroledoaviãoficouinstável.Issoocorreporque
nãoestamosusandonenhumatolerânciaparamoveroavião,ouseja,movemossem-
preindependentedeserumamovimenta çãorealmenteválidadoaparelho.Oace-
lerômetronãoéperfeito,alémdequeelepegamovimenta çõesminúsculas,sempre
gerandoeventos!
Paramelhorarisso,vamosusarumlimite.Emvezdecompararcomzero,uti-
lizaremosumaconstantedetolerância.Chamaremosessaconstantede NOISE.Ela
136

## Página 147

CasadoCódigo Capítulo9. Voandocomagravidade!
definiráovalormínimoqueoacelerômetrodeveseralteradopararealmentemover
oavião.
Altereométodo updateecriaaconstante NOISEnaclasse Player.
private static final double NOISE = 1;
public void update(float dt) {
if(this.currentAccelX< - NOISE){
this.positionX++;
}
if(this.currentAccelX> NOISE){
this.positionX--;
}
if(this.currentAccelY< - NOISE){
this.positionY++;
}
if(this.currentAccelY> NOISE){
this.positionY--;
}
// Configura posicao do aviao
this.setPosition(CGPoint.ccp(this.positionX, this.positionY));
}
Apartirdestemomento, devemosterumbomcontroledoavião, podendo
movimentá-loportodaatela.Oúnicoinconvenienteéquenãotemosumacalibra-
çãoparautilizaroacelerômetro,ouseja,elefuncionabemparaposi çãoinicialzero,
queéaaquelaquandodeixamosoaparelhoparadoemumamesa,porexemplo.
9.3 C alibrando a partir da posição inicialdo apa -
relho
Vamosutilizarumaestratégiadecalibra çãonojogo!Aideiaénãosebasearapenas
naposiçãoenviadapeloacelerômetroparamoveroplayer,masfazerantesalgumas
contasparaentenderaposi çãoqueojogadorestásegurandooaparelhoeconsiderá-
lacomoaposi çãoZERO,ouposi çãoinicial.
137

## Página 148

9.3. Calibrandoapartirdaposi çãoinicialdoaparelho CasadoCódigo
Paraissofaremosalgumasaltera çõesnaclasse Accelerometer. Criaremos
novasvariáveisqueserãoresponsáveisporguardarinforma çõessobreacalibra ção.
Essasvariáveisguardarãoasinformaçõesiniciaisesejátemosacalibra çãoconcluída.
Na classeAccelerometercrieasseguintesvariáveis:
private float calibratedAccelerationX;
private float calibratedAccelerationY;
private int calibrated;
Alteraremostambémométodo onSensorChanged. Nele,faremosumloop
quereceberáas100primeirasinforma çõesdoacelerômetro.Comesses100primei-
rosvaloresguardaremosaposi çãoinicialdoaparelho.
Porque100vezes?Oacelerômetrodemoraparaenviarascoordenadascorretas
doaparelho,eprecisamosesperarqueeletermineessetrabalhocomprecisão.Com
isso,conseguiremosdefinirqualaposi çãoinicialdoaparelho.
Apartirdisso,faremosumaaltera çãonovalorqueéenviadoparamoveroavião.
Aoinvésdeenviarovalordiretamenteinformadopeloacelerômetro,vamostirara
posiçãoinicial,paraterapenasamudan çarelativaàquelamovimenta ção.
Na classeAccelerometerométodo onSensorChangeddeveficarcomoa
seguir:
@Override
public void onSensorChanged(SensorEvent acceleration ) {
if(calibrated < 100){
this.calibratedAccelerationX += acceleration.values[0];
this.calibratedAccelerationY += acceleration.values[1];
System.out.println(acceleration.values[0]);
System.out.println(acceleration.values[1]);
calibrated++;
if (calibrated == 100 ) {
this.calibratedAccelerationX /= 100;
this.calibratedAccelerationY /= 100;
}
return;
}
138

## Página 149

CasadoCódigo Capítulo9. Voandocomagravidade!
// Leitura da aceleracao
this.currentAccelerationX =
acceleration.values[0] - this.calibratedAccelerationX;
this.currentAccelerationY =
acceleration.values[1] - this.calibratedAccelerationY;
}
Vocêpodemanteros logsporumtempoparaentenderosvaloresenviadose
depoisapagar. Nessemomentooaviãojádeveestarsendocontroladopelamovi-
mentaçãodoaparelho!
Retirando os botões
Provavelmentevocênãovaiquerermovermaisoaviãoutilizandoosbotõeses-
querdaedireita. Umaformasimplesderemovê-losécomentarasduaslinhasa
seguir,naclasse GameButtons:
// addChild(leftControl);
// addChild(rightControl);
9.4 D esafios com o acelerômetro
Utilizarrecursoscomoacelerômetropodetornarojogomuitomaisdivertidoeen-
gajador,sendodaquelesdetalhesquefazemaexperiênciadogamesertotalmente
única.Quetalmelhoraraindamaisessaexperiênciacomassugestõesabaixo?
• Controledevelocidade:Vocêpodefazerque,quantomaisinclinado,oavião
deslizemais.Seeleestiverpoucoinclinado,emvezdeincrementaravariável
xem1,vocêincrementariaem0.5oualgoproporcionalàacelera çãoindicada
peloacelerômetro.
• Oacelerômetropodemandarsinaisinvertidosdeacordocomainclina ção.
Dependendodacalibra ção,vocêprecisadetectarseissoestaocorrendo,para
nãomudaraorienta çãodoaviãorepentinamente!Issodáumcertotrabalho...
9.5 C onclusão
Esseéumcapítulotrabalhoso,masmuitogratificante.Utilizarrecursosdosapare-
lhoséumdosprincipaisapelosdarevolu çãodosjogosparacelular.Sabertrabalhar
139

## Página 150

9.5. Conclusão CasadoCódigo
bemcomessespoderososrecursospodeelevarojogoaumníveldejogabilidade
muitomaisinteressante!
Figura9.3:Controleporacelerômetro.
140

## Página 151

Capítulo10
T e l afinalegameover
T o d oofluxodojogoestábemencaminhado,desdeateladeabertura,passandopelas
colisões eefeitos,sonseacelerômetro. Agoracriaremosduastelasquefecharãoo
cicloprincipaldogame.
Aprimeiratelaasercriadaseráatelamostradaquandoojogoacabar,ouseja,
quandoo14bisvenceros100meteoros.
Essatelaserácompostaporumamúsicafinal,porumaimagemnovaeumbotão
deiniciodojogo.
Aofinal,deveremosteratelacomoabaixo.

## Página 152

10.1.T e l afinal CasadoCódigo
Figura10.1:T e l adofinaldojogo.
10.1 Telafinal
Para montar a tela de final de jogo precisaremos de mais uma imagem, a
finalend.png. Essaimagemdeveficarnodiretório assetsdoprojetoeserá
incluídananossaclassede Assets.
public class Assets {
public static String FINALEND = "finalend.png";
}
V a m o scriaraclassequerepresentaráatelafinal.Elaseráumanova CCLayer
eseunomeseráFinalScreen.
142

## Página 153

CasadoCódigo Capítulo10.T e l afinalegameover
Nela,criaremosumavariáveldebackgroundeoutraparaobotãoqueiniciao
gamenovamente:
package com.example.nave.game.scenes;
public class FinalScreen extends CCLayer{
private ScreenBackground background;
private Button beginButton;
public CCScene scene() {
CCScene scene = CCScene.node();
scene.addChild(this);
return scene;
}
}
Oconstrutordessaclassedeveinicializarosobjetos background, some imagem
de logo.Faremosissocomojáfizemosemoutrastelas:Crieoconstrutordaclasse
FinalScreen:
public FinalScreen() {
// background
this.background = new ScreenBackground(Assets.BACKGROUND);
this.background.setPosition(
screenResolution(CGPoint.ccp(screenWidth() / 2.0f,
screenHeight() / 2.0f)));
this.addChild(this.background);
// som
SoundEngine.sharedEngine().playSound(
CCDirector.sharedDirector().getActivity(),
R.raw.finalend, true);
// imagem
CCSprite title = CCSprite.sprite(Assets.FINALEND);
title.setPosition(
screenResolution(CGPoint.ccp( screenWidth() /2 ,
screenHeight() - 130 ))) ;
this.addChild(title);
}
Configuraremos,aindanoconstrutor,obotãoqueiniciaojogonovamente:
143

## Página 154

10.1.T e l afinal CasadoCódigo
this.setIsTouchEnabled(true);
this.beginButton = new Button(Assets.PLAY);
this.beginButton.setPosition(
screenResolution(CGPoint.ccp( screenWidth() /2 ,
screenHeight() - 300 ))) ;
this.beginButton.setDelegate(this);
addChild(this.beginButton);
Essa tela terá um botão, portanto, implementaremos a interface
ButtonDelegateeométodo buttonClicked.
public class FinalScreen extends CCLayer implements ButtonDelegate {
@Override
public void buttonClicked(Button sender) {
if (sender.equals(this.beginButton)) {
SoundEngine.sharedEngine().pauseSound();
CCDirector.sharedDirector()
.replaceScene(new TitleScreen().scene());
}
}
Paraqueessaclassepossaservistanojogo,aclasse GameScenedeveestarciente
einicializá-la.Paraisso,teremosométodostartFinalScreenquefazatransição
paraatelafinal.
Naclasse GameSceneadicioneoseguintemétodo:
public void startFinalScreen() {
CCDirector.sharedDirector()
.replaceScene(new FinalScreen().scene());
}
Equandoteremosateladefinaldojogo? Faremosissoquando100meteoros
foremdestruídos!Porém,parafacilitarostestes,mostraremosatelafinalquando5
meteorosforemdestruídos.
Naclasse Scoredeixeocódigodométodo increasecomoaseguir:
public void increase() {
score++;
this.text.setString(String.valueOf(this.score));
144

## Página 155

CasadoCódigo Capítulo10.T e l afinalegameover
if(score==5){
this.delegate.startFinalScreen();
}
}
Aodestruir5meteorosjádevemosteratelafinalcomosomdavitória!
Figura10.2:T e l adofinaldojogo.
10.2 TelaGame Over
Ateladegameoverseguiráamesmalógicadatelafinal,porémdeveráserinici-
alizadaemumoutromomento.Quando? Simples,quandoummeteoroatingiro
145

## Página 156

10.2.T e l aGameOver CasadoCódigo
avião!
V a m o saocódigo.Primeiro,adicionandoumanovafiguranaclasse Assets.
public class Assets {
public static String GAMEOVER = "gameover.png";
}
Crieaclasse GameOverScreenqueéuma CCLayer.Nessaclasse,utilizaremos
amesmaideiadateladefinaldejogo:
package com.example.nave.game.scenes;
public class GameOverScreen extends CCLayer{
private ScreenBackground background;
private Button beginButton;
public CCScene scene() {
CCScene scene = CCScene.node();
scene.addChild(this);
return scene;
}
}
Oconstrutordaclasse GameOverScreentambémébemsimples,parecidocom
oquejáconhecemos:
public GameOverScreen() {
// background
this.background = new ScreenBackground(Assets.BACKGROUND);
this.background.setPosition(
screenResolution(CGPoint.ccp(screenWidth() / 2.0f,
screenHeight() / 2.0f)));
this.addChild(this.background);
// image
CCSprite title = CCSprite.sprite(Assets.GAMEOVER);
title.setPosition(
screenResolution(CGPoint.ccp( screenWidth() /2 ,
screenHeight() - 130 ))) ;
this.addChild(title);
146

## Página 157

CasadoCódigo Capítulo10.T e l afinalegameover
// habilita o toque na tela
this.setIsTouchEnabled(true);
this.beginButton = new Button(Assets.PLAY);
this.beginButton.setPosition(
screenResolution(CGPoint.ccp( screenWidth() /2 ,
screenHeight() - 300 ))) ;
this.beginButton.setDelegate(this);
addChild(this.beginButton);
}
Para que o botão de reiniciar o jogo funcione, implemente a interface
ButtonDelegateeométodo buttonClickednaclasse GameOverScreen:
public class GameOverScreen extends CCLayer
implements ButtonDelegate {
@Override
public void buttonClicked(Button sender) {
if (sender.equals(this.beginButton)) {
SoundEngine.sharedEngine().pauseSound();
CCDirector.sharedDirector()
.replaceScene(new TitleScreen().scene());
}
}
}
Achamadaaessateladeveserfeitaquandoacolisãoentremeteoroeaviãofor
detectada.Paraisso,adicioneatransiçãoaométodo playerHitda GameScene:
public void playerHit(CCSprite meteor, CCSprite player) {
((Meteor) meteor).shooted();
((Player) player).explode();
CCDirector.sharedDirector()
.replaceScene(new GameOverScreen().scene());
}
Ateladegameoverdeveestaraparecendoquandoometeorocolidecomoavião,
comomostradoaseguir.
147

## Página 158

10.3.Conclusão CasadoCódigo
Figura10.3:T e l adegameover.
10.3 Conclusão
Esseéumcapítulosimples,poisjáconhecemostudoqueénecessárioparacriação
detelasetransições. V o c êpodeusarsuaimaginaçãoecriardiversasnovastelasno
game!
148

## Página 159

Capítulo11
P a u s a n d oojogo
Nessecapítulofalaremosdemaisumaparteimportantíssimadeumjogo,atelade
pause.Essatelanãocostumaserdasmaisdivertidasdeserdesenvolvida,atémesmo
pelafalsaimpressãoquepodeserumatelasimples.Porém,tenhaatençãoaqui!T e -
remosmuitosconceitosimportantesnessemomento.
Paranãoseenganar,vamosàlistadefuncionalidadesqueumateladepausedeve
ter.
•Construirumanovacamadaparaateladepause
•Criarumaclassequeentenderáseojogoestáempauseourodando
•Criarmaisumbotãonateladejogo,obotão pause
•Fazerolinkentreateladepauseeteladejogo
•Pararrealmenteosobjetosnatela

## Página 160

11.1.Montandoateladepause CasadoCódigo
V e j acomoateladepausepodeenganar.Sãomuitascoisasaseremfeitaspara
quetudofuncionebem.
Repareque,semprequepossível,fazerumalistadefuncionalidadesesperadas
natelapodeajudaravercommaisprofundidadeotrabalhoqueseránecessário
desenvolver.
Aofinaldessecapítuloateladeveráestarcomoabaixo:
Figura11.1:T e l adepause.
11.1 Montando a tela de p a u s e
V a m o scomeçardeformasimplesecomoquejávimosatéomomento.Atelade
pauseénaverdademaisumacamadadentrodeumatela,ouseja,nãomudaremos
150

## Página 161

CasadoCódigo Capítulo11.Pausandoojogo
decena( CCScene).Comoanteriormente,todonovacamadano Cocos2Dpode
serrepresentadapelaclasse CCLayer.
U m aparteimportantedessatelaéqueelaterá2botões, ocontinuar,quevolta
projogo,eosair,quevaiparaateladeabertura.
Criaremososdoisbotões nessacamadaeimplementaremosumainterfacejá
utilizada,emoutraspartesdogame,a ButtonDelegate.
Crieaclasse PauseScreencomoabaixo:
public class PauseScreen extends CCLayer implements ButtonDelegate {
private Button resumeButton;
private Button quitButton;
private CCColorLayer background;
}
Apróximaetapaéadicionaraseguintelistanessatela:
•Habilitarotouchnessacamada
•Definirumbackground,nessecasoumpretoescurotransparente
•Colocarologo,comonateladeabertura
•Adicionarosbotões
•Posicionarosbotões
Naclasse Assetsadicione:
public static String EXIT = "exit.png";
Faremosasdefinições acimanoconstrutordaclasse. Crieoconstrutorda
PauseScreencomoabaixo:
public PauseScreen() {
// habilita o toque na tela
this.setIsTouchEnabled(true);
// background
this.background = CCColorLayer.node(ccColor4B.ccc4(0, 0, 0, 175),
screenWidth(),
screenHeight());
this.addChild(this.background);
151

## Página 162

11.2.ControlandooGameLoop CasadoCódigo
// logo
CCSprite title = CCSprite.sprite(Assets.LOGO);
title.setPosition(screenResolution(
CGPoint.ccp( screenWidth() /2 , screenHeight() - 130 ))) ;
this.addChild(title);
// Adiciona botoes
this.resumeButton = new Button(Assets.PLAY);
this.quitButton = new Button(Assets.EXIT);
this.addChild(this.resumeButton);
this.addChild(this.quitButton);
// Posiciona botoes
this.resumeButton.setPosition(screenResolution(
CGPoint.ccp( screenWidth() /2 , screenHeight() - 250 ))) ;
this.quitButton.setPosition(screenResolution(
CGPoint.ccp( screenWidth() /2 , screenHeight() - 300 ))) ;
}
Nessemomentotemosateladepause,porémessaésóaprimeiraparte.Repare
quecriarumateladepausenãoéalgodiferentedastelasanterioresdojogo,porém,
fazerocontrolequeelaprecisademandaránovosconceitos.V a m o saeles.
11.2 Controlando o Game Lo o p
Lembradaanalogiadedesenhosemblocosdepapeldocapítulosobreprotótipos?
Falamosqueumjogopodesercomparadoaumasequênciadeimagensquesão
desenhadasacadamudançanoposicionamentodosobjetosdojogo,gerandoaim-
pressãodemovimento.
Oqueissoimportaparaateladepause?Precisamosterumcontroledequeo
jogoestárodando,ouseja,estamosnapartedejogorealmenteenão emtelasde
abertura,porexemplo.Alémdisso,precisamossaberseojogoestápausadoounão
naquelemomento.
Comessasduasvariáveisdecontroledeestado,podemosdefinirsedevemos
mostrarateladepause,sedevemosparalisarosobjetosnatela,retomarosmovi-
mentosdosobjetosetc.
Faremosessecontrolecomumaclassequeteráapenasessaresponsabilidade.
152

## Página 163

CasadoCódigo Capítulo11.Pausandoojogo
Crieaclasse Runner,comoduasvariáveisdecontrole:
public class Runner {
private static boolean isGamePlaying;
private static boolean isGamePaused;
}
Essaclasseteráalgumaspeculiaridades.U m adelaséqueelasóteráumainstân-
ciaativanoprojeto,paraquenãoocorramconfusões entreosestados.
Paraisso,oconstrutorseráprivadoeainstânciaserácontroladapelavariável
ru n n e r.
Crieavariávelabaixoeoconstrutorprivadonaclasse Runner:
static Runner runner = null;
private Runner(){
}
Semprequeprecisarmosfazeraverificaçãodoestadodogame,chamaremosum
métodoquenosdevolveráareferênciaqueestácuidadodisso.Casonãotenhasido
criadaainda,criaremosnessemomento.
Adicioneométodo check()naclasse Runner:
public static Runner check(){
if (runner!=null){
runner = new Runner();
}
return runner;
}
Parafinalizaraclassedecontrole,criaremosos getterse settersdasclassesda
classedecontrole.
Crieosmétodosabaixonaclasse Runner:
public static boolean isGamePlaying() {
return isGamePlaying;
}
public static boolean isGamePaused() {
return isGamePaused;
153

## Página 164

11.3.Adicionandoobotãodepause CasadoCódigo
}
public static void setGamePlaying(boolean isGamePlaying) {
Runner.isGamePlaying = isGamePlaying;
}
public static void setGamePaused(boolean isGamePaused) {
Runner.isGamePaused = isGamePaused;
}
Essaclassepodeparecersimples. U mSingletoncom getterse setters. Porém,
suafuncionalidadeédeextremaimportâncianogame.V a m o sutilizá-lasemvários
momentos.
11.3 Adicionando o bo t ã o de p a u s e
Apróximaetapaérelativamentesimples.Iremosadicionarobotãopausenatelado
jogo.Paraissoprecisamosdeumnovoarquivo,aimagemdobotãopause.Adicione-
oaclasse Assets.
public static String PAUSE = "pause.png";
Adicionaremosessenovobotão naclasse GameButtons. Aqui,replicaremos
oquejátemoscomosoutrosbotões. Oobjetivoécriarumanovavariáveldotipo
Button,adicioná-lanacamadadebotões, configurarodelegateeposicioná-lana
tela.
Parafechar,nométodobuttonClicked(),faremosumachamadaaométodo
pauseGameAndShowLayer.Essemétodoserácriadona GameSceneefaráacha-
madaàteladepause.
Deixeaclasse GameButtonscomoabaixo:
public class GameButtons extends CCLayer implements ButtonDelegate {
private Button leftControl;
private Button rightControl;
private Button shootButton;
private Button pauseButton;
private GameScene delegate;
public static GameButtons gameButtons() {
154

## Página 165

CasadoCódigo Capítulo11.Pausandoojogo
return new GameButtons();
}
public GameButtons() {
// habilita o toque na tela
this.setIsTouchEnabled(true);
// Cria os botoes
this.leftControl = new Button(Assets.LEFTCONTROL);
this.rightControl = new Button(Assets.RIGHTCONTROL);
this.shootButton = new Button(Assets.SHOOTBUTTON);
this.pauseButton = new Button(Assets.PAUSE);
// configura delegacoes
this.leftControl.setDelegate(this);
this.rightControl.setDelegate(this);
this.shootButton.setDelegate(this);
this.pauseButton.setDelegate(this);
// configura posicoes
setButtonspPosition();
// adiciona botoes a tela
addChild(leftControl);
addChild(rightControl);
addChild(shootButton);
addChild(pauseButton);
}
private void setButtonspPosition() {
// posicao dos botoes
leftControl.setPosition(
screenResolution(CGPoint.ccp( 40 , 40 ))) ;
rightControl.setPosition(
screenResolution(CGPoint.ccp( 100 , 40 ))) ;
shootButton.setPosition(
screenResolution(CGPoint.ccp(screenWidth() -40, 40)));
pauseButton.setPosition(
screenResolution(CGPoint.ccp(40, screenHeight() - 30 )));
155

## Página 166

11.4.Ainterfaceentrejogoepause CasadoCódigo
}
@Override
public void buttonClicked(Button sender) {
if (sender.equals(this.leftControl)) {
this.delegate.moveLeft();
}
if (sender.equals(this.rightControl)) {
this.delegate.moveRight();
}
if (sender.equals(this.shootButton)) {
this.delegate.shoot();
}
if (sender.equals(this.pauseButton)) {
// configuraremos mais a frente
}
}
public void setDelegate(GameScene gameScene) {
this.delegate = gameScene;
}
}
11.4 A interface entre jogo e p a u s e
Defatoumateladepausenãoétão simplescomopodeparecer,certo? Recapitu-
lando,nessecapítulocriamosatéaqui3coisas:Ateladepause,umaclassedecon-
troledeestadoseadicionamosobotãodepausenateladejogo.
Ésemprebomparareanalisaroquejáfoifeitoemtarefasquesãograndescomo
essas,eenvolvemdiversasclasses.
Tendoaclassedateladepauseeosbotões, precisamosfazerojogoentender
quandoeledevemostrá-la.
Nessa jogo, precisamos fazer um link entre a classe principal do jogo, a
GameScene,eateladepause.Criaremosumainterfaceparadizeroqueatelado
jogodevesaberfazer,nessecaso,pararojogo,continuaresair.
Crieainterface PauseDelegate:
156

## Página 167

CasadoCódigo Capítulo11.Pausandoojogo
public interface PauseDelegate {
public void resumeGame();
public void quitGame();
public void pauseGameAndShowLayer();
}
ParaprepararateladePauseparafazerolinkcomateladejogo,criaremosum
delegate.Na PauseScreenadicioneocódigoabaixo:
private PauseDelegate delegate;
public void setDelegate(PauseDelegate delegate) {
this.delegate = delegate;
}
Adicioneosdelegatesdosbotões resumeButtone quitButtonaoconstrutor
daclasse PauseScreen.Essapartedeveficarcomomostradaaseguir:
public PauseScreen() {
// codigo
// botoes
this.resumeButton = new Button(Assets.PLAY);
this.quitButton = new Button(Assets.EXIT);
this.resumeButton.setDelegate(this);
this.quitButton.setDelegate(this);
this.addChild(this.resumeButton);
this.addChild(this.quitButton);
}
11.5 Pausando o jogo
Começaremosafazero linkentretudoquefoivistonessacapítuloagora!Aprincipal
ideiaéorquestrartudoquefizemospelaclasse GameScene,queéateladojogoe
receberáoeventodepauseeativaráa PauseScreen.
Paraqueateladepausepossaservista,precisaremosadicionarumanovaca-
madana GameScene.Criaremosumacamadadotipo CCLayereumobjetodo
tipo PauseScreen.
157

## Página 168

11.5.Pausandoojogo CasadoCódigo
Na GameScenecrieasvariáveis:
private PauseScreen pauseScreen;
private CCLayer layerTop;
Noconstrutorda GameSceneiniciaremosacamadaevamosadicionaramesma
àcenaatual.
private GameScene() {
// ...
this.layerTop = CCLayer.node();
this.addChild(this.layerTop);
}
Feitoisso,umanovacamadaexistenateladejogo,masaindasemrelaçãocom
ateladepausequequeremos.
M é t o d o sde pause
V a m o sseguirfazendoesselink.Faremosateladejogosaberquealgunsmétodos
depausesãonecessários,nessecaso, pause, r e s u m ee q u i t.
A GameScreenimplementaráainterfacequedizoquedeveserfeitopelopause.
public class GameScene extends CCLayer implements MeteorsEngineDelegate,
ShootEngineDelegate, PauseDelegate {
V a m o simplementarcadaumdos3métodosdepauseagora.Oprimeiroseráo
pauseGame().Oqueessemétododevefazeréverificarseogameestárodando,ou
seja,estamosjogandonateladejogo,eseojogonãoestájáempause.Casoissoseja
verdadeiro,configuramosavariáveldepausepara tr ue.
Na GameScenecrieométodo pauseGame():
private void pauseGame() {
if (!Runner.check().isGamePaused() &&
Runner.check().isGamePlaying()) {
Runner.setGamePaused(true);
}
}
158

## Página 169

CasadoCódigo Capítulo11.Pausandoojogo
Opróximopassoéummétodoqueremoveateladepauseparacontinuar
o jogo. Nele, configuramos o pause para f a l s e. É válidochamar o método
setIsTouchEnabledpoisaovoltardascamadasalgunsdevicesperdemessacon-
figuraçãode touch.
Adicioneométodo resumeGamema GameScreen:
@Override
public void resumeGame() {
if (Runner.check().isGamePaused() ||
! Runner.check().isGamePlaying()) {
// Continua o jogo
this.pauseScreen = null;
Runner.setGamePaused(false);
this.setIsTouchEnabled(true);
}
}
Parafechar,implementaremosométodo quit,omaissimplesentreos3.Nele,
V a m o spararossonsqueestamostocando.Alémdisso,faremosumatransiçãopara
ateladeabertura.
@Override
public void quitGame() {
SoundEngine.sharedEngine().setEffectsVolume(0f);
SoundEngine.sharedEngine().setSoundVolume(0f);
CCDirector.sharedDirector()
.replaceScene(new TitleScreen().scene());
}
Iniciando tudo
Precisamosconfiguraralgumasvariáveisdecontroledeestadologonocomeço
dojogo.Nométodo onEnter()da GameScreenvamosadicionarasconfigura-
ções de p l aye pauseabaixo:
public void onEnter() {
super.onEnter();
// Configura o status do jogo
159

## Página 170

11.5.Pausandoojogo CasadoCódigo
Runner.check().setGamePlaying(true);
Runner.check().setGamePaused(false);
// pause
SoundEngine.sharedEngine().setEffectsVolume(1f);
SoundEngine.sharedEngine().setSoundVolume(1f);
// verifica colisoes
this.schedule("checkHits");
this.startEngines();
}
Criaremosagoraummétodoresponsávelporiniciarateladepause,queserá
acionadopelobotão depause. Primeiramente,crieométodoabaixonaclasse
GameScreen:
public void pauseGameAndShowLayer() {
if (Runner.check().isGamePlaying() &&
! Runner.check().isGamePaused()) {
this.pauseGame();
}
if (Runner.check().isGamePaused() &&
Runner.check().isGamePlaying() &&
this.pauseScreen == null) {
this.pauseScreen = new PauseScreen();
this.layerTop.addChild(this.pauseScreen);
this.pauseScreen.setDelegate(this);
}
}
Efaçaachamadaaelenaclasse GameButtons:
if (sender.equals(this.pauseButton)) {
this.delegate.pauseGameAndShowLayer();
}
Agoraquejátemososmétodosdepausecriadosna GameScreen,vamosvoltar
naclasse PauseScreenereferenciarasações dosbotões, adicionando:
160

## Página 171

CasadoCódigo Capítulo11.Pausandoojogo
@Override
public void buttonClicked(Button sender) {
// Verifica se o botão foi pressionado
if (sender == this.resumeButton) {
this.delegate.resumeGame();
this.removeFromParentAndCleanup(true);
}
// Verifica se o botao foi pressionado
if (sender == this.quitButton) {
this.delegate.quitGame();
}
}
Aorodaroprojeto,ateladepausedeveaparecermasaindatemostrabalhoa
fazer.
11.6 Pausando os objetos
Temostodaaarquiteturapreparadaparaopause,masalgomuitoimportanteainda
nãofoifeito.Aorodaroprojetoeapertaropause,temosatelaaparecendo,porém,
nãotemososobjetosparando.
Precisamosusaraclasse Runnerquecontrolaoestadodogameparaisso.Será
atravésdasvariáveisdessaclassequepoderemosdefinirseosobjetoscomometeoros,
tiroseaviãodevemsemoverno game loop.
Alógicaparaissoserásempreigual.Apenasmovimentaremosumobjetonatela
dejogoseojogoestiverrodandoenão empause. Alémdisso,sópodemoscriar
novoselementosseessacombinaçãotambémforsatisfatória.
Naclasse MeteorsEngineadicioneaverificaçãoabaixo:
public void meteorsEngine(float dt) {
if (Runner.check().isGamePlaying() &&
! Runner.check().isGamePaused()) {
if (new Random().nextInt(30) == 0) {
this.getDelegate().createMeteor(
new Meteor(Assets.METEOR));
}
}
}
161

## Página 172

11.6.Pausandoosobjetos CasadoCódigo
Naclasse Meteoradicioneaverificaçãoabaixoduranteo update:
public void update(float dt) {
// pause
if (Runner.check().isGamePlaying() &&
! Runner.check().isGamePaused()) {
y -= 1;
this.setPosition(screenResolution(CGPoint.ccp(x, y)));
}
}
Naclasse Shootadicioneaverificaçãoabaixo:
public void update(float dt) {
if (Runner.check().isGamePlaying() &&
! Runner.check().isGamePaused()) {
positionY += 2;
this.setPosition(screenResolution(
CGPoint.ccp(positionX, positionY)));
}
}
Naclasse Playeradicioneaverificaçãoabaixo:
public void shoot() {
if (Runner.check().isGamePlaying() &&
! Runner.check().isGamePaused()) {
delegate.createShoot(new Shoot(positionX, positionY));
}
}
public void moveLeft() {
if (Runner.check().isGamePlaying() &&
! Runner.check().isGamePaused()) {
if (positionX > 30) {
positionX -= 10;
}
setPosition(positionX, positionY);
}
}
162

## Página 173

CasadoCódigo Capítulo11.Pausandoojogo
public void moveRight() {
if (Runner.check().isGamePlaying() &&
! Runner.check().isGamePaused()) {
if (positionX < screenWidth() - 30) {
positionX += 10;
}
setPosition(positionX, positionY);
}
}
Muitotrabalho,não? Ateladepausepodeenganar,mascomofoivisto,éum
pontochavenodesenvolvimentodosgames.Rodeoprojetoeverifiqueocompor-
tamentodessanovatelanojogo.
11.7 Conclusão
Fazerumateladepauseénormalmenteumapartequeosdesenvolvedoresdeixam
deladonaconstruçãodeumgameedepoispercebemacomplexidadedesuaimple-
mentação.Essatelausaconceitosquesepropagamportodoogameedeveserfeita
comcuidadoeplanejamento.
Anotíciaboaéquesevocêchegouatéaquivocêjátemosconceitosprincipais
paradesenvolverumjogo! Imagens,loop,camadas,sons,colisões, etc. Não são
coisasfáceis,mascomapráticaviramconceitosqueserepetemportodoogame.
163

## Página 174

11.7.Conclusão CasadoCódigo
Figura11.2:T e l adepause.
164

## Página 175

Capítulo12
Continuandonossojogo
Depoisdesabercomocriarabasedeumjogoesuaestrutura,montaroscenário
einterações ecriartelasdefluxodogame,muitacoisapodeserdesenvolvidade
acordocomasuaimaginação.Apartemaislegaldeagoraemdianteserápensarem
ideiasquepossamtornarojogocadavezmaisdivertidoemotivante.Omundodos
gamesésempreummundodenovidades,deinovações, emquecadanovaideiadá
margemparamilharesdenovosjogos.
Essecapítulomostrarásugestões decomotornarogamemaissocial,dinâmico
e,quemsabe,rentável.
12.1 Utilizando ferramentas sociais
Paratornarojogomaisengajadorpodemos adicionardiversasfuncionalidades
comorankings,ondeosusuáriosdisputamqueméomelhor, badgesqueservem
comomedalhasparaprovarconquistasduranteojogoeatémonetizaroaplicativo
comitensespeciais.

## Página 176

12.2.Highscore CasadoCódigo
Existemhojediversasplataformassociaisquesimplificammuitotodoessede-
senvolvimento,funcionandopraticamentedeforma plug a n dp l ay.
U m aboaalternativaparanossojogoéconhecero Swarm. O Swarméuma
plataformasocialutilizadapordiversosgamesetrazasfuncionalidadeacimadeuma
formasimplesdeimplementar.
Confiraositedo Swarmem:http://swarmconnect.com/
T o d oo setupdasuacontapodeserfeitoiniciandoporesselink:
http://swarmconnect.com/admin/docs/setup
Figura12.1:PlataformaSwarmConnect.
Osjogosqueutilizamaplataforma Swarmtêmnasuaprimeiratelaumatelade
conexão,naqualcomumsimplesaceiteemumbotão,umIDégeradoparaaquele
jogador.Ficaacritériodojogadorcompletardepoisseusdadospessoais,comonome
eapelidocasotenhainteresse.
12.2 Highscore
Os rankingsou highscoresno Swarmsãochamadosde Leaderboards.Aideiaécriar
ummuralondetodososusuáriossãoordenadosparasaberquemsãoosmelhores.
Aimplementaçãoésimples.Acadafimdejogo,fazemosumarequisiçãoa API
passando IDepontuação.
Ocódigoficaparecidocom:
SwarmLeaderboard.submitScore(LEADERBOARD_ID, meteorosDestruidos);
V o c êpodeconferiraáreasobre Leaderboardsnesselink:
http://swarmconnect.com/admin/docs/leaderboard
166

## Página 177

CasadoCódigo Capítulo12.Continuandonossojogo
Figura12.2:Leaderboards
12.3 Badges
Imagineseapósdestruir10meteorosojogadosganhasseotítulode Piloto pró,
eapósdestruir50ganhasseotítulode Piloto Master.Quetal,aofimdojogo,
entregara badge Santos Dumontaojogador?Essascriações tornamojogomais
atrativo,commaisobjetivos,einclusive,podemsercompartilhadasemredessociais.
Acriação de badgesusandoo Swarmétambémfácil.V o c êapenasdefineas
badgesdojogoeinformaatravésdaAPIquandoissoocorreu:
if (meteorosDestruidos == 50) {
SwarmAchievement.unlock(PILOTO_MASTER_ID);
}
Esse IDseráumnúmerocriadonositedoSwarm.
Crieideiasinteressantesde badgeseimplemente-ascom Swarm.Parasabermais
acesseadocumentaçãonaáreaAdding Achievements t oyour A p ppelolink:
167

## Página 178

12.4.Desafiosparavocêmelhorarojogo CasadoCódigo
http://swarmconnect.com/admin/docs/achievements
Figura12.3:Criandobadges.
12.4 Desafiospara v o c êmelhorar o jogo
Aquivãoalgumassugestõesquevisamdesafiaroleitorasolidificarosconhecimentos
adquiridoscomolivroeampliaroengajamentodojogo14bis.
Novos tiros
T o d ojogadoradoraincrementarsuamunição.Crieumtiroduploparao14bis!
Essestirosdevemsairnãomaisemlinharetamassimformandoumangulode45
grausparacadalado.Interessantefazeressetiroserdadoaojogadorapósalguma
conquistadogame,comomatarumnúmerodemeteoros,ouatiraremumelemento
especialquedeuessepoder!
168

## Página 179

CasadoCódigo Capítulo12.Continuandonossojogo
Diferentes meteoros
Quemdissequetodososmeteorossãoiguais?Quetalimplementartamanhos
diferentesdemeteoros,quepontuamdiferentedeacordocomseutamanho? Co-
mecesimples,meteorosmaioresvalem2pontosemeteorosmenorescontinuam
valendo1.Comissoimplementado,mudeaimagemdosmeteoroseatécoloque
esporadicamenteoutroselementosquepodemvaler5ou10pontos,masqueapare-
cemcomumfrequênciamenor.V a l etambémfazercomqueosmeteorostenham
velocidadesdiferentesentresi!
Armaduras
Morrercomapenasummeteoroéchato,maspodemoscapturarumelemento
quefortificaoavião!Crieumelementoquefuncionacomoumaarmaduraepermite
acolisãoentreummeteoroeoavião.Lembre-sedemostraraojogadorqueeleestá
equipadocomesseelemento,mudandoacordoaviãoporexemplo.
Efeitos nos sprites
Atualmenteosobjetossão estáticosnonossogame. Quetaladicionarefeitos
comofazerometeorodescergirandoouluzesnoavião? Essespequenosdetalhes
fazemojogoparecermuitomaisatraente.
12.5 Co m o ganhar dinheiro?
Omundodosgamesmoveumvalorenormeeéhojeumadasmaioresmovimen-
tações financeirasdomundo.Esselivronãovisatrazeranálisessobreessemercado
financeiro,porémhojeascifrasdosgamessuperamosnúmerosdocinema.
Paramonetizarogamevocêpodeseguirpordiversasabordagens,comoestabele-
cerumvalordevendaquandoousuáriobaixar.Porém,nomundodossmartphones
essaestratégianãoémuitoutilizada.
U m aformabeminteressantedeganhardinheirocomojogoédeixando-ogra-
tuitooucobrandoumvalorbembaixo,comoqualousuáriovaiinstalarojogosem
muitoesforço.A p ó sisso,ojogodevecativarousuárioeentãopodeofereceritensa
seremcompradosquemelhoramaexperiênciaeperformancedojogo.
O Swarmofereceumaformabeminteressantedemonetizarogameefácilde
aplicar.TendotodaadocumentaçãoeAPIpronta,vocêpodeadicionaressesitens
compoucaslinhasdecódigo,comonaslinhasabaixo,queindicamavendadeum
169

## Página 180

12.6.Conclusão CasadoCódigo
item:
SwarmStoreListing.purchase(context, SUPER_BOMBA_ID);
Parasabermaissobremonetização dojogoutilizandoo Swarmacesseaárea
Adding a S w a r mStore t oyour A p pnoseguintelink:
http://swarmconnect.com/admin/docs/store
Figura12.4:Exemplodeitenspagos.
12.6 Conclusão
Desenvolverjogoséumatarefacomplexaeaomesmotempodivertida,alémdeser
umaótimamaneiradeelevaroconhecimentodeprogramação.Atualmente,oscelu-
laresmodernostrouxeramumaoportunidadeúnicaparaquedesenvolvedorespos-
samteressaexperiência,criandoseusprópriosgames,umarevoluçãosimilaraque
awebeoscomputadorespessoaisgeraramalgunsanosatrás.
Alémdisso,criarjogoséumexercíciodecriatividadequepermiteexplorara
nossaimaginaçãoecriarhistóriasinterativaseúnicas.Esselivrotentacompartilhar
essesconhecimentoseideias,esperandoserdefatoútilatodosaquelesqueestão
ingressandonessemágicomundodejogosparaAndroid.
Ficanovamenteoconviteparavocêparticipardanossalistadediscussão:
https://groups.google.com/group/desenvolvimento-de-jogos-para-android
EvocêpodetirardúvidaspelofórumdoGUJ.com.br:
http://www.guj.com.br/
Boadiversão!
170