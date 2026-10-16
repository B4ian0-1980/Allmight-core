---json
{
  "id": "a_l_gica_do_jogo_recriando_cl_ssicos_da_hist_ria_dos_videogames",
  "title": "A lógica do Jogo Recriando clássicos da história dos videogames",
  "categoria": "03-linguagens",
  "subcategoria": "go",
  "resumo": "**Arquivo Original:** `A lógica do Jogo Recriando clássicos da história dos videogames.pdf` **Data Conversão:** 1643798097.0",
  "gatilhos": [
    "dos",
    "gica",
    "hist",
    "jogo",
    "linguagens",
    "recriando",
    "ria",
    "ssicos"
  ],
  "perguntas_tipo": [
    "Como utilizar A lógica do Jogo Recriando clássicos da história dos videogames?",
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

# A lógica do Jogo Recriando clássicos da história dos videogames

> **Arquivo Original:** `A lógica do Jogo Recriando clássicos da história dos videogames.pdf`
> **Data Conversão:** 1643798097.0

---


## Página 1

66657


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
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 3

E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 4

E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 5

CasadoCódigo
Agradecimentos
Agradeoatodaminhafamliaque,dealgumaforma,emdiversosmomentos
daminhavida,meajudouachegaraolugarondeestouhoje.
i
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 6

E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 7

CasadoCódigo
Introdução
Estelivronãobuscasomenterecriaralgunsgrandesclássicosdomundodo
entretenimentoeletrônico,massimentender,deformaprática,alógicaen-
volvidaemcadaumdeles,cujasmecânicassãoutilizadasatéhojeemmuitos
jogosmodernos.Assim,daráaoleitorabaseinicialnecessáriaparaacria ção
deseusprópriosprojetos.
Estrutura do livro
Contamoscom10capítulos,sendo3delesdedicadosaosprotótiposde
jogo,6paraosjogose1pararevermososdesafiospropostosnosoutroscapí-
tulos.
Nãosófalamosdediversosjogoscomoabordamos,acadanovojogocri-
ado,aspectosgeraisdodesenvolvimentodejogosdeformagradual,desdea
movimentaçãodopersonagematéousodesonseimagens.Quandoterminar
oúltimocapítulo,vocêpoderádesenvolverqualquerumdosjogosabordados
deformacompleta,cominício,meioefim.
Nocapítulo1,veremoscomocriarjanelas,desenhar,interatividadeeani-
mação,alémdecriarmosumprotótipodejogoedetec çãodecolisão.
Nocapítulo2,criaremosnossaversãodoSpaceInvaders,explorandomais
amovimentaçãodojogadoredosinimigos(queéumexercíciológicoàparte)
comumapequenaanima ção.Adicionaremostambémpontua çãoeaumento
dedificuldade.
Nocapítulo3,oPongquecriamoséparadoisjogadores,então,usaremos
tecladoemouseparacontrolarcadaum.Aprenderemosasepararojogoem
cenários,ecriaremosummenusimplesparaconfigura çãodomododejogo.
iii
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 8

CasadoCódigo
Nocapítulo4,aocriaroBlockade(Jogodacobrinha),focamosemutilizar
níveis,tambémconhecidoscomofasesou levels,tendoassimumjogocom
inúmeraspossibilidades.
Nocapítulo5,veremosporqueTetriséoquebra-cabe çasanimadomais
viciantejácriado,alémdededicarmosumaparteespecialparafalarmosde
músicaeefeitossonoros,ecomocalcularotamanhododesenhodeacordo
comotamanhotelaoujaneladojogo.
Nocapítulo6,criaremosumprotótipodoPac-Mansóparaabordarmos
aInteligênciaArtificialutilizadanapersegui çãoefugadospersonagensdo
jogo.Tambémveremosumtipodecolisãomaiscomplexa.
Nocapítulo7,criaremosumPac-Manmaisparecidocomojogooriginal,
utilizandonãosomenteimagens,mastambémSpriteseTiles.
Nocapítulo8,usaremosojogoNaveQuebradaparaabordamosamate-
máticadojogoAsteroids,semfalardematemáticaveremos:rota ção,escalo-
namento,transiçãoeângulos.
Nocapítulo9,alémdeumaversãoparaumoudoisjogadoresdeAs-
teroids,veremosmaisderota çãoeângulosalémdeanima çãodeSpritese
melhoriasnoprocessamentodojogo.
Nocapítulo10,reveremososdesafiosdeixadosparaoleitore,paraos
desafiosondeapenasindicarasolu çãonãoéosuficiente,criaremosexemplos
práticos.
Convenções de código usadas no livro
OcódigoJavautilizadonolivroaparecedestacadodeduasformas:em
blocosdecódigocomformata çãodiferenciada,quebradosporexplica ções;
ounaslinhasdotextocomformata çãomaissimples,geralmentequandonos
referirmosanomesdemétodosouvariáveis.
Nemsempreconseguimosmanteraindenta çãodecódigodesejada,de-
vidoàlarguradapágina.Códigosquejáforamexplicadosoutenhampouca
importânciaparacontextodaexplica çãoserãosubstituídospor "...".
Ferramentas e código-fonte: Java, Eclipse e GitHub
UsamosoJavaparadesenvolverosjogosdestelivro,eomotivoéqueo
iv
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 9

CasadoCódigo
Javaémaisqueumalinguagemdeprograma ção,éumaplataformadedesen-
volvimento,presenteemdiversosdispositivosemilharesdecomputadores.
MuitoprovavelmentevocêjátenhaamáquinavirtualJava( Java Virtual
Machine,ouJVM)instaladaemseucomputador.Sequiserverificaroubaixar,
acessehttp://java.com/pt_BR/.
UtilizamoscomoAmbientedeDesenvolvimentoIntegrado( Integrated
Development Environment,ouIDE)oEclipse,masvocêpodeutilizaroutras
IDEs,comoporexemplo,oNetBeans.
Usamostambémumrepositóriopúblicoparaosfontesdestelivro,para
queosleitorespossamcontribuircomseuspróprioscódigos,sejacriando
maisfasesemelhoriasounovasversõesdosjogosabordados.
Escolhemos o Git, um poderoso versionador de código. Usamos o
GitHub,queéumrepositórioGitnaweb,ondeseususuáriospodemcom-
partilharseuscódigosdemaneirapúblicaeprivada(pago).
Para obter os fontes, basta acessar https://github.com/logicadojogo/
fontes.
Vocêtambémpodeparticipardonossogrupodediscussão,em: http:
//forum.casadocodigo.com.br.
Aspróximasse çõessãoparaosleitoresquenãoestãofamiliarizadoscom
algumasdasferramentasutilizadasnolivro.
Instalação do Java para desenvolvedores
CasoaindanãodesenvolvautilizandoJavaequeirafazê-lo,recomenda-
mosainstala çãodoKitdeDesenvolvimento( Java Development Kit,ouJDK).
Váemhttp://www.oracle.com/technetwork/java/javase/downloads/,eclique
noíconededownloadparabaixaraúltimaversão.
v
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 10

CasadoCódigo
Fig.1:BaixandoJDK
Napróximapágina,apósaceitarocontratodelicen ça( Accept License
Agreement),escolhaaversãodoseusistemaoperacional:
vi
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 11

CasadoCódigo
Fig.2:EscolhendoaversãoparaseuSistemaOperacional
Sigaasetapasdeinstala çãopadrãoclicandoem Próximo(Next)
Fig.3:Etapasdainstala ção
Aofinaldainstala ção,cliqueem Fechar(Close).UmavezcomoJavains-
vii
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 12

CasadoCódigo
talado,vocêpodecompilareexecutaroscódigosdestelivroutilizandoalguns
comandos,masofaremosapartirdoEclipse.
Baixando o código-fonte do projeto
Em https://github.com/logicadojogo/fontes, você encontrará as duas
principaisversõesdocódigodivididasemduas branches.
Na branch master,temosocódigoprincipalexplicadonoscapítulose,na
branch desafios,temosocódigocomasmodifica çõesreferentesaosdesafios
propostosnolivro.
Fig.4:Escolhendoabranchparadownload
Vocênãoprecisaterumacontacadastradaparaacessarocódigodolivro,
bastaclicarem Download ZIP,noladodireitoinferiordatela.
viii
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 13

CasadoCódigo
Fig.5:BaixandoZip
Apósbaixareextrairosarquivos,temososcódigosdoprojetoseparados
empastasreferentesaoscapítulosdolivro:
ix
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 14

CasadoCódigo
Fig.6:Pastasseparadasporcapítulos
Depoisdisso,paravocêanalisar,melhorar,personalizarousimplesmente
jogarosjogosdesenvolvidosnestelivro,sóprecisamosimportaroscódigos-
fontedoscapítuloscomoumnovoprojetonoEclipse.
x
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 15

CasadoCódigo
Prefácio
Público-alvo
Oprincipalpúblico-alvodestelivrosãodesenvolvedoresiniciantesindepen-
dentes–nãonecessariamentedesenvolvedoresJava–quedesejamaprender
acriarseusprópriosjogos,tendocomobaseosgrandesclássicos:SpaceIn-
vaders,Pong,Blockade,Tetris,Pac-ManeAsteroids.
Masestelivrotambémpodeserusadoporoutrosinteressadosnomundo
dosjogos,sejaparaconhecerumpoucomaissobreJava,acomplexidadee
lógicadecadajogo,parafazerportedojogoparaoutraplataforma,paracriar
umaversãoprópriadocódigo-fontedolivro,ouporsimplescuriosidadedeste
mundotãodesafiador.
Pré-requisitos
Émuitoimportanteterconhecimentoemlógicadeprograma çãoefun-
damentosdeOrienta çãoaObjetos(OO)paraaproveitarcompletamenteo
conteúdodolivro,emborautilizemosobásicodeOOederecursosdoJava,
queestãopresentesnamaioriadaslinguagensdeprograma ção.
SevocêjápossuirconhecimentoemJava,conseguirátirar100%depro-
veitodestelivro.Jácasoaindanãosesintamuitoconfortávelcomalingua-
gem,aeditoraCasadoCódigopossuiummaterialparaagradardesdeinici-
antesatévelhosdeguerra.
xi
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 16

E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 17

CasadoCódigo
Sobre o autor
MarcusBecker BacharelemSistemadeInformao,etrabalhacomtecnologia
desde2005.ComeoucomFlash,HTMLeJavaScript,depoisPHP,atquese
apaixonoupeloJavaapontodetirarcertificaoem2009.Jdesenvolveudiver-
sospequenosjogosemdiversaslinguagensdeprogramao,mas,desde2012,
vemsededicandoacriarjogos2DcomJavaeAndroid,criandosuaprpria
GameEngine.Descubramaisemhttps://github.com/marcusbecker.
xiii
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 18

E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 19

CasadoCódigo Sumário
Sumário
1 Protótipo de jogo 1
1.1 Desenhandonajanela. . . . . . . . . . . . . . . . . . . . . . . 2
1.2 Movendoascoisaspelatela. . . . . . . . . . . . . . . . . . . . 7
1.3 Interatividade. . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
1.4 Objetivosedesafios . . . . . . . . . . . . . . . . . . . . . . . . 20
1.5 Caixadeferramentas . . . . . . . . . . . . . . . . . . . . . . . 27
1.6 Resumo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
2 Invasão por Space Invaders 29
2.1 Estruturadojogo . . . . . . . . . . . . . . . . . . . . . . . . . 31
2.2 Jogandoocódigo . . . . . . . . . . . . . . . . . . . . . . . . . 35
2.3 Odiscochefevoador . . . . . . . . . . . . . . . . . . . . . . . 42
2.4 Osinvasoresmarcham . . . . . . . . . . . . . . . . . . . . . . 44
2.5 Codificandoojogo . . . . . . . . . . . . . . . . . . . . . . . . 50
2.6 Resumo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
3 Meu nome é Pong, Ping Pong 51
3.1 Separandoateladocenário . . . . . . . . . . . . . . . . . . . 52
3.2 Jogandoocódigo . . . . . . . . . . . . . . . . . . . . . . . . . 62
3.3 Codificandoojogo . . . . . . . . . . . . . . . . . . . . . . . . 74
3.4 Resumo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
xv
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 20

Sumário CasadoCódigo
4 Jogo da cobrinha 77
4.1 Níveis:aquiloquevocêfazparareaproveitarocenário. . . . 78
4.2 Jogandoocódigo . . . . . . . . . . . . . . . . . . . . . . . . . 85
4.3 Codificandoojogo . . . . . . . . . . . . . . . . . . . . . . . . 92
4.4 Resumo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
5 T etris ou Quatro Quadrados 95
5.1 Umjogodearrays . . . . . . . . . . . . . . . . . . . . . . . . . 96
5.2 Desenhandoarrays . . . . . . . . . . . . . . . . . . . . . . . . 102
5.3 Jogandoocódigo . . . . . . . . . . . . . . . . . . . . . . . . . 105
5.4 Efeitossonoros . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
5.5 Tetrissonoro . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120
5.6 Programar,desenhareaindaterdecompor?. . . . . . . . . . 124
5.7 Codificandoojogo . . . . . . . . . . . . . . . . . . . . . . . . 125
5.8 Resumo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
6 Pac-Man, vulgo Come-come 127
6.1 Caçafantasma . . . . . . . . . . . . . . . . . . . . . . . . . . . 129
6.2 Jogandoocódigo . . . . . . . . . . . . . . . . . . . . . . . . . 141
6.3 UmpoucodeI.A.nãofazmal . . . . . . . . . . . . . . . . . . 151
6.4 Codificandoojogo . . . . . . . . . . . . . . . . . . . . . . . . 158
6.5 Resumo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158
7 Come-come e os bitmaps 161
7.1 Umaimagemvalemaisdoquemillinhasdecódigo . . . . . 163
7.2 Jogandoocódigo . . . . . . . . . . . . . . . . . . . . . . . . . 172
7.3 Codificandoojogo . . . . . . . . . . . . . . . . . . . . . . . . 185
7.4 Resumo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 186
8 Um jogo de ângulos e rota ções 187
8.1 Rotação . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 188
8.2 Escalonamentoetransi ção . . . . . . . . . . . . . . . . . . . . 195
8.3 Umjogoparagirareatirar . . . . . . . . . . . . . . . . . . . . 198
xvi
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 21

CasadoCódigo Sumário
8.4 Jogandoocódigo . . . . . . . . . . . . . . . . . . . . . . . . . 205
8.5 Codificandoojogo . . . . . . . . . . . . . . . . . . . . . . . . 213
8.6 Resumo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 215
9 Asteroids: o jogo que sabe representar a física 217
9.1 Umébom,doisémultiplayer . . . . . . . . . . . . . . . . . . 218
9.2 Dividirparadestruir. . . . . . . . . . . . . . . . . . . . . . . . 229
9.3 Jogandoocódigo . . . . . . . . . . . . . . . . . . . . . . . . . 233
9.4 Codificandoojogo . . . . . . . . . . . . . . . . . . . . . . . . 251
9.5 Resumo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 253
10 Última fase, último chefe e próximos jogos 255
10.1 Desafios . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 256
10.2 Useacaixadeferramentasparacriarseusprópriosjogos . . 271
11 Referências bibliográficas 273
Versão:19.2.8
xvii
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 22

E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 23

Capítulo1
Protótipodejogo
Nestecapítulo,criaremosabaseparaosjogosqueserãodesenvolvidosnos
capítulosseguintes.Acadanovocapítuloejogocriado,aumentaremosnossa
bibliotecadecódigo.
Veremosnaspróximasse ções,códigoapóscódigo,comocriarnossopro-
tótipodejogopassandopelasetapas:
• Desenho;
• Animação;
• Interação;
• Objetivos;
• Desafios.
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 24

1.1. Desenhandonajanela CasadoCódigo
1.1 D esenhando na janela
Fig.1.1:Primeirajanela
Gostodepensarnosjogoseletrônicoscomo“umaanima çãointerativacom
objetivosedesafios”. Então,vamosdividirodesenvolvimentodojogobase
assim. Paraanimar,precisamosdesenhare,paradesenhar,precisamosde
umatela;eatela,porsuavez,precisadeumajanela/moldura.Paracriaruma
janelaemJavaésimples,fa çaassim:
package br.com.mvbos.lgj;
import javax.swing.JFrame;
public class Janela extends JFrame {
public Janela() {
setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
setSize(640, 480);
setVisible(true);
2
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 25

CasadoCódigo Capítulo1. Protótipodejogo
}
public static void main(String[] args) {
new Janela();
}
}
Criamosumaclassechamada Janelaqueestende JFrame,quevocê
podepensarcomoumamoldura.Depois,nométodoconstrutor,definimos
aaçãopadrãoaoclicarnobotãofechardajanela.Logoabaixo,definimoso
tamanho(640delargurapor800dealtura),eexibimosajanelachamandoo
método setVisible(true).
Seajanela( JFrame)énossamoldura, nossateladepinturaseráo
JPanel.Maso JPanelnãoseráumaboateladepinturaparajogosamenos
quemodifiquemosalgunsdeseuscomportamentospadrão.Porisso,emvez
deinstanciarmosumobjeto,criaremosumaclassequeestenda JPanele,
assim,teremosmaiorcontrolesobreela.
UsaremosoatalhoqueJavanosfornece,armazenandonanossavariável
telaainstânciadaclassesobrescrita,dessaforma:
Package br.com.mvbos.lgj;
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;
public class Janela extends JFrame {
private JPanel tela;
public Janela() {
tela = new JPanel() {
@Override
public void paintComponent(Graphics g) {
// A pintura ocorre aqui
}
};
3
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 26

1.1. Desenhandonajanela CasadoCódigo
super.getContentPane().add(tela);
setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
setSize(640, 480);
setVisible(true);
}
public static void main(String[] args) {
new Janela();
}
}
Dica
Nãoconfundir paintComponentcom paintComponents,usea
versãonosingular.
Assim,podemospersonalizarométodo paintComponent,queparafa-
cilitarnossavida,nosforneceoobjeto Graphics,evocêpodepensarnele
comosendonossopincel.Depoisdecriadaatela,bastaadicioná-lanamol-
durachamando super.getContentPane().add(tela).
Temosamoldura( JFrame),atela( JPanel)eopincel( Graphics),
comissojápodemosdesenhar:
package br.com.mvbos.lgj;
import java.awt.Color;
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;
public class AnimaTelaDesenho extends JFrame {
private JPanel tela;
public AnimaTelaDesenho() {
tela = new JPanel() {
@Override
4
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 27

CasadoCódigo Capítulo1. Protótipodejogo
public void paintComponent(Graphics g) {
g.setColor(Color.BLUE);
g.drawLine(0, 240, 640, 240);
g.drawRect(10, 25, 20, 20);
g.drawOval(30, 20, 40, 30);
g.setColor(Color.YELLOW);
g.drawLine(320, 0, 320, 480);
g.fillRect(110, 125, 120, 120);
g.fillOval(230, 220, 240, 230);
g.setColor(Color.RED);
g.drawString("Eu seria um ótimo Score!", 5, 10);
}
};
getContentPane().add(tela);
setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
setSize(640, 480);
setVisible(true);
tela.repaint();
}
public static void main(String[] args) {
new AnimaTelaDesenho();
}
}
Dentrodométodo paintComponent,antesdachamadaparaométodo
dedesenho,definimosacorcomaqualessedesenhoserápintado(azul).
Desenhamosumalinhareta( g.drawLine)nahorizontal,umquadrado(
g.drawRect)eumaoval( g.drawOval)sempreenchimento. Sendoque
osdoisprimeirosparâmetrossãoreferentesaoposicionamentonatela,eixo
XeY.Osdoisúltimossãoreferentesaotamanhododesenho.
Logoabaixo,depoisdedefinirmosacoramarela,desenhamosumali-
nhacentralizadanavertical,comnossoquadradoeumovalpreenchidos(
fillRecte fillOval).Nacorvermelha,utilizamos g.drawStringpara
“desenharmosumafrase”.
5
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 28

1.1. Desenhandonajanela CasadoCódigo
Fig.1.2:Primeirodesenho
Dica:
Lembre-se,osmétodosquecome çamcom drawsãosempreenchi-
mento,eosquecome çamcom fillsãopreenchidos.
Estassãoapenasalgumasfun çõesdedesenhoe,nospróximoscapítulos,
vamosexplorá-lasmelhor.Antesdeutilizarmosasfun çõesdedesenho,seta-
mosacordopincelusandoasconstantesdecoresdoJava.Vocêaindapode
usarsuaprópriacorcriandoumnovoobjeto Color,passandocomoparâ-
metroastonalidadesRGB( Red=vermelho; Green=verde;e Blue=Azul),
dessaforma: Color azulClaro = new Color(135, 206, 250); .
Asfunçõesdedesenhovetorialtêmumaequivalenteparadesenhopre-
enchido(começamcom fill)ouapenasborda(come çamcom draw).Os
6
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 29

CasadoCódigo Capítulo1. Protótipodejogo
doisprimeirosparâmetrossãoasposi çõesdeorigemdoseixosXeYemrela-
çãoàtela,osdoisúltimossãoaalturaelarguraou,nocasodasretas,aposi ção
finaldoseixosXeY,amboscommedi çãoempixel.
Então,paradesenharumalinhavertical( g.drawLine)retanomeioda
tela,definimosqueelainiciaráem320doeixoX,sendoquenossatelatemo
tamanhode640,e0noeixoY.SeueixoXfinalteráomesmovalorinicial;
casocontrário,nãoseriaumalinhareta,eseueixoYfinalseráaalturadatela,
nessecaso,480.
Paradesenharumretângulo(quadradosetivertodososladosiguais)pre-
enchido( g.fillRect),definimosparaoseixosXeY,110e125,comalar-
guraealturade120pixels.Comachamada g.drawString,escrevemosum
textonatelautilizandotamanhoefontepadrão,sendoqueoeixoY(segundo
parâmetro)representaalinhadebasedotexto.
1.2 M ovendo as coisas pela tela
Aanimaçãotemamesmabasedesdequefoicriada.Asimagenssãomostra-
dasemquadros( frames)quemudamacada nsegundos. Agoraquetemos
nossaprimeiraimagem,vamosgerarnovasimagensemostrá-lasemlongos
20framesporsegundo,considerandoquemuitosjogosrodama60FPS.
...
public class AnimacaoTela extends JFrame {
private JPanel tela;
private int fps = 1000 / 20; // 50
private int ct; //contador
private boolean anima = true;
public void iniciaAnimacao() {
long prxAtualizacao = 0;
while (anima) {
if (System.currentTimeMillis() >= prxAtualizacao) {
ct++;
tela.repaint();
prxAtualizacao = System.currentTimeMillis() + fps;
7
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 30

1.2. Movendoascoisaspelatela CasadoCódigo
if (ct == 100)
anima = false;
}
}
}
...
Comoestamostrabalhandocommilissegundos,nossavariável fpsre-
cebeovalor50(1000/20). Avariável ct(nossocontador)éresponsável
pelamudançanatela,sejaalterandooseixosouotamanhodosdesenhos,
enquanto animaencerraráaanimação(o loop)quandoocontadorchegara
100.Esseéonúcleobásicodeumjogo,umla ço( loop)infinitoquefazatua-
lizaçõesepinturasdiversasvezesporsegundo.
Dentro do método iniciaAnimacao, usamos
System.currentTimeMillis para obter o tempo corrente em mi-
lésimos de segundo, e quando esse tempo for maior ou igual ao valor
armazenado na variávelprxAtualizacao, atualizamos o contador e
pintamosatelanovamente.
Depois,passamosovaloratualizadoparaexecutarmosapróximaatuali-
zaçãoe,assim,mantemosumaconstânciadeframesporsegundoatéqueo
contadorcheguea100.Manteraconstânciadetempoémuitoimportante,e
existemtécnicassofisticadasparaisso,veremosumpoucomaisnocapítulo
9.
Dica
Lembre-sedepegarotempocorrentenovamenteapósaatualiza ção
epinturadatela.
...
public AnimacaoTela() {
tela = new JPanel() {
@Override
public void paintComponent(Graphics g) {
// Limpando os desenhos anteriores
8
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 31

CasadoCódigo Capítulo1. Protótipodejogo
g.setColor(Color.WHITE);
g.fillRect(0, 0, tela.getWidth(),
tela.getHeight());
g.setColor(Color.BLUE);
g.drawLine(0, 240 + ct, 640, 240 + ct);
g.drawRect(10, 25 + ct, 20, 20);
g.drawOval(30 + ct, 20, 40, 30);
g.setColor(Color.YELLOW);
g.drawLine(320 - ct, 0, 320 - ct, 480);
g.fillRect(110, 125, 120 - ct, 120 - ct);
g.fillOval(230, 220, 240 + ct, 230);
g.setColor(Color.RED);
g.drawString("Eu seria um ótimo Score! " +
ct, 5, 10);
}
};
getContentPane().add(tela);
setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
setSize(640, 480);
setVisible(true);
tela.repaint();
}
public static void main(String[] args) {
AnimacaoTela anima = new AnimacaoTela();
anima.iniciaAnimacao();
}
}
Nométodo paintComponent,alémdeutilizarmosavariável ctpara
modificarasformasdosdesenhos,aoutraaltera çãoéqueagoraapagamoso
desenhoanterior,desenhandoumretângulobrancoquepreenchetodaatela.
Écomosevirássemosapáginaantesdopróximodesenho.
Sevocêjáestiverpreocupadocomperformance,saibaquealémdeoJava
serumdesenhistaperformático,paraevitarasensa çãodeatrasodurantea
9
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 32

1.2. Movendoascoisaspelatela CasadoCódigo
repinturadatela,usaremosumasegundateladepintura,emoutraspalavras,
um buffer.Oresultadodanossaanima çãoserá:
Fig.1.3:Primeiraanima ção
Assimcomoaclasse Graphics2DdoJava,duranteolivroutilizamoso
sistemadecoordenadasX,Y,sejaparaposicionarajanelaouodesenhodentro
dela. Essesistemautilizapixels(quesãovaloresinteiros)comounidadede
medida,entãoaposi ção 0, 0 estánocantosuperioresquerdo,sendoque
oeixoxaumentaparadireitaeoeixoyparabaixo,podendosernegativoou
maiorqueotamanhodoframe(nestecaso,nãosendovisíveisnodesenho).
Noexemploanterior,criamosumajanelade640pixelsdelargurapor
480pixelsdealtura,entãoseucantosuperioresquerdoé 0, 0 eseucanto
inferiordireito 640, 480. Tendoditoisso,valeadiantarqueamedidade
velocidadequeusamosnosjogoséadepixelsporframe,ou Pixels per frame
(PPF).
10
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 33

CasadoCódigo Capítulo1. Protótipodejogo
1.3 I nteratividade
Nosjogosdehoje,até cutsceneteminteratividade.Ainteratividadeconsiste
emobteraentradadojogadorerefleti-lanojogodealgumaforma. Neste
livro,noslimitaremosatecladoemouse,nãoqueinteragirpormeiodesons
capturadosdomicrofoneouimagensdawebcam,ouumsimplesjoystick,não
sejatentador,masinfelizmentefogedoescopodolivro.
OJavanospermiteregistraroseventosquequeremosmonitorar,como
umcliquedemouseeumateclapressionada. Nocasodocliquedomouse,
oeventoéregistradodiretamentenateladepintura( JPanel). Ajanela(
JFrame)ficaresponsávelpelasentradasdoteclado. Noexemploaseguir,
usamosassetasdotecladoparamoverumquadradoazulpelatela:
package br.com.mvbos.lgj;
import java.awt.*;
import javax.swing.*;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
public class Interativo extends JFrame {
private JPanel tela;
private int px;
private int py;
private boolean jogando = true;
private final int FPS = 1000 / 20; // 50
public void inicia() {
long prxAtualizacao = 0;
while (jogando) {
if (System.currentTimeMillis() >= prxAtualizacao) {
tela.repaint();
prxAtualizacao = System.currentTimeMillis() + FPS;
}
}
}
11
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 34

1.3. Interatividade CasadoCódigo
Começamos inserindo dois novos imports do pacote
java.awt.event: KeyEvente KeyListenere,nacria çãodajanela,
adicionamosnossoouvintedotecladocom super.addKeyListener.
Nométodoconstrutordaclasse,monitoramosapenasoeventodetecla
pressionada( keyPressed)e,quandoeleocorre,atualizamosasvariáveisde
px(posiçãonoeixoX)e py(posiçãonoeixoY).
public Interativo() {
super.addKeyListener(new KeyListener() {
@Override
//Evento para tecla apertada
public void keyTyped(KeyEvent e) {
}
@Override
//Evento para tecla liberada
public void keyReleased(KeyEvent e) {
}
@Override
//Evento para tecla pressionada
public void keyPressed(KeyEvent e) {
int tecla = e.getKeyCode();
switch (tecla) {
case KeyEvent.VK_ESCAPE:
// Tecla ESC
jogando = false;
dispose(); // para fechar a janela
break;
case KeyEvent.VK_UP:
// Seta para cima
py--;
break;
case KeyEvent.VK_DOWN:
// Seta para baixo
py++;
break;
case KeyEvent.VK_LEFT:
12
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 35

CasadoCódigo Capítulo1. Protótipodejogo
// Seta para esquerda
px--;
break;
case KeyEvent.VK_RIGHT:
// Seta para direita
px++;
break;
}
}
});
Por meio da interfaceKeyListener, conseguimos tomar ações de
acordocomoeventoocorrido,eutilizamosasconstantesdaclasse KeyEvent
paranãotermosdenospreocuparoutentardescobrirocódigoreferenteàte-
clapressionada.
tela = new JPanel() {
@Override
public void paintComponent(Graphics g) {
g.setColor(Color.WHITE);
g.fillRect(0, 0,
tela.getWidth(), tela.getHeight());
int x = tela.getWidth() / 2 - 20 + px;
int y = tela.getHeight() / 2 - 20 + py;
g.setColor(Color.BLUE);
g.fillRect(x, y, 40, 40);
g.drawString("Agora eu estou em "
+ x + "x" + y, 5, 10);
}
};
getContentPane().add(tela);
setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
setSize(640, 480);
setVisible(true);
}
13
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 36

1.3. Interatividade CasadoCódigo
public static void main(String[] args) {
Interativo jogo = new Interativo();
jogo.inicia();
}
}
Paradesenharoquadradoazulnocentrodatela,obtemosmetadedota-
manhodatelasubtraindoametadedotamanhodoquadrado,nestecaso,20
pixels. Emboraajanelatenhaotamanhode640,metadedatelaémenor
que320,jáquedevemosconsiderarasbordaseabarradetítulodajanela.
Quandopressionadoparacima,decrementamos px,fazendoodesenhosu-
bir;casocontrário,incrementamos px.Omesmoocorrecom py,movendo
odesenhoparaesquerda(negativo)oudireita(positivo).Outrateclamape-
adaéatecla ESC,quepodeserusadacomopausa,abrirmenusouencerrar
ojogo.
Dica
Oevento keyTypednãoreconheceassetasdoteclado.
Valenotarque,emJava,osouvintessãomonitoradosemuma Thread
separadada Threadprincipal. Então,quandovocêpressionaateclaseta
paracima,porexemplo,avariável pyestásendoatualizaforadotempo
dodesenhode50ms,deixandoojogoinconstante. Outroproblemaéque,
daformaatual,nãoconseguimostrabalharcomduasteclaspressionadasao
mesmotempo.Paraalgunsjogos,issonãofarádiferen ça,paraoutros,trará
problemasdejogabilidadefazendovocêperderprêmiosnessacategoria. A
novaversãoutilizaumaabordagemmelhor:
package br.com.mvbos.lgj;
...
public class Interativo2 extends JFrame {
...
private boolean[] controleTecla = new boolean[4];
public Interativo2() {
14
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 37

CasadoCódigo Capítulo1. Protótipodejogo
this.addKeyListener(new KeyListener() {
@Override
public void keyTyped(KeyEvent e) {
}
@Override
public void keyReleased(KeyEvent e) {
setaTecla(e.getKeyCode(), false);
}
@Override
public void keyPressed(KeyEvent e) {
setaTecla(e.getKeyCode(), true);
}
});
tela = new JPanel() {
@Override
public void paintComponent(Graphics g) {
...
}
};
...
}
Transferimosaresponsabilidadedeiniciarepararamovimenta çãodo
nossoobjetoparaométodo setaTeclaque,alémdereceberocódigodate-
clapressionada( pressed)ouliberada( released),recebetambémumvalorbo-
oleanoparaindicarseestamosliberando( false)oupressionando( true).
public void inicia() {
long prxAtualizacao = 0;
while (jogando) {
if (System.currentTimeMillis() >= prxAtualizacao) {
atualizaJogo();
15
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 38

1.3. Interatividade CasadoCódigo
tela.repaint();
prxAtualizacao = System.currentTimeMillis() + FPS;
}
}
}
private void atualizaJogo() {
if (controleTecla[0])
py--;
else if (controleTecla[1])
py++;
if (controleTecla[2])
px--;
else if (controleTecla[3])
px++;
}
Agora, antes de atualizarmos nossa tela, chamamos o método
atualizaJogo,queatualizaasvariáveisdeacordocomosvaloresdonosso
array controleTecla,controladopelonossométodo setaTeclaquefi-
couassim:
private void setaTecla(int tecla, boolean pressionada) {
switch (tecla) {
case KeyEvent.VK_ESCAPE:
// Tecla ESC
jogando = false;
dispose();
break;
case KeyEvent.VK_UP:
// Seta para cima
controleTecla[0] = pressionada;
break;
case KeyEvent.VK_DOWN:
// Seta para baixo
controleTecla[1] = pressionada;
break;
16
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 39

CasadoCódigo Capítulo1. Protótipodejogo
case KeyEvent.VK_LEFT:
// Seta para esquerda
controleTecla[2] = pressionada;
break;
case KeyEvent.VK_RIGHT:
// Seta para direita
controleTecla[3] = pressionada;
break;
}
}
public static void main(String[] args) {
Interativo2 jogo = new Interativo2();
jogo.inicia();
}
}
Comparadocomaversãoanterior,agoraamovimenta çãodonossoqua-
dradoazulficoumaisfluidaeconstante,alémdepodermosmovimentá-lo
nadiagonal.Observeque,emvezdeatualizarmosaimagemforadotempo
definido,apenasarmazenamosasteclasqueforampressionadaseasquefo-
ramliberadas,utilizandoavariável controleTecla.E,notempodecada
frame,executamosaatualiza çãodojogo,método atualizaJogo(),que
cuidadamovimenta çãodoobjetopelatela.
17
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 40

1.3. Interatividade CasadoCódigo
Fig.1.4:Movendoobjetospelatela
Ouvircliquesdomouseétãosimplesquanto,emboraoeventodearras-
taresoltar( Drag and Drop)exijaumpoucomaisdecódigo. Lembre-sede
que,emvezderegistrarmosoeventoparaajanela,vamosregistrarnatela
( JPanel);casocontrário,teríamosdeconsiderarotamanhodabordaeda
barradetítulo,aoobterasposi çõesecliques.
package br.com.mvbos.lgj;
import java.awt.Point;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
...
public class InterativoMouse extends JFrame {
private JPanel tela;
private int px, py;
private Point mouseClick = new Point();
18
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 41

CasadoCódigo Capítulo1. Protótipodejogo
private boolean jogando = true;
private final int FPS = 1000 / 20; // 50
public InterativoMouse() {
tela = new JPanel() {
...
};
tela.addMouseListener(new MouseListener() {
@Override
public void mouseReleased(MouseEvent e) {
// Botão mouse liberado
}
@Override
public void mousePressed(MouseEvent e) {
// Botão mouse pressionado
}
@Override
public void mouseExited(MouseEvent e) {
// Mouse saiu da tela
}
@Override
public void mouseEntered(MouseEvent e) {
// Mouse entrou na tela
}
@Override
public void mouseClicked(MouseEvent e) {
// Clique do mouse
mouseClick = e.getPoint();
}
});
...
}
19
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 42

1.4. Objetivosedesafios CasadoCódigo
public void inicia() {
...
}
private void atualizaJogo() {
px = mouseClick.x;
py = mouseClick.y;
}
public static void main(String[] args) {
InterativoMouse jogo = new InterativoMouse();
jogo.inicia();
}
}
Assimcomoasteclaspressionadas,passamososvaloresparaavariável
mouseClickquelemosnaatualiza çãodojogo. Nãonosimportamoscom
qualbotãoocliqueérealizado,nemcomosoutroseventos,masnospróximos
capítulos,exploraremosmaissobreoassunto.
1.4 O bjetivos e desafios
Umobjetivoporsisójárepresentaumdesafio,masnessecaso,desafiossão
pensadospelodesenvolvedordojogoparagerarumasensa çãodeconquista
(àsvezes,ódio)nojogador. Particularmentefalando,estaéumaetapade
grandeprazernodesenvolvimentodojogo,elaborardesafios,pensandoem
comoedequeformaoutraspessoasvãosuperá-los.Comobásicoquevimos
atéagora,vamoselaborarumpequenodesafio,queseráimpedirquequadra-
dosazuisatravessemalinhacinza.
20
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 43

CasadoCódigo Capítulo1. Protótipodejogo
Nota
Aparentemente,osjogosficaramtãofáceiscomseussalvamentosau-
tomáticoevidainfinita,queumnovogênerodejogosurgiu,conhecido
como Roguelike.Esseestilodejogoprezapeladificuldadecomopartedo
desafiodojogador,videcomoexemplo,asérie Dark Souls.
Fig.1.5:Umjogo
Oobjetivoéfazê-lopelomaiortempopossível,conseguindoamaiorpon-
tuação.Usaremosumcódigocompacto,evitandoconversõesepadrões,mas
nãoseacostume,ésódessavez.
package br.com.mvbos.lgj;
21
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 44

1.4. Objetivosedesafios CasadoCódigo
//... Ocultamos os imports
public class UmJogo extends JFrame {
private final int FPS = 1000 / 20; // 50
class Elemento {
public int x, y, largura, altura;
public float velocidade;
public Elemento(int x, int y, int width, int height) {
this.x = x;
this.y = y;
this.largura = width;
this.altura = height;
}
}
private JPanel tela;
private boolean jogando = true;
private boolean fimDeJogo = false;
private Elemento tiro;
private Elemento jogador;
private Elemento[] blocos;
private int pontos;
private int larg = 50; // Largura padrão
private int linhaLimite = 350;
private java.util.Random r = new java.util.Random();
private boolean[] controleTecla = new boolean[4];
Definimosumaclasseinternachamada Elemento,quecontémaspro-
priedadescomunsaostrêselementosdojogo( blocos, jogadore tiro).
Declaramosalgumasvariáveisjáconhecidasealgumasnovasparacontrolar
ojogo,quevocênãoprecisasepreocuparagora,jáqueveremoscommais
detalhesemcapítulosfuturos.
22
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 45

CasadoCódigo Capítulo1. Protótipodejogo
public UmJogo() {
this.addKeyListener(new KeyListener() {
...
});
tiro = new Elemento(0, 0, 1, 0);
jogador = new Elemento(0, 0, larg, larg);
jogador.velocidade = 5;
blocos = new Elemento[5];
for (int i = 0; i < blocos.length; i++) {
int espaco = i * larg + 10 * (i + 1);
blocos[i] = new Elemento(espaco, 0, larg, larg);
blocos[i].velocidade = 1;
}
Nométodoconstrutordaclasse,configuramosotamanhodotiro(1de
largura,0dealtura),aposi çãoserárelativaaojogador.Tantoojogador(qua-
dradoinferiorverde)quantoosobstáculos(quadradossuperioresazuis)têm
omesmotamanho,masavelocidadedelesédiferente:5paraojogadore1
paraosobstáculos,quesãoposicionadosladoaladocomumespa çamento
de10pixelsentreeles.
tela = new JPanel() {
private static final long serialVersionUID = 1L;
@Override
public void paintComponent(Graphics g) {
g.setColor(Color.WHITE);
g.fillRect(0, 0,
tela.getWidth(), tela.getHeight());
g.setColor(Color.RED);
g.fillRect(tiro.x, tiro.y,
tiro.largura, tela.getHeight());
g.setColor(Color.GREEN);
23
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 46

1.4. Objetivosedesafios CasadoCódigo
g.fillRect(jogador.x, jogador.y,
jogador.largura, jogador.altura);
g.setColor(Color.BLUE);
for (Elemento bloco : blocos) {
g.fillRect(bloco.x, bloco.y,
bloco.largura, bloco.altura);
}
g.setColor(Color.GRAY);
g.drawLine(0, linhaLimite,
tela.getWidth(), linhaLimite);
g.drawString("Pontos: " + pontos, 0, 10);
}
};
getContentPane().add(tela);
...
setResizable(false);
jogador.x = tela.getWidth() / 2 - jogador.x / 2;
jogador.y = tela.getHeight() - jogador.altura;
tiro.altura = tela.getHeight() - jogador.altura;
}
public void inicia() {
...
}
Estamosutilizandoosmétodosjáconhecidosparadesenho,masosva-
loresestãonopróprioobjeto Elemento.Alémdenãodeixarmosatelaser
redimensionadacom setResizable(false),definimosaposi çãoinicial
do jogadoredo tirousandocomobaseotamanhoda tela.
Nométodo atualizaJogo,movemosojogadornahorizontalcon-
formeateclapressionada,semprevalidandoparaque,seelesairdatela,apa-
reçadoladooposto,eposicionamosotirocentralizadonojogador.
24
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 47

CasadoCódigo Capítulo1. Protótipodejogo
private void atualizaJogo() {
if (fimDeJogo)
return;
if (controleTecla[2])
jogador.x -= jogador.velocidade;
else if (controleTecla[3])
jogador.x += jogador.velocidade;
if (jogador.x < 0)
jogador.x = tela.getWidth() - jogador.largura;
if (jogador.x + jogador.largura > tela.getWidth())
jogador.x = 0;
tiro.y = 0;
tiro.x = jogador.x + jogador.largura / 2;
Paracadabloco,verificamossealgumpassoutotalmentedalinhalimite;
casoaconteça,encerramosojogo.Quandoalgum blococolidircomo tiro
(veremosmelhordetec çãodecolisãoaseguir),elevoltarágradualmenteao
topodatelacomodobrodavelocidadededecida.Casonãoocorraacolisão,
descemoso blocoutilizamosofator sorte.
for (Elemento bloco : blocos) {
if (bloco.y > linhaLimite) {
fimDeJogo = true;
break;
}
if (colide(bloco, tiro) && bloco.y > 0) {
bloco.y -= bloco.velocidade * 2;
tiro.y = bloco.y;
} else {
int sorte = r.nextInt(10);
if (sorte == 0)
bloco.y += bloco.velocidade + 1;
25
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 48

1.4. Objetivosedesafios CasadoCódigo
else if (sorte == 5)
bloco.y -= bloco.velocidade;
else
bloco.y += bloco.velocidade;
}
}
pontos = pontos + blocos.length;
}
private boolean colide(Elemento a, Elemento b) {
if (a.x + a.largura >= b.x && a.x <= b.x + b.largura) {
return true;
}
return false;
}
private void setaTecla(int tecla, boolean pressionada) {
...
}
public static void main(String[] args) {
UmJogo jogo = new UmJogo();
jogo.inicia();
}
}
Mesmoparaumprotótipo,precisamosdebastantecódigo.Temoscódigo
parapintaratela,atualizarosobjetos,receberetrataraentradadojogador,
verificarcolisões.Eotamanhodocódigosótendeacrescerconformevamos
construindonovosjogosnoscapítulosseguintes.Então,usaremosopoderda
OrientaçãoaoObjeto,alémdereaproveitarmospartescomunsentreosjogos,
criandoeampliandonossacaixadeferramentasdecódigoparafazemosmais
jogoscommenostrabalho.
26
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 49

CasadoCódigo Capítulo1. Protótipodejogo
1.5 C aixa de ferramentas
Nossoprimeiroitemdacaixadeferramentaséaclasse Util,quevemcomo
métodomaisutilizadodetodososjogos,responsávelpeladetec çãodecolisão
nojogo,maisprecisamentecolisãoentreosobjetosdaclasse Elemento.
Nota
Eu,comoleitor,prefironomescurtosparavariáveis,assimficamenos
cansativodigitarocódigodeexemplo.Porisso,adoteiessaabordagem
paraescreverolivro.
package br.com.mvbos.lgj.base;
public class Util {
public static boolean colide(Elemento a, Elemento b) {
if (!a.isAtivo() || !b.isAtivo())
return false;
//posição no eixo X + largura do elemento A e B
final int plA = a.getPx() + a.getLargura();
final int plB = b.getPx() + b.getLargura();
//posição no eixo Y + altura do elemento A e B
final int paA = a.getPy() + a.getAltura();
final int paB = b.getPy() + b.getAltura();
if (plA > b.getPx() && a.getPx() < plB
&& paA > b.getPy() && a.getPy() < paB) {
return true;
}
return false;
}
}
Nospróximosjogos,algunselementospodemfazerpartedojogo,mas
nãoestarativos,.Assim,porconveniência,colisõescomelementosinativos
27
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 50

1.6. Resumo CasadoCódigo
retornamfalso.
Primeiramente,obtemosaposi çãomaislargurado Elemento a ( pla)
e Elemento b ( plb),comotambémaposi çãomaisalturadeambos( paA
e paB).Sendoque,paraalargura,consideramosoeixoXealturaoeixoY.
Depoisdisso,verificamosacolisãototal(noseixosXeY),checandosea
posiçãosomadaalarguradoobjetoAémaioraposi çãodoobjetoB,esea
posiçãodoobjetoAémenoraposi çãomaisalarguradoobjetoB.Fazemos
omesmoprocessoparaaaltura.Seasduasprimeirasvalida çõesderemver-
dadeiro,temosumacolisãonoeixoX;seasduasúltimasderemverdadeiro,
umacolisãonoeixoY.
Fig.1.6:Colisões
Nafigura1.6,osdoisprimeirosquadradosnãoestãocolidindo;jánose-
gundoquadro,elescolidemnoseixosX.Noterceiroquadro,temosacolisão
emambososeixos;porfim,noúltimo,somenteacolisãonoeixoY.
Criaremosjogosemqueosobjetosserãoposicionadosmuitopróximos
umdooutro,então,consideramoscolisãoapenasseaposi çãodeumdelesfor
maior,enãomaiorouigual,adooutroelemento.
Valelembrarqueocódigo-fontecompletopode(edeve)serbaixadoem
https://github.com/logicadojogo/fontes.
1.6 R esumo
Nestecapítulo,vimosalgunselementosbásicosquecompõemumjogocomo:
desenho,interatividadeeanima ção. Criamosumprotótipodejogoenossa
funçãoparadetectarcolisão.Estamossónosaquecendo,queosjogoscome-
cem.Aliás,quecomecemososjogos!
28
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 51

Capítulo2
InvasãoporSpaceInvaders
SpaceInvaders,ojogoquefezoJapãotriplicarsuaprodu çãodemoedasde
100-yen(elesnãousavamfichasdefliperama),foidesenvolvidopelaTaito
Corporation,em1978noJapão,elan çadoemoutubrodomesmoanonos
EstadosUnidospelaMidway.Nestecapítulo,abordaremoscombaseemas-
pectosdojogooriginal:
• Movimentaçãodojogadoreinimigos;
• Tirosnavertical;
• Pontuação;
• Aumentodedificuldade;
• Animaçãodosinimigos;
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 52

CasadoCódigo
Fig.2.1:Visualizaçãodojogo
30
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 53

CasadoCódigo Capítulo2. InvasãoporSpaceInvaders
2.1 E strutura do jogo
Umjogoéformado,porentreoutrascoisas,deelementosequaisquercoisas
queesseselementossejam,porexemplo:naves,tanques,carros,pássaroszan-
gados...todoselestêmaspectosemcomum,comoposi ção,tamanhoea ções.
Nossotanqueatira,nossanavevoa,eassimpordiante.Porisso,paranossos
jogos,teremosumaclasse Elementoqueinicialmenteseparececom:
package br.com.mvbos.lgj.base;
import java.awt.Color;
import java.awt.Graphics2D;
public class Elemento {
private int px;
private int py;
private int largura;
private int altura;
private int vel;
private boolean ativo;
private Color cor;
public Elemento() { }
public Elemento(int px, int py, int largura, int altura) {
this.px = px;
this.py = py;
this.largura = largura;
this.altura = altura;
}
Vimosalgoparecidonocapítuloanterior,masvalerelembrarque px,
py, largurae alturasãopropriedadesqueutilizamosmuitonahorade
desenharedetectarcolisõescomoutroselementosdojogo. Paracontrolar
avelocidadedopersonagem,usamosapropriedade vele,seelepodeser
atualizadooudesenhado,utilizamosapropriedade ativo.Eenquantonão
trabalhamoscomimagens,usaremosapropriedade corparadarmaisvida
aojogo.
31
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 54

2.1. Estruturadojogo CasadoCódigo
public void atualiza() { }
public void desenha(Graphics2D g) {
g.drawRect(px, py, largura, altura);
}
public void incPx(int x) { px = px + x; }
public void incPy(int y) { py = py + y; }
Ummétodoparaatualizareoutroparadesenharsãodoismétodosque
todosnossoselementosdevemter.Porpadrão,nossaclasse Elementonão
faznenhumaatualiza çãoedesenhaumretângulosempreenchimentocom
basenaposi çãoetamanho. Elatambémvemdefábricacomdoismétodos
auxiliaresparafacilitaramudan çadeposi çãodoelementonatela( incPx()
e incPy()). Osoutrosmétodossãoparaacessarosatributosprivadosda
classe:
public int getLargura() {
return largura;
}
public void setLargura(int largura) {
this.largura = largura;
}
public int getAltura() {
return altura;
}
public void setAltura(int altura) {
this.altura = altura;
}
public int getPx() {
return px;
}
public void setPx(int px) {
this.px = px;
32
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 55

CasadoCódigo Capítulo2. InvasãoporSpaceInvaders
}
public int getPy() {
return py;
}
public void setPy(int py) {
this.py = py;
}
public int getVel() {
return vel;
}
public void setVel(int vel) {
this.vel = vel;
}
public boolean isAtivo() {
return ativo;
}
public void setAtivo(boolean ativo) {
this.ativo = ativo;
}
public Color getCor() {
return cor;
}
public void setCor(Color cor) {
this.cor = cor;
}
}
33
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 56

2.1. Estruturadojogo CasadoCódigo
Dica
NoEclipse,depoisdedeclararqualquerpropriedadedaclasse,utilize
oatalho: ALT + SHIFT + S ecliqueem Generate Getters and
Setters...paragerarosmétodos gete setdelas.
Osprincipaisobjetosdosnossosjogosvãoestenderdaclasse Elemento,
assim, além de reaproveitarmos os comportamentos e atributos em co-
mum,muitosmétodosprecisarãosimplesmentesaberquenossoobjetoéum
Elemento,comoporexemplo,ométodo Colidedaclasse Util.
Quandoumelementodojogoformuitogenérico,eleseráumainstância
diretadaclasse Elemento,como Elemento el = new Elemento() .
Quando precisarmos personalizar algum comportamento, instanciaremos
dessaforma: Elemento tanque = new Tanque() . Casonossaimple-
mentaçãoadicionenovoscomportamentos,adeclara çãoseráamesmada
classequeinstanciarmos: Invader chefe = new Invader() .
Aestruturadonossoprojetoficouconformeafigura:
Fig.2.2:Estruturadoprojeto
34
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 57

CasadoCódigo Capítulo2. InvasãoporSpaceInvaders
2.2 J ogando o código
Asnavesinimigasestãoalinhadaseemperfeitasincronia,indodaesquerda
paraadireitaeavan çandoparaaparteinferiordatela,conformecolidemcom
aslaterais.Quantomaisnavesderrubar,maisrápidoseráoavan çodasrestan-
tes,atéqueaúltimapare çao The Flashemdiadecorrida.Enquantoaúnica
nave(nestejogo,tanque)defendeaTerracommovimentosnahorizontale
umtiroporvez.
Temostrêsobjetosprincipais, Invader, Tanquee Tiro,queestendem
daclasse Elementoemodificamouacrescentamnovoscomportamentos.
Chamamosaclassede Invaderemhomenagemaojogo,estesserãoosini-
migosinvasores.
Paragerenciarasnavesinimigas,criamosumamatrizmultidimensional
(arraydearrays),11por5,tendoumtotalde55inimigosmaisochefe,que
tambéméumobjeto Invader,massemovesomentenahorizontal.
...
private Invader[][] invasores = new Invader[11][5];
private Invader.Tipos[] tipoPorLinha = { Tipos.PEQUENO,
Tipos.MEDIO, Tipos.MEDIO, Tipos.GRANDE, Tipos.GRANDE };
...
private void carregarJogo() {
...
for (int i = 0; i < invasores.length; i++) {
for (int j = 0; j < invasores[i].length; j++) {
Invader e = new Invader(tipoPorLinha[j]);
e.setAtivo(true);
e.setPx(i * e.getLargura() + (i + 1) * espacamento);
e.setPy(j * e.getAltura() + j * espacamento +
linhaBase);
invasores[i][j] = e;
}
35
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 58

2.2. Jogandoocódigo CasadoCódigo
}
...
}
Cadalinhatemumtipodeinimigo,usamosoarray tipoPorLinha,que
armazenaosvaloresdanossaenumera ção( enum,queagrossomodosão
constantescommaisrecursos)definidosnaclasse Invaderparacontrolar
isso.
Osinimigossãoposicionadosumaoladodooutroeoposicionamento
horizontallevaemcontaalarguradecadamaisumespa çamentoadicional,
porexemplo,considerandoqueoinimigoocupe20pixelseoespa çamento
sejade15,oprimeiro Invadercomeçaránaposição15(0*20+1*15),eo
segundonaposi ção50(1*20+2*15),assimpordiante.
Omesmoéfeitoparaposicioná-losemlinha,mas,nestecaso,utilizamos
umespaçomaior(60pixels),deixandoespa çoparaescrevemosapontua ção
eolevelnotopodatela.
Utilizamosumcontadorparacontrolaramarchadosinvasores.Quanto
menorforonúmerodeinimigos,menorseráotempodeesperaparaamo-
vimentaçãodeles:
...
// Parte do código dentro do loop do jogo
if (contador > contadorEspera) {
moverInimigos = true;
contador = 0;
contadorEspera = totalInimigos - destruidos - level * level;
} else {
contador++;
}
Acadaframe(loopdojogo),incrementamosavariável contadore,
quandoelaformaiorque contadorEspera,quesimplesmenteéototalde
inimigossubtraindoosinimigosdestruídoseodobrodolevel,movemosos
invasores.Então,acadaavan çodenível,ojogoficamaisdifícil.
if (tanque.isAtivo()) {
if (controleTecla[2]) {
36
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 59

CasadoCódigo Capítulo2. InvasãoporSpaceInvaders
tanque.setPx(tanque.getPx() - tanque.getVel());
} else if (controleTecla[3]) {
tanque.setPx(tanque.getPx() + tanque.getVel());
}
}
// Pressionou espaço, adiciona tiro
if (controleTecla[4] && !tiroTanque.isAtivo()) {
tiroTanque.setPx(tanque.getPx() + tanque.getLargura() / 2
- tiroTanque.getLargura() / 2);
tiroTanque.setPy(tanque.getPy() - tiroTanque.getAltura());
tiroTanque.setAtivo(true);
}
if (chefe.isAtivo()) {
chefe.incPx(tanque.getVel() - 1);
if (!tiroChefe.isAtivo() && Util.colideX(chefe, tanque)) {
addTiroInimigo(chefe, tiroChefe);
}
if (chefe.getPx() > tela.getWidth()) {
chefe.setAtivo(false);
}
}
Senosso tanqueestiverativo,realizamosomovimentoparaaesquerda
oudireitacasoasteclascorrespondentessejampressionadas.Otirodotanque
edochefe(navequepercorreahorizontalsuperior)sãodisparosemlinhareta
navertical,sendoqueotirodotanquepartedebaixoparacimaquandoo
jogadorpressionaateclaespa ço,eotirodochefedecimaparabaixo,quando
ocorreumacolisãonoeixoX.
Quandoaposi çãodochefeformaiorquealarguradatela,elesetorna
inativo.Veremosmaissobreposicionamentologoaseguir.
Paraostirossaíremprimeiramentedasnavesinferiores,percorremosos
arraydebaixoparacima(domaiorparaomenor):
boolean colideBordas = false;
37
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 60

2.2. Jogandoocódigo CasadoCódigo
// Percorrendo primeiro as linhas, de baixo para cima
for (int j = invasores[0].length - 1; j >= 0; j--) {
// Depois as colunas
for (int i = 0; i < invasores.length; i++) {
Invader inv = invasores[i][j];
if (!inv.isAtivo()) {
continue;
}
if (Util.colide(tiroTanque, inv)) {
inv.setAtivo(false);
tiroTanque.setAtivo(false);
destruidos++;
pontos = pontos + inv.getPremio() * level;
continue;
}
Seoinvasornãoestivermaisativo(foidestruído),passamosparaopró-
ximo.Seeleestavaativoefoiatingidopelotirodonossotanque,inativamos
ambos,atualizamosacontagemdeinimigosdestruídoseaaumentamosa
pontuaçãodojogador,levandoemcontaotipodoinvasoreo leveldojogo.
if (moverInimigos) {
inv.atualiza();
if (novaLinha) {
inv.setPy(inv.getPy() + inv.getAltura() +
espacamento);
} else {
inv.incPx(espacamento * dir);
}
if (!novaLinha && !colideBordas) {
int pxEsq = inv.getPx() - espacamento;
int pxDir = inv.getPx() + inv.getLargura() +
38
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 61

CasadoCódigo Capítulo2. InvasãoporSpaceInvaders
espacamento;
if (pxEsq <= 0 || pxDir >= tela.getWidth())
colideBordas = true;
}
Quandochegaahorademoverosinimigos,verificamosseomovimento
seránavertical(novalinha)ounahorizontal,paraesquerdaoudireitade-
pendendodovalorde dir(1ou-1).Casonãosejaumanovalinhaeacolisão
comasbordasdatelaaindanãotenhasidodetectada,verificamosseopró-
ximomovimentoresultaráemumacolisão.
Setodasasnavesficassememjogootempotodo,precisaríamosverifi-
carapenasaprimeiraeaúltimacoluna,mascomoojogadorpodeeliminar
colunasinteiras,precisamosfazeraverifica çãoindividual.
Osinimigosatirameatirambem,sãoapenastrêstiros,mashácertaIA
(InteligênciaArtificial)neles(falaremosdeIAnocapítulo6.Oprimeirotiro
ésempredolardoesquerdodojogador,osegundonadire çãodojogadoreo
terceirodoladodireito.
if (!tiros[0].isAtivo() && inv.getPx() < tanque.getPx()) {
addTiroInimigo(inv, tiros[0]);
} else if (!tiros[1].isAtivo() &&
inv.getPx() > tanque.getPx() &&
inv.getPx() < tanque.getPx() + tanque.getLargura()) {
addTiroInimigo(inv, tiros[1]);
} else if (!tiros[2].isAtivo() &&
inv.getPx() > tanque.getPx()) {
addTiroInimigo(inv, tiros[2]);
}
if (!chefe.isAtivo() && rand.nextInt(500) == destruidos) {
chefe.setPx(0);
chefe.setAtivo(true);
}
39
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 62

2.2. Jogandoocódigo CasadoCódigo
Todaverificaçãoutilizaaposi çãodoselementosnoeixoX.Agora,sópre-
cisamosfecharaschavesquedeixamosabertas.
}//Fim if moverInimigos
// Desenhe aqui se quiser economizar no loop.
// e.desenha(g2d);
} // Fim do loop colunas
} // Fim do loop linhas
Seotiroinimigoestiverinativo(aindanãofoidisparado,oucolidiucom
ojogadoroualinhadebase),paraoprimeirotiro,verificamosseanavede
ondesairáodisparoestáàesquerdadotanque.Paraosegundo,verificamos
sehouveumacolisãovertical,eparaoterceiro,seanaveestáàdireitado
tanque.
Seo chefenãoestiverativoeonúmeroaleatóriode0à499coincidir
comonúmerodeinimigosdestruídos,teremosumanaveinimigaamaisna
tela.
if (moverInimigos && novaLinha) {
dir *= -1;
novaLinha = false;
} else if (moverInimigos && colideBordas) {
novaLinha = true;
}
moverInimigos = false;
...
Porfim,verificamossehouvemovimenta çãocomnovalinha,oumovi-
mentaçãoecolisão.Paramovimenta çãocomnovalinha,invertemosadire-
ção( dircomvalorpositivovaidaesquerdaparadireitae,comvalornega-
tivo,dadireitaparaesquerda)edesativamosanovalinha. Casoasegunda
verificaçãosejaverdadeira,apróximamovimenta çãoseráparaumanovali-
nha.Ométodoqueadicionatirosdosinvasoreséresponsávelporposicionar
otiroabaixoenocentrodanavequedisparou.
40
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 63

CasadoCódigo Capítulo2. InvasãoporSpaceInvaders
...
public void addTiroInimigo(Elemento inimigo, Elemento tiro) {
tiro.setAtivo(true);
tiro.setPx(inimigo.getPx() +
inimigo.getLargura() / 2 - tiro.getLargura() / 2);
tiro.setPy(inimigo.getPy() + inimigo.getAltura());
}
...
Valelembrarque,paraosdisparoscome çaremdaslinhasinferiores,o
loopéfeitopercorrendoaslinhas(oarraydentrodoarray)deformadecres-
cente.Nonossocódigo,odisparosóéefetuadoquandooinimigosemovi-
menta,masessaescolha,bemcomooutras(espa çamento,velocidade,tama-
nhodatela,elementosdojogoetc.)sãoabordagensquevocêdeveescolher,
deixandoomododejogoaoseugosto.
...
// Pressionou espaco, adiciona tiro
if (controleTecla[4] && !tiroTanque.isAtivo()) {
tiroTanque.setPx(tanque.getPx() +
tanque.getLargura() / 2 - tiroTanque.getLargura() / 2);
tiroTanque.setPy(tanque.getPy() - tiroTanque.getAltura());
tiroTanque.setAtivo(true);
}
...
if (chefe.isAtivo()) {
chefe.incPx(tanque.getVel() - 1);
if (!tiroChefe.isAtivo() && Util.colideX(chefe, tanque)) {
addTiroInimigo(chefe, tiroChefe);
}
if (chefe.getPx() >canvas.getWidth()) {
chefe.setAtivo(false);
}
}
41
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 64

2.3. Odiscochefevoador CasadoCódigo
Osváriosdisparosdessejogosemprepartemdocentrodanaveoudo
tanque,então,sempreestamoscentralizandoalgumacoisausandoumcódigo
semelhanteaeste:
el.getPx() + el.getLargura() / 2 - tiro.getLargura() / 2
Emoutraspalavras,posi çãoXdoelementoorigemmaismetadedota-
manhodoelementoorigemmenosametadedotamanhodoelementoque
queremoscentralizar.Ouseja,alinhamosocentrodanavecomocentrodo
tiro.
Fig.2.3:Alógicadocentralizar
CentralizarnahorizontaléequivalenteasubstituirPxporPyelargura
poraltura. Essaéumaótimafun çãoparairparanossaclasse Util,mas
deixaremosporsuaconta.
2.3 O disco chefe voador
Ochefedojogo(ouquaseisso)éumainstânciadoobjeto Invaderqueapa-
recedeformarandômica,sendoque,nojogooriginal,aapari çãoétempo-
rizada.Elecruzaatelanahorizontaletodavezqueavistaojogador(colide
noeixoX),eledisparaumtiromaislongoemaisrápidoquedosinvasores
comuns.Destacandoochefeeotirodochefe:
...
chefe = new Invader(Invader.Tipos.CHEFE);
42
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 65

CasadoCódigo Capítulo2. InvasãoporSpaceInvaders
tiroChefe = new Tiro(true);
tiroChefe.setVel(20);
tiroChefe.setAltura(15)
...
if (chefe.isAtivo()) {
chefe.incPx(tanque.getVel() - 1);
if (!tiroChefe.isAtivo() && Util.colideX(chefe, tanque)) {
addTiroInimigo(chefe, tiroChefe);
}
if (chefe.getPx() > tela.getWidth()) {
chefe.setAtivo(false);
}
}
...
if (tiroChefe.isAtivo()) {
tiroChefe.incPy(tiroChefe.getVel());
if (Util.colide(tiroChefe, tanque)) {
vidas--;
tiroChefe.setAtivo(false);
} else if (tiroChefe.getPy() > tela.getHeight() 
linhaBase - tiroChefe.getAltura()) {
tiroChefe.setAtivo(false);
} else
tiroChefe.desenha(g2d);
}
...
Quandoo tiroChefeestáativo,eledescenaverticale,casocolidacom
otanque,ojogadorperdeumavidaeodisparoéinativado.Seotirochegar
àlinhadebase,tambéméinativado;casocontrário,eleédesenhadonatela.
43
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 66

2.4. Osinvasoresmarcham CasadoCódigo
2.4 O s inv asores marcham
Aqui,comonojogooriginal,sãotrêstiposdiferentesdeinvasores,sendoque
osmaioresdãomenospontosqueosmenores.Alémdisso,elestêmdoises-
tadosdiferentes,fazendoodesenhovariarconformemarchampelatela.Esse
controleéfeitonaclasse Invader,usandoum enumparaostipos,eum
booleanparavariarodesenho.
package br.com.mvbos.lgj;
import java.awt.Color;
import java.awt.Graphics2D;
import br.com.mvbos.lgj.base.Elemento;
public class Invader extends Elemento {
enum Tipos {
PEQUENO, MEDIO, GRANDE, CHEFE
}
private Tipos tipo;
private boolean aberto;
public Invader(Tipos t) {
this.tipo = t;
setLargura(20);
setAltura(20);
}
@Override
public void atualiza() {
aberto = !aberto;
}
Toda vez que o métodoatualiza é chamado, o valor da variável
abertoéinvertido.Alógicadométodo desenhadámaistrabalho.Cada
tipodeinvasortemseuprópriodesenho,eodesenhomudadependendodo
valordavariável aberto.
44
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 67

CasadoCódigo Capítulo2. InvasãoporSpaceInvaders
Jávimoscomodesenharnoprimeirocapítulo,entãoocódigofoiomitido
porenquanto,masrecomendoquepratiquecomseusprópriosdesenhos.
@Override
public void desenha(Graphics2D g) {
if (!isAtivo())
return;
int larg = getLargura();
if (tipo == Tipos.PEQUENO) {
larg = larg - 2;
g.setColor(Color.BLUE);
if (aberto)
// Desenha um círculo azul com quadrados ao redor
else
// Desenha um quadrado azul
} else if (tipo == Tipos.MEDIO) {
g.setColor(Color.ORANGE);
if (aberto)
// Desenha um quadrado vazio bordas na cor laranja
else
// Desenha um quadrado preenchido na cor laranja
} else if (tipo == Tipos.GRANDE) {
larg = larg + 4;
if (aberto)
// Desenha um retângulo em pé na cor cinza escuro
else
// Desenha um retângulo deitado na cor cinza
} else {
// Tenta desenhar algo parecido com um disco
// voador com luzes piscantes
...
if (aberto) {
45
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 68

2.4. Osinvasoresmarcham CasadoCódigo
// Três quadrados brancos
}
}
}
Alémdeutilizarmoso enum Tipos paradeterminaroformatodode-
senho,usamosparadefinirospontosdojogador. Sendoque,seelenãofor
pequeno,médioougrande,seráochefe,dandomaiorpontua ção.
public int getPremio() {
switch (tipo) {
case PEQUENO:
return 300;
case MEDIO:
return 200;
case GRANDE:
return 100;
default:
return 1000;
}
}
}
Asclasses Tiro, Tanquee Texto,quetambémsãofilhasdaclasse
Elemento,sãoparecidascomaclasse Invader,emboramaissimples. O
quedefineseoelemento Tiroseráusadopelotanqueoupelosinimigoséa
propriedade inimigo.
package br.com.mvbos.lgj;
import java.awt.Color;
import java.awt.Graphics2D;
import br.com.mvbos.lgj.base.Elemento;
public class Tiro extends Elemento {
private boolean inimigo;
public Tiro() {
46
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 69

CasadoCódigo Capítulo2. InvasãoporSpaceInvaders
setLargura(5);
setAltura(5);
}
public Tiro(boolean inimigo) {
this();
this.inimigo = inimigo;
}
@Override
public void atualiza() {
}
@Override
public void desenha(Graphics2D g) {
if (!isAtivo())
return;
g.setColor(inimigo ? Color.RED : Color.WHITE);
g.fillRect(getPx(), getPy(), getLargura(), getAltura());
}
}
Então,seovalorforverdadeiro,sabemosqueotiroédoinimigoeeleserá
desenhadonacorvermelha,casocontrário,nacorbranca. Paraquenosso
Tanquetenhaumformatodetanque(ouquaseisso),fizemostrêsdesenhos.
package br.com.mvbos.lgj;
import java.awt.Color;
import java.awt.Graphics2D;
import br.com.mvbos.lgj.base.Elemento;
public class Tanque extends Elemento {
private final int cano = 8;
private final int escotilha = 10;
public Tanque() {
47
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 70

2.4. Osinvasoresmarcham CasadoCódigo
setLargura(30);
setAltura(15);
}
@Override
public void atualiza() {
}
@Override
public void desenha(Graphics2D g) {
g.setColor(Color.GREEN);
g.fillRect(getPx() + getLargura() / 2 - cano / 2,
getPy() - cano, cano, cano);
g.fillRect(getPx(), getPy(), getLargura(), getAltura());
g.setColor(Color.YELLOW);
g.fillOval(getPx() + getLargura() / 2 - escotilha / 2,
getPy() + getAltura() / 2 - escotilha / 2,
escotilha, escotilha);
}
}
Oprimeiropararepresentarocanodedisparo,osegundoacarca çaeo
terceiroaescotilha,esseúltimoumcírculopreenchidonacoramarela.Vale
ressaltarqueutilizamossomenteumainstânciadaclasse Texto,porisso,
nelanãoarmazenamosinforma çõessobreoqueseráescrito,esimcomqual
fonte,coretamanhoseráescrito.Istoporquetodosostextosdojogoterãoa
mesmaaparência.
package br.com.mvbos.lgj.base;
import java.awt.Font;
import java.awt.Graphics2D;
public class Texto extends Elemento {
private Font fonte;
48
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 71

CasadoCódigo Capítulo2. InvasãoporSpaceInvaders
public Texto() {
fonte = new Font("Tahoma", Font.PLAIN, 16);
}
public Texto(Font fonte) {
this.fonte = fonte;
}
public void desenha(Graphics2D g, String texto) {
desenha(g, texto, getPx(), getPy());
}
public void desenha(Graphics2D g, String texto,
int px, int py) {
if (getCor() != null)
g.setColor(getCor());
g.setFont(fonte);
g.drawString(texto, px, py);
}
public Font getFonte() {
return fonte;
}
public void setFonte(Font fonte) {
this.fonte = fonte;
}
}
Esseérealmentenossoprimeirojogoealgunsdetalhestiveramdeficar
deforaparaquepudéssemoscodificarumaversãosimplesdesercriada,mas
funcional.Conformeveremosaolongodolivro,mesmoumjogosimplesde
serjogadonãonecessariamentequerdizersimplesparasercodificado.
49
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 72

2.5. Codificandoojogo CasadoCódigo
2.5 C odificando o jogo
Depoisdetudoisso,omelhorparatirarqualquerdúvidaépegarumaversão
ejogar,fazendoasmodifica çõesquequisereficandoàvontadeparacom-
partilharconoscoem: https://github.com/logicadojogo/fontes/tree/master/
Cap02.
Naseçãoaseguir,comentamosoqueachamosqueseriaimportantepara
ojogoeacabounãocabendonocapítulo.Enase ção2.5,deixamosumdesafio
paravocê,leitor. Paraasduasse ções,asrespostasouestãodistribuídasem
outroscapítulos,ouserãovistascommaiorprofundidadenocapítulo10.
Não fizemos aqui
• Barreirasparecidascomasdojogooriginal.
Melhore você mesmo
• Impedirojogadordesairdatela;
• Encerrarojogoquandootanqueperdertodasasvidas.
2.6 R esumo
Criarjogoséumexercíciomuitocriativoe,sevocêconseguirimaginarformas
dedarmaiscriatividadeaojogo,porfavor,ofa çaecompartilhe.Nossojogo
jácomeçadiretonaa çãoesabemosquenãoébemassimqueumbomjogo
devecome çar. Seaomenoseletivesse pause(pausa),masnemisso. Mas
nãosepreocupe,jáqueessessãodoisrecursosqueabordaremosnopróximo
capítulo.
50
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 73

Capítulo3
MeunomeéPong,PingPong
Naverdade,onomeésomentePong,oprimogênitodaAtariInc.,projetado
porAlAlcornelan çadoem1972.Foiumgrandesucesso.
Porserumjogosimplesdeserprogramado,vamosacrescentarmaisfun-
cionalidadeseaumentarnossabibliotecadecódigo.
Nestecapítulo,abordaremoscombaseemaspectosdojogooriginal:
• Interaçãocomtecladoemouse;
• Separarojogoemcenários;
• Menusimples;
• Movimentaçãodiagonal;
• Configuraçãodomododejogo.
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 74

3.1. Separandoateladocenário CasadoCódigo
Fig.3.1:Jogomodonormal
3.1 S eparando a tela do cenário
Em nosso jogo anterior, a mesma classe responsável por criar a janela (
JFrame),atela( JPanel)ecapturaraentradadojogadortambémcon-
trolavaofluxodojogo. Claramentepodemossepararessastarefasemduas
classesdistintas:umaqueconversediretamentecomosistemaoperacional,
eoutraquefiqueresponsávelpelodojogo.Alémdetermosumcódigomais
enxutoereaproveitável,ficamaisfácilmigrarojogoparaoutrasplataformas.
Éaiqueentranossaclasse CenarioPadraoparaincrementarnossa
caixadeferramentas.
package br.com.mvbos.lgj.base;
import java.awt.Graphics2D;
52
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 75

CasadoCódigo Capítulo3. MeunomeéPong,PingPong
public abstract class CenarioPadrao {
protected int altura, largura;
public CenarioPadrao(int largura, int altura) {
this.altura = altura;
this.largura = largura;
}
public abstract void carregar();
public abstract void descarregar();
public abstract void atualizar();
public abstract void desenhar(Graphics2D g);
}
Assim,podemosdividirnossosjogosemdiversoscenários,quenãone-
cessariamenteserãofasesdojogo,comoporexemplo,ateladeintrodu çãoou
ummenudeop ções.
Nestejogo,temosduasclassesqueextendemdaclasse CenarioPadrao,
InicioCenarioe JogoCenario.Aprimeiraéondeojogadorescolherá
omododejogo(normalouemcasa)eavelocidade(normal,rápidoelento).
Asegundaéojogopropriamentedito.
Nossaclasse Jogotrabalhandocomcenáriosficouassim:
...
private CenarioPadrao cenario;
...
public void iniciarJogo() {
long prxAtualizacao = 0;
while (true) {
if (System.currentTimeMillis() >= prxAtualizacao) {
g2d.setColor(Color.BLACK);
g2d.fillRect(0, 0, JANELA_LARGURA, JANELA_ALTURA);
53
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 76

3.1. Separandoateladocenário CasadoCódigo
...
if (cenario == null) {
g2d.setColor(Color.WHITE);
g2d.drawString("Carregando...", 20, 20);
} else {
cenario.atualizar();
cenario.desenhar(g2d);
}
tela.repaint();
prxAtualizacao = System.currentTimeMillis() + FPS;
}
}
}
Atrocaentreoscenáriosfuncionadaseguinteforma:seojogadorestiver
nateladeintrodu çãoepressionaratecla enterouespaço,trocamosparao
cenáriodojogo,masseestiverjogando,ojogoserápausado.Casopressione
ESCduranteojogo,voltamosparaocenáriodeintrodu ção.
...
public enum Tecla {
CIMA, BAIXO, ESQUERDA, DIREITA, BA, BB
}
public static boolean[] controleTecla =
new boolean[Tecla.values().length];
...
public static boolean pausado;
...
if (controleTecla[Tecla.BA.ordinal()]) {
// Pressionou espaço ou enter
if (cenario instanceof InicioCenario) {
cenario.descarregar();
cenario = new JogoCenario(tela.getWidth(),
tela.getHeight());
cenario.carregar();
54
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 77

CasadoCódigo Capítulo3. MeunomeéPong,PingPong
} else if (cenario instanceof JogoCenario) {
Jogo.pausado = !Jogo.pausado;
}
liberaTeclas();
} else if (controleTecla[Tecla.BB.ordinal()]) {
// Pressionou ESC
if (cenario instanceof JogoCenario) {
cenario.descarregar();
cenario = new InicioCenario(tela.getWidth(),
tela.getHeight());
cenario.carregar();
}
liberaTeclas();
}
Utilizamosooperador instanceofparasabermosemqualcenárioes-
tamose,antesdeocorreratroca,chamamosométodo descarregar,seja
paraliberarmemóriaouparasalvaralgumestadodojogo.
Porcomodidade,passamosalarguraealturadatelanoconstrutorda
classe.Mesmoquenossastelasnãosejamredimensionadas,utilizamosmui-
tasvezesovalordalarguraealturadatelaemnossoscenários.
Ométodo carregar,alémdecarregarojogo,éútilparaoscasosemque
querermosapenasreiniciá-lo,reposicionandotodososelementosnoponto
deorigem,oqueseriamaisrápidoquecriarumanovainstância.
Dica
Menusdevemserintuitivosefáceisdeusar. Logo,evitegrandese
complexosmenus,enãotenhareceiodeutilizaríconeselegendas.
Comovocêdeveterreparado,nãoestamosmaisusandonúmerosparaas
teclaspressionadas,poiscomo enum Tecla ficamaisfácilsaberqualtecla
foipressionada.Utilizamos BAe BB(BotãoAeB)emvezdonomedatecla
paraserindependentedevínculos,facilitandomudan ças.
55
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 78

3.1. Separandoateladocenário CasadoCódigo
Emnossoscenários,sóprecisamossaberse BAou BBforampressiona-
dos,semprecisarmossaberqualteclaestáligadaaestesbotões. Usamoso
métodoliberaTeclasquandoprecisamosgarantirquenãoexecutaremos
amesmaa çãomaisdeumavez.
public static void liberaTeclas() {
for (int i = 0; i < controleTecla.length; i++) {
controleTecla[i] = false;
}
}
Elefazoopostodométodo setaTecla,definindotodososvaloresde
controleTeclacomofalso. Porfim,nossojogotemdoisjogadores,um
controladopelotecladoeoutropelomouse,mas,diferentedoquejávimos
noexemplo InterativoMousenocapítulo1,aquiignoramososcliquese
pegamosapenasaposi çãodomousenoeixoY.
...
public static int mouseY;
...
tela.addMouseMotionListener(new MouseMotionListener() {
@Override
public void mouseMoved(MouseEvent e) {
mouseY = e.getY();
}
@Override
public void mouseDragged(MouseEvent e) {
}
});
...
Usamos mouseYparaarmazenaraposi çãodomouse,queéatualizada
todavezquea teladetectarsuamovimenta ção.
Nossaclasse InicioCenarioteráessevisual:
56
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 79

CasadoCódigo Capítulo3. MeunomeéPong,PingPong
Fig.3.2:Introdu çãodojogo
Temosdoismenus:oprimeirocomduasop çõeseosegundocomtrês.
Paraenfeitarocenáriointrodutório,inserimosaboladojogo.
...
private Bola bola;
private Menu menuModo;
private Menu menuVeloc;
@Override
public void carregar() {
bola = new Bola();
menuModo = new Menu("Modo");
menuModo.addOpcoes("Normal", "Em casa");
menuVeloc = new Menu("Vel.");
57
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 80

3.1. Separandoateladocenário CasadoCódigo
menuVeloc.addOpcoes("Normal", "Rápido", "Lento");
Util.centraliza(bola, largura, altura);
Util.centraliza(menuModo, largura, altura);
Util.centraliza(menuVeloc, largura, altura);
menuModo.setPy(menuModo.getPy() + 20);
menuVeloc.setPy(menuModo.getPy() + menuModo.getAltura());
bola.setAtivo(true);
menuModo.setSelecionado(true);
menuModo.setAtivo(true);
menuVeloc.setAtivo(true);
}
Nãosepreocupecomoobjeto Bolaagora,veremoscommaisdetalhes
quandofalarmosdojogoemsi,afinal,esteépraticamenteoastrodoPong.
Criamosdoisobjetos Menu,queveremosembreve,eadicionamosasrespec-
tivasopçõesparacadaum.
Depoisdecentralizarmosostrêsobjetos,apenasdistanciamososmenus,
deformaqueo menuModonãocolidacomabolaeo menuVelocnãocolida
como menuModo.Ométodo descarregartemumafun çãoimportante,
queépassarparaojogoasop çõesescolhidas.
@Override
public void descarregar() {
Jogo.velocidade = bola.getVel();
Jogo.modoNormal = menuModo.getOpcaoId() == 0;
}
Valenotarqueabolaqueficaquicandonateladeintrodu çãonãoserve
somentedeenfeite.Aoalteraraop çãodevelocidade,refletimosnabolaque
semovenavelocidadeescolhida,dandoaojogadorumaindica çãodequal
seráavelocidadedeladentrodojogo,porisso Jogo.velocidaderecebeo
valorde bola.getVel().
Asmudançasnomenusãoverificadasdentrodométodo atualizar:
@Override
public void atualizar() {
58
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 81

CasadoCódigo Capítulo3. MeunomeéPong,PingPong
if (Jogo.controleTecla[Jogo.Tecla.CIMA.ordinal()] ||
Jogo.controleTecla[Jogo.Tecla.BAIXO.ordinal()]) {
if (menuModo.isSelecionado()) {
menuModo.setSelecionado(false);
menuVeloc.setSelecionado(true);
} else {
menuModo.setSelecionado(true);
menuVeloc.setSelecionado(false);
}
Quandoojogadorpressionaparacimaouparabaixo,alternamosen-
treosmenus, eomenuqueestiverselecionadoserádesenhadocomsu-
blinhado. Agora,quandoelepressionaparaesquerdaoudireita,ométodo
trocaOpcaodaclasse Menufazamudan çaentreasop çãodefinidas,indo
paraaesquerda(seovalorpassadoforverdadeiro)ouparaadireita(sefor
falso),claroqueissosomenteseomenuemquestãoestiverselecionado.
} else if (Jogo.controleTecla[Jogo.Tecla.ESQUERDA.ordinal()]
|| Jogo.controleTecla[Jogo.Tecla.DIREITA.ordinal()]) {
boolean esqueda =
Jogo.controleTecla[Jogo.Tecla.ESQUERDA.ordinal()];
menuModo.trocaOpcao(esqueda);
menuVeloc.trocaOpcao(esqueda);
if (menuVeloc.getOpcaoId() == 0) {
bola.setVel(Bola.VEL_INICIAL);
} else if (menuVeloc.getOpcaoId() == 1) {
bola.setVel(Bola.VEL_INICIAL * 2);
} else {
bola.setVel(Bola.VEL_INICIAL / 2);
}
}
Jogo.liberaTeclas();
59
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 82

3.1. Separandoateladocenário CasadoCódigo
// Controle da bola
...
}
Dependendodaop çãopassadaparao menuVeloc,atualizamosavelo-
cidadedabola,sendoqueaop ção“Rápido”éodobrodavelocidadenormal,
e“Lento”émetadedessavelocidade. AclasseMenuencontra-senopacote
baseefazpartedanossacaixadeferramentas,servindoparaoutrosjogos.
public class Menu extends Texto {
private short idx;
private String rotulo;
private String[] opcoes;
private boolean selecionado;
public Menu(String rotulo) {
super();
this.rotulo = rotulo;
setLargura(120);
setAltura(20);
}
public void addOpcoes(String... opcao) {
opcoes = opcao;
}
Portrabalharprincipalmentecomescrita,nossaclasse Menuherdade
Texto,enãodiretamentedanossaclasse Elemento.Nométodoconstru-
tor,definimosumalarguraealturapadrãoe,nométodo desenha,concate-
namosorótulodomenueaúltimaop çãoselecionadaentreosinalde <e >.
Casoestejaselecionado,desenhamosumalinhaabaixodotexto.
@Override
public void desenha(Graphics2D g) {
if (opcoes == null)
return;
60
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 83

CasadoCódigo Capítulo3. MeunomeéPong,PingPong
g.setColor(getCor());
super.desenha(g, getRotulo() + ": <" + opcoes[idx] + ">",
getPx(), getPy() + getAltura());
if (selecionado)
g.drawLine(getPx(), getPy() + getAltura() + 5,
getPx() + getLargura(), getPy() + getAltura() + 5);
}
...
public void trocaOpcao(boolean esquerda) {
if (!isSelecionado() || !isAtivo())
return;
idx += esquerda ? -1 : 1;
if (idx < 0)
idx = (short) (opcoes.length - 1);
else if (idx == opcoes.length)
idx = 0;
}
}
Ométodoparanavegarentreasop ções( trocaOpcao)primeiroverifica
seomenuestáselecionadoeseéumelementoativo,paraentãonavegarpara
aesquerda.Decrementamos idxeincrementamosparairparaadireita.
Se,poracaso,o idxformenordoquezero(queéaprimeiraop ção),
posicionamosomenunaúltimaop ção;casoelepassedaúltimaop ção,posi-
cionamosnaprimeira.
Utilizamosumtipo shortparao idx,queocupamenosespa çoem
memóriaqueumtipo int,issofarádiferençaseestiverdesenvolvendojogos
paraplataformascompoucamemória.
61
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 84

3.2. Jogandoocódigo CasadoCódigo
Dica
Estamos concatenando os textos rótulo e opção do menu,
mas o Java nos fornece uma forma mais elegante com o método
String.format. Assim, podemos substituir o código anterior
pela chamada: String.format("%s: <%s>", getRotulo(),
opcoes[idx]), onde cada %s será substituído pelos parâmetros
seguintesnamesmaordememqueaparecem.
Usamos %spara String(texto), %dparainteirose %fparaponto
flutuante.
3.2 J ogando o código
Amaiorpartedalógicadojogoestáligadaàbola(nossaclasse Bola),que
temdequicareserrebatidaemdiferentesvelocidadeseângulos. Paraisso,
usamosdoisinteirosparacontrolaradire çãodabola,edoisflutuantespara
controlaravelocidade,ambosparaoseixosXeY,respectivamente.
Comisso,podemosterumabolaindorapidamenteparaaesquerda,mas
subindolentamente.Ouseja,comdire çõesevelocidadesdiferentesparacada
eixo,deixandoomovimentomaisnatural.
public class Bola extends Elemento {
public static final int VEL_INICIAL = 3;
private int dirX = -1;
private int dirY = -1;
private float velX;
private float velY;
public Bola() {
velX = velY = VEL_INICIAL;
setAltura(10);
setLargura(10);
setCor(Color.WHITE);
}
62
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 85

CasadoCódigo Capítulo3. MeunomeéPong,PingPong
...
@Override
public void setVel(int vel) {
velX = velY = vel;
}
@Override
public int getVel() {
return (int) velX;
}
public void incPx() {
incPx((int) velX * dirX);
}
public void incPy() {
incPy((int) velY * dirY);
}
public void inverteX() {
dirX *= -1;
}
public void inverteY() {
dirY *= -1;
}
}
Játrabalhamoscomdireçãonojogoanterior,aquiestamosapenasutili-
zandoamesmalógicanosdoiseixoscom dirXe dirY.Iniciamosnossa
bolacomavelocidade,largura,alturaecorpadrão.
Observequeométodo setVelatualizatanto velXquanto velY.Não
usamosoatributo veldaclasse Elementoparaevidenciarmelhordequal
eixoestamosmudandoavelocidade.
Eagora,semmaisdelongas,vamosànossaclasse JogoCenario,onde
doisjogadoresdeslizamnaverticalrebatendoumpontobrancoquevaifi-
candocadavezmaisrápido,atéqueumdeleserreeooutrofa çaponto.Co-
63
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 86

3.2. Jogandoocódigo CasadoCódigo
meçamosdeclarandoasseguintesvariáveis:
...
private float inc = 0.5f;
private Ponto pontoA, pontoB;
private Bola bola;
private Elemento esquerda;
private Elemento direita;
private boolean reiniciarJogada;
private final Texto textoPausa = new Texto(Ponto.fonte);
// Modo em casa
private int idx;
private Bola[] bolaArr = new Bola[0];
private Random rand;
...
Utilizamos incparaincrementaravelocidadedabolaquandoelaére-
batida.Usamosotipoflutuanteparaumaumentomaisgradual.Comopode
imaginar, pontoAe pontoBsãousadosparaexibirapontua çãodecada
jogador,quesãorepresentadospor: esquerdae direita.
Duranteapausadojogo,seráexibidootexto PAUSA,comamesmafonte
usadaparaexibirapontua ção;usamos textoPausaparaisso. Essejogo
temdoismodos:ummaisparecidocomooriginal,eoutronoqual,acada
rebatida,umanovabolasurgenocentrodatela,comtamanhoevelocidades
variadas,batizadode Em casa.Paraisso,sãousadasastrêsúltimasvariáveis.
...
public JogoCenario(int largura, int altura) {
super(largura, altura);
bola = new Bola();
esquerda = new Elemento();
direita = new Elemento();
pontoA = new Ponto();
pontoB = new Ponto();
}
...
64
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 87

CasadoCódigo Capítulo3. MeunomeéPong,PingPong
Iniciamososprincipaiselementosdojogonoconstrutordaclasse,dei-
xandoparaométodo carregarotrabalhodeconfigurá-los.
...
@Override
public void carregar() {
bola.setVel(Jogo.velocidade);
pontoA.setPx(largura / 2 - 120);
pontoA.setPy(Ponto.TAMANHO_FONTE);
pontoB.setPx(largura / 2 + 120 - Ponto.TAMANHO_FONTE / 2);
pontoB.setPy(Ponto.TAMANHO_FONTE);
esquerda.setVel(5);
esquerda.setAltura(70);
esquerda.setLargura(5);
esquerda.setCor(Color.WHITE);
direita.setVel(5);
direita.setAltura(70);
direita.setLargura(5);
direita.setCor(Color.WHITE);
direita.setPx(largura - direita.getLargura());
Util.centraliza(bola, largura, altura);
Util.centraliza(direita, 0, altura);
Util.centraliza(esquerda, 0, altura);
bola.setAtivo(true);
direita.setAtivo(true);
esquerda.setAtivo(true);
...
Abolainicialmenteetodavezqueajogadaéreiniciadarecebeavelo-
cidadedefinidanaintrodu çãodojogo. Osdoisobjetosdaclasse Ponto,
queestendemaclasse Texto,sãoposicionadospróximosdalinhacentralde
formabemsimples,variandodeacordocomotamanhodafonte.
Valeressaltarque,paraposicionarcorretamenteapontua ção,alémdo
65
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 88

3.2. Jogandoocódigo CasadoCódigo
tamanhodafonte,teríamosdeconsideraraquantidadedecaractereserecal-
cularaposi çãoconformeelessãoalterados.Semrecalcularmos,conformea
pontuaçãodojogadordaesquerdaforaumentando,elainvadiráocampodo
jogadordadireita,issoacimadosmilpontos.
Aindanométodo carregar,seomododejogonãoforomodonormal,
iniciaremoso bolaArrcomtamanhode30e,então,criamos30objetos
(bolas),variandodire ção,velocidade,larguraealtura.
...
if (!Jogo.modoNormal) {
rand = new Random();
bolaArr = new Bola[30];
for (int i = 0; i < bolaArr.length; i++) {
int v = rand.nextInt(3) + 1;
bolaArr[i] = new Bola();
bolaArr[i].setDirX(i % 2 == 0 ? -1 : 1);
bolaArr[i].setVel(Bola.VEL_INICIAL * v);
bolaArr[i].setAltura(bola.getAltura() * v);
bolaArr[i].setLargura(bola.getLargura() * v);
Util.centraliza(bolaArr[i], largura, altura);
}
}
}
Ovalorde vpodeserde1a3. Assim,seovalorfor1,seráumabola
padrão,massefor3,serátrêsvezesmaisrápidaemaior.
66
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 89

CasadoCódigo Capítulo3. MeunomeéPong,PingPong
Fig.3.3:Modofeitoemcasacompausa
Dica
Seavelocidadedabolaforsuperioràlarguradaraquete,achancede
elanãoserpegapelonossodetectordecolisão,atravessandoojogador,
égrande.
Ométodo atualizaéojuizdessapartida:
@Override
public void atualizar() {
if (Jogo.pausado)
return;
bola.incPx();
67
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 90

3.2. Jogandoocódigo CasadoCódigo
bola.incPy();
if (Jogo.controleTecla[Jogo.Tecla.CIMA.ordinal()]) {
esquerda.incPy(esquerda.getVel() * -1);
} else if (Jogo.controleTecla[Jogo.Tecla.BAIXO.ordinal()]) {
esquerda.incPy(esquerda.getVel());
}
if (direita.getPy() + direita.getAltura() / 2 >
Jogo.mouseY + direita.getVel())
direita.incPy(direita.getVel() * -1);
else if (direita.getPy() + direita.getAltura() / 2 <
Jogo.mouseY - direita.getVel())
direita.incPy(direita.getVel());
validaPosicao(esquerda);
validaPosicao(direita);
if (reiniciarJogada) {
reiniciarJogada = false;
bola.inverteX();
bola.setVel(Jogo.velocidade);
Util.centraliza(bola, largura, altura);
} else {
reiniciarJogada = validaColisao(bola);
}
...
}
Antes de qualquer atualização do cenário ser feita, verificamos se o
jogoestápausado. Casoesteja,nadamaisseráatualizadoatéquevalorde
Jogo.pausadomudeparafalso.
Amovimentaçãodojogadordadireitausaaposi çãodaraquetenoeixo
Ymaisametadedaalturadelaparaposicioná-lacentralizadaemrela çãoao
ponteirodomouse.Naverifica ção,somamosousubtraímosavelocidadeda
68
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 91

CasadoCódigo Capítulo3. MeunomeéPong,PingPong
raqueteparaaumentarolimitedoposicionamento,evitandoqueoobjeto
fiquetrepidandonatela.
Ométodo validaPosicaoapenasnãodeixaqueosobjetosacabemfora
datelanoeixoY.Quandoreiniciamosajogada,invertemosadire çãodabola,
então,quemmarcarpontoteráquedefender.Tambémvoltamosavelocidade
eposi çãoinicialdela. Ométodo validaColisaotambéméresponsável
pelapontuação:
private boolean validaColisao(Bola b) {
boolean saiu = false;
if (Util.colide(esquerda, b)) {
rebate(esquerda, b);
} else if (Util.colide(direita, b)) {
rebate(direita, b);
} else if (b.getPx() < 0 ||
b.getPx() + b.getLargura() > largura) {
saiu = true;
if (b.getPx() < 0)
pontoB.add();
else
pontoA.add();
} else if (b.getPy() <= 0 ||
b.getPy() + b.getAltura() >= altura) {
// Colisão no topo ou base da tela
b.inverteY();
}
return saiu;
}
Seabolacolidircomalgumadasraquetes,elaserárebatida,masseela
agilmenteescapardelas,conseguindosairdatelapelaslaterais,ojogadordo
69
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 92

3.2. Jogandoocódigo CasadoCódigo
ladoopostodeondeabolasaiumarcaponto.Porfim,verificamosseabola
colidiucomotopoouabasedatela,então,invertemossuadire çãonoeixoY.
OmétodopararebaterabolapoderiasimplesmenteinverteroeixoX,
maseleéumpoucomaissofisticadoqueisso. Quandoumadasraquetes
colidecomabola,temoscincotiposdiferentesderebatidas:paraumacolisão
acimadocentro,nocentroeabaixodocentro,eparacolisãocomasquinas
daraquete.
Fig.3.4:Pontosdecolisãoraquete
Paraisso,dividimosaraqueteemtrêspartes(quejuntocomaquinasupe-
rioreinferiorsomarãocincovaria ções),everificamosemqualdessaspartes
abolabateu:
public void rebate(Elemento raquete, Bola bola) {
float vx = bola.getVelX();
float vy = bola.getVelY();
if (bola.getPy() <
raquete.getPy() + raquete.getAltura() / 3) {
bola.setDirY(-1);
vx += inc;
vy += inc;
if (bola.getPy() < raquete.getPy()) {
vy += inc;
}
} else if (bola.getPy() > raquete.getPy() +
70
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 93

CasadoCódigo Capítulo3. MeunomeéPong,PingPong
raquete.getAltura() - raquete.getAltura() / 3) {
bola.setDirY(1);
vx += inc;
vy += inc;
if (bola.getPy() + bola.getAltura() >
raquete.getPy() + raquete.getAltura()) {
vy += inc;
}
} else {
vx += inc;
vy = 1;
}
bola.inverteX();
bola.incVel(vx, vy);
if (bolaArr.length > 0) {
if (idx < bolaArr.length) {
bolaArr[idx++].setAtivo(true);
} else {
idx = 0;
}
}
}
Seabolabaternoter çodecima,elaérebatidaparacima(passamos-1
para dirY),eadicionamosvelocidadeemambososeixos. SeoeixoYda
bolaformenorqueodaraquete(quina),incrementamosumpoucomaisa
velocidadenoeixoY.
Seacolisãofornoter çodebaixo,faremosalgosimilar.Casosejanoter ço
central,incrementamos velXedeixamos velYcom1,fazendoabolavoltar
quaseemlinhareta. Estamosusandoumtipoflutuanteparatermosmais
opçõesdevelocidade.
Depoisdeinvertemosadire çãonoeixoX( bola.inverteX)epassar-
71
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 94

3.2. Jogandoocódigo CasadoCódigo
mosasnovasvelocidadesparaabola( bola.incVel(vx, vy)),verifica-
mosseativamosumanovabola,sendoque bolaArr.lengthvaisermaior
quezerodependendodomododejogo.
Nãousamosoângulodabolacomobasedecálculoparaasrebatidascomo
éfeitonojogooriginal,resultandoemmenosvaria ção.Masnãosepreocupe,
temosumjogoespecíficosóparaabordarânguloserota ções(consegueima-
ginarqualé?).Então,vocêpoderádeixarojogomaispróximodooriginalse
quiser.
Ométodoparadesenharnossoselementosficouassim:
@Override
public void desenhar(Graphics2D g) {
// Desenha linha de fundo
for (int i = 0; i < altura; i += 20) {
g.setColor(Color.WHITE);
g.drawRect(largura / 2 - 2, i, 4, 10);
}
pontoA.desenha(g);
pontoB.desenha(g);
// depurarColisao(esquerda, g);
// depurarColisao(direita, g);
bola.desenha(g);
for (Bola b : bolaArr) {
b.desenha(g);
}
esquerda.desenha(g);
direita.desenha(g);
if (Jogo.pausado)
textoPausa.desenha(g, "PAUSA",
largura / 2 - Ponto.TAMANHO_FONTE,
altura / 2);
}
72
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 95

CasadoCódigo Capítulo3. MeunomeéPong,PingPong
Nada que já não tenhamos visto antes. Você pode usar o método
depurarColisaoparavisualizaradivisãonaraquete. Porfim,masnão
menosimportante,nossaclasse Ponto:
...
public class Ponto extends Texto {
public static final int TAMANHO_FONTE = 60;
public static final Font fonte =
new Font("Consolas", Font.PLAIN, TAMANHO_FONTE);
private short ponto;
public Ponto() {
super.setFonte(fonte);
}
public short getPonto() {
return ponto;
}
public void setPonto(short ponto) {
this.ponto = ponto;
}
public void add() {
ponto++;
}
@Override
public void desenha(Graphics2D g) {
super.desenha(g, Short.toString(ponto),
getPx(), getPy());
}
}
Utilizamosnovamenteumtipo short,dessaveznospontos,parapou-
parmemória,jáqueserádifícilumjogadorpassardamarcade32.767pontos.
73
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 96

3.3. Codificandoojogo CasadoCódigo
Pouparmemóriaéumacoisaaseteremmentequandoseprogramajogos
(ouqualquersistema).Vocêpodepensarqueojogoésimplesdemaisouque
oscomputadoresdehojesãopoderosososuficienteparanãoterdesepreo-
cuparcomisso,massempreexisteapossibilidadedeportarseujogoparaum
celular(enemdigosmartphone),ouumdispositivocommenosmemória.
Masentãoqualomotivodenãoutilizarmos shortemquasetodaparte
donossocódigo?Paranãotermosdefazerconversãotodahora,jáqueamai-
oriadosmétodosdoJavaqueusamosemnossosjogostrabalhacominteiros
ouflutuantes.
3.3 C odificando o jogo
SevocêpensouemAsteroidscomoojogoemquefalaremosdeângulos(ca-
pítulo8),acertou. Nossaversãodojogosemprecisarcalcularângulosestá
em:https://github.com/logicadojogo/fontes/tree/master/Cap03.
Lávocêpodeconferircommaisdetalhesasdiversasaltera çõesquefize-
mosnaclasse Jogo.javaparatrabalharmoscomcenários,alémdasno-
vasclasses: Bola.java, InicioCenario.java, JogoCenario.javae
Ponto.java.
Temosdoisjogose,sevocêunirSpaceInvaderscomPong,poderácriar
ojogoBreakout,idealizadoporNolanBushnelleSteveBristow,lan çadopela
Atariem1976.
Não fizemos aqui
• Calcularoângulodabolanarebatida;
• Exibirasúltimaspontuaçõesnocenáriodeintrodu çãodojogo.
Melhore você mesmo
• Quetalummododejogoseu?
74
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 97

CasadoCódigo Capítulo3. MeunomeéPong,PingPong
3.4 R esumo
Temosdoiscenáriosaqui:umparaojogadorescolheromodoevelocidade
dojogo,eoutroemqueojogoacontece.Poderíamossepararessesdoiscená-
rioscomumoumais ifs,entretanto,issodeixarianossocódigobagun çado,
dandotrabalhoparamanuten çãoedetec çãodeerros. Alémdomais,tería-
mosobjetosquesóprecisariamexistirnocenáriodeintrodu çãomisturados
comobjetosdocenáriodojogo.
Outropontoseriaacria çãodenovoscenários,porexemplo,umjogo
comooSonic2,noqualtemosateladeintrodu ção,teladeop ções,telado
jogoeateladebônusquesecomportamdemaneirasdiferentes.
EmboranãoestejamoscriandonadaparecidocomosjogosdoSonic(e
eunãosaibaexatamentecomoelefoiprojetado),separaremcenários(não
merefiroafases)emumalinguagemOrientadaaObjetoéumaabordagem
vantajosa.
Nossaclasse CenarioPadraoéabstrataparaquesejaimplementada
porumcenáriodeverdade. Enossaclasseprincipal( Jogo),aotratardos
cenários,sepreocupabasicamenteemavisaraocenárioquandoéhorade
atualizare desenharseuselementosefazeratrocadecenário,cha-
mandoosmétodos descarregar,sejáestivercomumcenárioemexe-
cução,e carregar,casonãoesteja.Apausaimplementadaésimplesmente
parardeatualizaroselementosecontinuarpintandoatela.
Autilizaçãodeconstantesparacontrolarasteclaspressionadasbeneficia
amudançadeteclas/botõesdojogo. Porexemplo,seemvezdeusar seta
para cimapassássemosautilizar W,atrocaseriafeitasomentenométodo
setaTecla.
Nocenárioinicial,aopressionarparacimaouparabaixo,éfeitaatroca
desele çãoentreosmenus. Aopressionaresquerdaoudireita,omenuque
estiverselecionadovaiparaapróximaop ção.
Oquevaledestacarparaocenáriodojogo( JogoCenario)sãoasmo-
dificaçõesquefizemosparaomodo Em casa.Declaramosvariáveis,massó
criamosainstânciacasonãosejao modo normal,efazemosissoquandoo
jogoécarregado,enãoemtempodeexecu ção.
Alocamostodaamemóriaqueprecisamosegerenciamososelementos
ativandoedesativando-os,semquesejamcriadasnovasinstâncias.Avanta-
75
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 98

3.4. Resumo CasadoCódigo
gemdestaabordageméaperformance,emboranãosejaumadiferen çanotá-
velparaestejogo.Masficacomodica.
76
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 99

Capítulo4
Jogodacobrinha
NemBlockade,desenvolvidopelaGremlinem1976,nemSurround,desen-
volvidopelaAtariem1977.Jogodacobrinhaeracomoeuchamavaaversão
quevinhacomoQBasic(Nibbles).
Foiaprimeiravezquetivecontatocomocódigo-fontedeumjogoepude
modificá-loparacriaroutrosníveis.Então,nãofoicasualescolheressejogo
parafalardesseassunto;afinal,quemnuncajogouessejogoemumcelular
antigo,nafiladobancooumesmonobanheiro?
Veremosnestecapítulo:
• Interaçãocomteclado;
• Criaçãodeníveis/fases/ levels.
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 100

4.1. Níveis:aquiloquevocêfazparareaproveitarocenário CasadoCódigo
Fig.4.1:Jogodacobrinha
4.1 N íveis: aquilo que você faz para reaprovei-
tar o cenário
Nocapítuloanterior,dividimosnossocódigoparatermosumaclasselidando
comosistemaoperacionaleoutraparacuidardalógicadonossojogo,oce-
nário. Imaginandoumjogonoestilo Super Mario Bros. 3,definitivamente
nãoprecisamosdeumcenárionovoparacadafasedojogo,jáquemuitas
78
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 101

CasadoCódigo Capítulo4. Jogodacobrinha
dasmecânicas,comocorrer,pularecomercogumelos,serãoreutilizadasem
outrasfases.
Faremosissonestecapítulo,usaremosnossocenáriodeformaqueelete-
nhaoutrosníveis,reaproveitandoamecânicadojogo.
Fig.4.2:Códigodafase
Nafigura4.2,temosocódigoquerepresentaafasee,nafigura4.3,te-
mosoresultadodessafasenocenário.Sãoapenasduaslinhasverticaisque
formamos,utilizandozeroseespa çoembrancoparaasáreasvazias.
79
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 102

4.1. Níveis:aquiloquevocêfazparareaproveitarocenário CasadoCódigo
Fig.4.3:Fase
Algunsjogostrabalhamcomníveisdeformaintrínsecanocódigo,outros
nemtanto,eamaioriautilizaarquivosindependentes. Amaioriatambém
usaferramentasàparteparacria çãoeedi çãodeníveis( Level Editor),àsvezes
daprópriaempresa,outras,deterceiros. Ainda,algumasdesenvolvedoras
distribuemessasferramentasparaqueojogadorpossaexpandirouniverso
dojogo.
Emnossocaso, separamosnossocódigocontendoosníveisnaclasse
Nivel,eutilizamosumarraytridimensionalestáticodotipo char(quedei-
80
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 103

CasadoCódigo Capítulo4. Jogodacobrinha
xamospré-formatadoparafacilitaraedi ção).
Fig.4.4:Umjogo,trêsfases
Masnãosepreocupe,continuamostrabalhandocomarraybidimensional
(18por18):
...
81
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 104

4.1. Níveis:aquiloquevocêfazparareaproveitarocenário CasadoCódigo
char[][] nivelSelecionado = Nivel.niveis[Jogo.nivel];
nivel = new Elemento[nivelSelecionado.length * 2];
for (int linha = 0; linha < nivelSelecionado.length; linha++) {
for (int coluna = 1; coluna < nivelSelecionado[0].length;
coluna++) {
if (nivelSelecionado[linha][coluna] != ' ') {
Elemento e = new Elemento();
e.setAtivo(true);
e.setCor(Color.LIGHT_GRAY);
e.setPx(_LARG * coluna);
e.setPy(_LARG * linha);
e.setAltura(_LARG);
e.setLargura(_LARG);
nivel[contadorNivel++] = e;
}
}
}
...
Avariável Jogo.nivelrecebeovalordonívelqueselecionamosno
cenáriointrodutóriodojogo(similaraojogodocapítuloanterior).Logo,ob-
temosumarraybidimensionalrepresentandoaslinhasecolunasdocenário
quedevemserpreenchidas,nestecaso,osvaloresdiferentesdeumespa çoem
branco.
Cadaespa çopreenchidoserárepresentadoporum Elementonacor
cinza,tendoasmesmasdimensõesdosoutrosobjetosdojogo.Então,acaba-
mosutilizandoumarray(destavez,unidimensional),tendocomotamanho
odobrodelinhasdonívelselecionado(nestecaso,36),jáqueosníveisde
exemploquecriamosnãoprecisamdemaisespa çoqueisso.
Observeque,devidoaofatodenossaserpentecome çarnalinha0ecoluna
0,ignoramosacolunainicial,come çandoa colunacomovalor1. Multi-
plicando _LARGpela coluna,temosaposi çãonoeixoX,e _LARGpela
82
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 105

CasadoCódigo Capítulo4. Jogodacobrinha
linha,aposi çãodoelementonoeixoY.
Dica
Usenúmerosouletrasdiferentesparacriarblocosdecoresdiferentes.
AvariávelcontadorNiveléusadaparapercorrermosoarraydeacordo
comonúmerodeelementos,enãopelocomprimento,umavezqueocom-
primentosempreserámaiorouigualaocontador.Sabendoquenossosblocos
nãopodemocuparatelainteira(poisaserpentenãoteriacomosemover),
umaformamelhorseriacriaroarraycomotamanhoigualàquantidadede
blocosdefinidanosníveis.
Umaformanãotãoboaseriapercorreroarrayinteiro–queparaum
cenáriomaior,teriabemmaisque36posi ções–,semutilizarocontador.Fi-
camosnomeiotermo,ganhandopoucaperformance,queémelhorquene-
nhuma.
Tamanho da tela versus tamanho dos níveis
Nossojogorodaemumajanelarelativamentepequena,issoporqueota-
manhodatelaeaquantidadedelinhasecolunasdosníveisquecriamosestão
ligadosaotamanhodosnossoselementosnojogo.
Porexemplo,asdimensõesdanossatelasão450px,enossasfasestêm
18linhasecolunas. Dividindo450por18,nóstemosumespa çamentode
25pixelsparanossoselementos. Seaumentarmosanossatela,mantendoo
mesmonúmerodelinhasecolunas,nossoselementosquecompõemosní-
veisdocenárioterãodeocuparumespa çomaiorparaseremposicionados
corretamente.Issoquerdizerquenãonecessariamenteteremosmaisespa ço.
Fixamosotamanhoem18linhasecolunasparafacilitaraedi çãosem
precisarmosdeumeditordelevels.Mesmoassim,játemostrabalho,eeusei
quevocêmalpodeesperarpelocapítulo6,ondetrabalhamoscom31linhase
28colunas.
Oselementospoderiamterumtamanhomenoroumaiorque25pixels,
83
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 106

4.1. Níveis:aquiloquevocêfazparareaproveitarocenário CasadoCódigo
masocupamosotamanhotodoparanãonospreocuparmosemcentralizaro
elementoparaposicioná-locorretamentenatela.
Noscapítulosanteriores,apenasnospreocupávamoscomotamanhoda
janela( JFrame),masnestejogo,otamanhodatela( JPanel)éoqueim-
porta,eelanãopodeperderespa çoparabordas. Assim,fizemosalgumas
modificações,eagoraacria çãodanossatelaficouassim:
...
tela = new JPanel() {
private static final long serialVersionUID = 1L;
@Override
public void paintComponent(Graphics g) {
g.drawImage(buffer, 0, 0, null);
}
@Override
public Dimension getPreferredSize() {
return new Dimension(JANELA_LARGURA, JANELA_ALTURA);
}
@Override
public Dimension getMinimumSize() {
return getPreferredSize();
}
};
getContentPane().add(tela);
setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
setResizable(false);
pack();
...
Em vez de chamarmos o métodosetSize(JANELA_LARGURA,
JANELA_ALTURA) do JFrame, sobrescrevemos os métodos
getPreferredSize() e getMinimumSize() do JPanel e cha-
mamosométodo pack(),quebasicamentedizparaajanelaqueoespa ço
dequeprecisamosédeacordocomotamanhodoselementosqueestãonela,
84
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 107

CasadoCódigo Capítulo4. Jogodacobrinha
garantindoquenossatelateráoespa çoqueelamerece.
Dica
Parasaberdequantaslinhasecolunasvocêprecisabaseadonota-
manhodatela,dividaoseutamanhopelotamanhoqueoelementovai
ocuparnela.
Paraumatelade650pxdelargura,emqueoselementosocuparão
25pxdelargura,porexemplo,precisamosde26colunas(650/25=26).
4.2 J ogando o código
Estevaiseroprimeirojogoemquerealmenteteremosinício,meioefim.
Ojogadorvaijogaratéperder,colidindocomocenárioouelemesmo;ou
ganhar,comendotodasasfrutasdatela.
Começamospelasprincipaisvariáveisdojogo,quesão:
enum Estado {
JOGANDO, GANHOU, PERDEU
}
private static final int _LARG = 25;
private static final int RASTRO_INICIAL = 5;
...
private int contadorRastro = RASTRO_INICIAL;
Nosso enum Estado éusadoparacontrolarofluxodojogo,queco-
meçanoestadojogando,noqualojogadorpodecontrolaraserpente;caso
contrário,umamensageméexibidaavisandoseeleganhououperdeu.
Paranãoparecerestranha,nossaserpentecome çainicialmentecom5ras-
tros,eutilizamosumcontador( contadorRastro)paracontrolaraadi ção
derastrosnojogo.
private Elemento fruta;
private Elemento serpente;
private Elemento[] nivel;
85
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 108

4.2. Jogandoocódigo CasadoCódigo
private Elemento[] rastros;
...
// Frutas para finalizar o level
private int dificuldade = 10;
Temosapenasumobjeto frutanojogo,queéreposicionadoaocolidir
comoobjeto serpente.Sendoquetemosnenhumoumaiselementosque
compõemoníveldocenário.Aquantidadederastrosqueojogadorprecisa
ter(frutasqueeledevecomer)écontroladapelavariável dificuldade.
Nossométodo carregar(),semaslinhasdecódigoparacarregaro
nível,quejávimosanteriormente,ficouassim:
...
// define direção inicial
dy = 1;
rastros = new Elemento[dificuldade + RASTRO_INICIAL];
fruta = new Elemento(0, 0, _LARG, _LARG);
fruta.setCor(Color.RED);
serpente = new Elemento(0, 0, _LARG, _LARG);
serpente.setAtivo(true);
serpente.setCor(Color.YELLOW);
serpente.setVel(Jogo.velocidade);
for (int i = 0; i < rastros.length; i++) {
rastros[i] = new Elemento(serpente.getPx(), serpente.getPy(),
_LARG, _LARG);
rastros[i].setCor(Color.GREEN);
rastros[i].setAtivo(true);
}
...
Amovimentaçãodaserpentetempontosimportantesqueocorremno
método atualizar().Primeiro,elanãosemovecontinuamente,massim
dentrodeumintervalo(controladopelavariável temporizador),eeste
podesermaioroumenordeacordocomavelocidadequeojogadorescolher
paraojogo.
86
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 109

CasadoCódigo Capítulo4. Jogodacobrinha
Segundo,aquantidadedepixelsutilizadosnamovimenta çãoéreferente
àlargura/alturapadrão,queusamosparadefinirotamanhodetodososele-
mentos.Assim,ojogadortemmaiorcontrolenasmanobras.
Oterceiropontoéque,todavezqueoprimeiroblocosemove(objeto
serpente),todoocorposeguejunto(objeto rastros),eelaestásempre
indoparaalgumadire çãodatela.
...
if (temporizador >= 20) {
temporizador = 0;
moveu = false;
int x = serpente.getPx();
int y = serpente.getPy();
serpente.setPx(serpente.getPx() + _LARG * dx);
serpente.setPy(serpente.getPy() + _LARG * dy);
...
for (int i = 0; i < contadorRastro; i++) {
Elemento rastro = rastros[i];
int tx = rastro.getPx();
int ty = rastro.getPy();
rastro.setPx(x);
rastro.setPy(y);
x = tx;
y = ty;
}
} else {
temporizador += serpente.getVel();
}
Paraentenderalógicadamovimenta çãodaserpente,bastapensarem
umafilaindiana,quandooprimeiroelementodafilasemove,osegundo
87
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 110

4.2. Jogandoocódigo CasadoCódigo
ocupaaposi çãoanteriordoprimeiro,oterceirodosegundo,eassimsuces-
sivamente. Emnossocódigo,primeiramente,pegamosaposi çãoatualdo
primeirobloco(cabe çadaserpente)esalvamosnasvariáveis xe y.Depois,
movemosacabe çaparaadire çãoseguinte. Percorremostodoorastro,fa-
zendoomesmoprocesso,guardandoaposi çãoatual(em txe ty),depois
movendoparaaposi çãoseguinte,atéosrastrosacabarem.
Aindafalandodamovimenta çãodaserpente,quandoelaestásemovendo
navertical,elasópodevirarnahorizontale,aosemovernavertical,virarna
horizontal.Assim,evitamosqueojogadordê“ré”ecolidacomorastro.
if (!moveu) {
if (dy != 0) {
if (Jogo.controleTecla[Jogo.Tecla.ESQUERDA.ordinal()]) {
dx = -1;
} elseif (
Jogo.controleTecla[Jogo.Tecla.DIREITA.ordinal()]) {
dx = 1;
}
if (dx != 0) {
dy = 0;
moveu = true;
}
} else if (dx != 0) {
if (Jogo.controleTecla[Jogo.Tecla.CIMA.ordinal()]) {
dy = -1;
} else if (
Jogo.controleTecla[Jogo.Tecla.BAIXO.ordinal()]) {
dy = 1;
}
if (dy != 0) {
dx = 0;
moveu = true;
}
}
88
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 111

CasadoCódigo Capítulo4. Jogodacobrinha
}
Utilizamos dxe dyparacontrolaradire çãodaserpente,eessasvariáveis
podemterovalor 0(semdireção), -1(paraaesquerdaouparacima)e 1
(paraadireitaouparabaixo).Massempreque dxfordiferentedezero, dy
seráigualazero,evice-versa.
Seojogadornãotiverfeitonenhummovimento( moveuigualafalso),
verificamosseaserpenteestásemovendonavertical( dydiferentedezero).
Entãoverificamosseomovimentodojogadorfoiparaaesquerdaoudireita,
atualizando dx.Tendoummovimentoválido,zeramos dyemarcamosque
omovimentofoirealizado.Omesmoocorreparaaverifica çãonahorizontal,
comsuasrespectivasdire ções,atualizando dy.
Duranteojogo,verificamosseacabe çadaserpentesaiudatela,seela
colidiucomalgumelementodocenárioousecolidiucomoprópriorastro.
Seissoocorrer,inativamosaserpenteparaignorarasoutrasvalida ções,eal-
teramosoestadodojogoparainformaraojogadorqueeleperdeu.
if (Util.saiu(serpente, largura, altura)) {
serpente.setAtivo(false);
estado = Estado.PERDEU;
} else {
// colisão com cenário
for (int i = 0; i < contadorNivel; i++) {
if (Util.colide(serpente, nivel[i])) {
serpente.setAtivo(false);
estado = Estado.PERDEU;
break;
}
}
// colisão com o rastro
for (int i = 0; i < contadorRastro; i++) {
if (Util.colide(serpente, rastros[i])) {
serpente.setAtivo(false);
estado = Estado.PERDEU;
break;
}
89
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 112

4.2. Jogandoocódigo CasadoCódigo
}
}
Masnemtudoéderrota.Seaserpentecolidircomoelemento fruta,
voltamoso temporizador(parasimularumapequenapausa),aumenta-
mosacontagemderastros( contadorRastro),einativamosoelemento
frutaparaquereapare çaemoutrolugar.Jáseacontagemderastroschegar
aonúmeromáximo,ojogadorganhaojogo.
if (Util.colide(fruta, serpente)) {
// Adiciona uma pausa
temporizador = -10;
contadorRastro++;
fruta.setAtivo(false);
if (contadorRastro == rastros.length) {
serpente.setAtivo(false);
estado = Estado.GANHOU;
}
}
Adicionadadeformarandômica,afrutaéposicionadanatela,dividindo
alarguraealturada telapelalarguraealturadoelemento.Paraumatela
dotamanhode450px,comlarguraealturapadrãode25px( _LARG),temos
umtotalde18posi çõespossíveis. Dessaformaestamostrabalhandocoma
telacomoseelafosseumarray.
// Adicionando frutas
if (estado == Estado.JOGANDO && !fruta.isAtivo()) {
int x = rand.nextInt(largura / _LARG);
int y = rand.nextInt(altura / _LARG);
fruta.setPx(x * _LARG);
fruta.setPy(y * _LARG);
fruta.setAtivo(true);
// colisão com a serpente
if (Util.colide(fruta, serpente)) {
fruta.setAtivo(false);
90
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 113

CasadoCódigo Capítulo4. Jogodacobrinha
return;
}
// colisão com rastro
for (int i = 0; i < contadorRastro; i++) {
if (Util.colide(fruta, rastros[i])) {
fruta.setAtivo(false);
return;
}
}
// colisão com cenário
for (int i = 0; i < contadorNivel; i++) {
if (Util.colide(fruta, nivel[i])) {
fruta.setAtivo(false);
return;
}
}
}
Se,poracaso,afrutanahoraemqueforadicionadacolidircomalgum
elemento,elaserádesativadaetentamosnopróximoloop,quandoométodo
atualizar()seráchamadonovamente.Depoisdetudoquefoicarregado
eatualizado,sónosfaltadesenhar:
@Override
public void desenhar(Graphics2D g) {
if (fruta.isAtivo()) {
fruta.desenha(g);
}
for(Elemento e : nivel){
if(e == null)
break;
e.desenha(g);
}
91
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 114

4.3. Codificandoojogo CasadoCódigo
for (int i = 0; i < contadorRastro; i++) {
rastros[i].desenha(g);
}
serpente.desenha(g);
A novidade aqui é que percorremos o arraynivel sem utilizar o
contadorNivel,parandoquandoencontramosumelementonulo.
texto.desenha(g,
String.valueOf(rastros.length - contadorRastro),
largura - 35, altura);
if (estado != Estado.JOGANDO) {
if (estado == Estado.GANHOU)
texto.desenha(g, "Ganhou!", 180, 180);
else
texto.desenha(g, "Vixe!", 180, 180);
}
if (Jogo.pausado)
Jogo.textoPausa.desenha(g, "PAUSA", largura / 2 -
Jogo.textoPausa.getFonte().getSize(),
altura / 2);
}
Utilizamosoobjeto texto(danossaclasse Textoqueestendede
Elemento)paramostrarnatelaquantasfrutasfaltamparaojogadorganhar
ojogo. Seeleganharouperder,usamosométodo desenhaparaexibira
mensagemdevitóriaouderrotae,enquantoojogoestiverpausado,exibimos
amensagemdepausanatela.
4.3 C odificando o jogo
Esperandoquevocêtraganovosníveis,nossocódigoencontra-seemhttps:
//github.com/logicadojogo/fontes/tree/master/Cap04.
92
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 115

CasadoCódigo Capítulo4. Jogodacobrinha
Gostariadetercolocadoocódigocompletodaclasse Nivel.javanas
páginasdestelivro,maselesperderiamaformata çãoealegibilidade.
Nossacaixadeferramentas(códigobase)nãosofreualtera ção,emodifi-
camosnossaclasse Jogo.javaparaqueajanelaseajusteàlarguradatela.
Parafinalizar,comosconhecimentosadquiridosaqui,jáconseguimos
criarasbarreirasquefaltaramnanossaversãodoSpaceInvadernocapítulo
2.
Não fizemos aqui
• Irparaopróximonívelquandoojogadorganhar(atécompletartodos
eganharojogo);
• Definiraposiçãoinicialdaserpentedeacordocomafase.
Melhore você mesmo
• Façacenárioscommaiscores;
• Crieseupróprionível.
4.4 R esumo
Vimoscomoasfasesdeumjogopodemsercriadasecomoocenáriopodeser
construídoparatrabalharcomelas.Masnãoprecisamosnoslimitarapenas
àconstruçãodeníveis,elementosdojogopodemsercriadosdessaforma,
comoveremosnopróximocapítulo.
Mesmoutilizandopoucaslinhasecolunas,adiversidadedelevelsque
conseguimoscriarégrande.Esteéumjogoondeostamanhos(tela,nívele
elemento)fazemdiferen ça. Estamosutilizandovaloresfixos(tela450x450,
nível18x18eelemento25x25),masestesestãoligados,então,aoalteraralgum
deles,teríamosdemodificarosoutros,sejadividindooumultiplicandoum
peloooutro.
Podemosselecionarnaintrodu çãoafaseeavelocidadedojogo,nadaque
nãotenhamosvistonocapítuloanterior,econstruímosojogointroduzindo
ofluxodevitóriaederrota.
93
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 116

E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 117

Capítulo5
TetrisouQuatroQuadrados
PossodizerqueTetriséojogorussomaisfamosojácriado.Mesmonãocon-
seguindoevitaraguerrafria,equasecausandoumaguerraentreaAtariea
Nintendo,ojogodeAlekeyPajitnov,criadoem1984,foipulicadopelaAtari
(versãonãooficialdesenvolvidapelaTengen)epelaNintendoparaNES,em
1989comummêsdediferen ça.
Alémdecriarmosestequebra-cabe çasanimadoeviciantecapazdega-
rantiralgumasboashorasdediversão,veremosnestecapítulo:
• Manipulaçõesavan çadasdearrays,comocolisãoerota ção;
• Músicaeefeitossonoros;
• Calcularotamanhododesenhodeacordocomatela.
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 118

5.1. Umjogodearrays CasadoCódigo
Fig.5.1:Ojogo
5.1 U m jogo de arrays
Vimosnocapítuloanteriorcomousarumarraytridimensionalparacriarfa-
ses,masdessavezvamosalém:daspe çasquesemovemnatelaatéagrade
ondeelassãoencaixadas.Usaremosarrays,deixandonossosobjetosdaclasse
Elementoforadojogo,aomenosneste.
Temosaseguirtodooesplendorqueumarraycomtrêsdimensõesdeve
ter:
public class Peca {
96
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 119

CasadoCódigo Capítulo5. TetrisouQuatroQuadrados
public static Color[] Cores = {
Color.GREEN, Color.ORANGE,
Color.YELLOW, Color.CYAN, Color.BLUE,
Color.MAGENTA, Color.WHITE };
public static final int[][][] PECAS = {
{
{ 0, 1, 0 },
{ 0, 1, 0 },
{ 1, 1, 0 } },
{
{ 0, 1, 0 },
{ 0, 1, 0 },
{ 0, 1, 1 } },
{
{ 1, 1, 1 },
{ 0, 1, 0 },
{ 0, 0, 0 } },
{
{ 1, 0, 0 },
{ 1, 1, 0 },
{ 0, 1, 0 } },
{
{ 0, 0, 1 },
{ 0, 1, 1 },
{ 0, 1, 0 } },
{
{ 1, 1 },
{ 1, 1 } },
{
{ 0, 1, 0, 0 },
{ 0, 1, 0, 0 },
{ 0, 1, 0, 0 },
{ 0, 1, 0, 0 } }
};
}
Essaénossaclasse Peca.java,responsávelporconternossaspe çaseas
coresdelas,dentrode(mais)umarray.Nãoexistenenhummotivoespecial
97
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 120

5.1. Umjogodearrays CasadoCódigo
paraotipodonossoarray PECASseruminteiro,masnotequecadape ça
temomesmonúmerodelinhasecolunas,sendoqueoszerosrepresentamos
espaçosembrancodaspe ças.
Cadapeçapoderiaserconstruídacomumnúmeroquerepresentassesua
cor,porexemplo, 1paracorverde, 2paracorlaranja,eassimpordiante.En-
tretanto,nossocódigoficoumaissimplesassim,etambémémaisfácilmudar
acordape ça.
Fig.5.2:Pe çasnaordememqueaparecemnocódigo
Nossaclasse JogoCenario.javacontémumagradequerepresentaos
espaçosondeaspe çaspodemserencaixadas.Elaédomesmotipodonosso
arraydepe ças,contendo10colunase16linhas,sendoquecadaespa çona
gradepodeconterumdessesvalores: -1paraosespa çosvazios; -2paraas
linhascompletas;ouoíndicequerepresentaalgumadassetepe ças( 0até6).
...
private static final int ESPACAMENTO = 2;
private static final int ESPACO_VAZIO = -1;
private static final int LINHA_COMPLETA = -2;
private int largBloco, altBloco; // largura bloco e altura bloco
private int ppx, ppy; // Posição peça x e y
private final int[][] grade = new int[10][16];
...
98
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 121

CasadoCódigo Capítulo5. TetrisouQuatroQuadrados
private boolean animar;
private boolean depurar;
...
Essassãoalgumasdasdiversasvariáveisqueutilizamosnojogoeveremos
commaisdetalhesaolongodocapítulo.
Algumaslinhascompletasdepois,emnossométodo carregar:
@Override
public void carregar() {
largBloco = largura / grade.length;
altBloco = altura / grade[0].length;
for (int i = 0; i < grade.length; i++) {
for (int j = 0; j < grade[0].length; j++) {
grade[i][j] = ESPACO_VAZIO;
}
}
...
adicionaPeca();
}
Consideramosqueaspe çassãoformadasporblocos,quatrocadauma,
ecadablocotemsualarguraealturabaseadosnotamanhodisponívelde
cadaespa çonagrade. Essesvaloressãoarmazenadosem largBlocoe
altBloco,quenadamaiséqueadivisãoda largurada telapelota-
manhodoarray(500/10),ea alturapelotamanhodoarrayinterno(672
/16).
Iniciamosnossa gradecomovalor ESPACO_VAZIO,logodepoisuma
peça,escolhidaaleatoriamente,éadicionadaaojogo.
public void adicionaPeca() {
ppy = -2;
ppx = grade.length / 2 - 1;
// Primeira chamada
99
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 122

5.1. Umjogodearrays CasadoCódigo
if (idPeca == -1)
idPeca = rand.nextInt(Peca.PECAS.length);
else
idPeca = idPrxPeca;
idPrxPeca = rand.nextInt(Peca.PECAS.length);
// Isso acontece muito
if (idPeca == idPrxPeca)
idPrxPeca = rand.nextInt(Peca.PECAS.length);
peca = Peca.PECAS[idPeca];
corPeca = Peca.Cores[idPeca];
}
Ape çacome çaumpoucoacimadotopodatelaepróximadocentro.
Usamos idPecae pecaparacontrolarape çaatual(queojogadorcontrola),
e idPrxPecaparaapróximape ça,queprecisamossaberdeantemãopara
dizeraojogadorqueelaviráaseguir.Naprimeirachamada,tantoape çaatual
quantoaqueviráemseguidasãoescolhidasaleatoriamente.
Dasegundachamadaemdiante,ovalordapróximape çapassaparaa
atualeapróximarecebeumnovovalor.Casoocorradeambasseremiguais,
tentamosoutravez.Comoestamostrabalhandocomapenas7possibilidades,
issoocorrebastante.
Duranteojogo,percorremosoarraydape çaselecionada,comparando
seusblocosdiferentesdezerocomovalorcorrespondentenagrade.Utiliza-
mos ppxe ppy(posiçãodape çanoeixoXeY)paramovimentá-la.Quando
elacolidecomabasedagradeoucomoutrape ça,agradeficacomomesmo
valordo idPeca(0a6),noslocaisequivalentesaosvaloresdiferentesde0
dapeça.
100
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 123

CasadoCódigo Capítulo5. TetrisouQuatroQuadrados
Fig.5.3:Simula çãoGradeePe ça
Considerandoafigura5.3,temosprimeiramenteagradevazia,depoisa
gradecomumape çaposicionadanacoluna1elinha0,onde ppxé1e ppy
0.Depois,ape çaémovidaumacolunaparaadireitaeumalinhaparabaixo,
ondeagora ppxé2e ppy1.
Issoquerdizerque,alémdepercorrermosoarray,somamosseuíndice
com ppxe ppyparasabermosaposi çãodape ça.Ométodoqueusamospara
adicionarape çanagradeéumbomexemplodecomoéorelacionamento
entregradeepe ça:
private void adicionarPecaNaGrade() {
for (int col = 0; col < peca.length; col++) {
for (int lin = 0; lin < peca[col].length; lin++) {
if (peca[lin][col] != 0) {
grade[col + ppx][lin + ppy] = idPeca;
}
}
}
}
Percorremosoarraydape çae,paracadavalordiferentede0,agradetem
seuvaloralteradode-1paraovalordo idPeca.Então,saberemoscomqual
coraqueleblocodeveráserpintado. Seosvaloresnagradeformaremuma
linhacompleta(todososvaloresnalinhaforemdiferentesde-1),elapassaa
terovalorde LINHA_COMPLETA.
101
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 124

5.2. Desenhandoarrays CasadoCódigo
Dica
Comooquedeterminaoqueélinhaeoqueécolunaéaformacomo
percorremosedesenhamosoarraynatela,émuitofácilnosconfundir-
moscomasvariáveisnaitera çãodoloop.Paraminimizaressaconfusão,
adotamosaseguinteregra:
Nolaço,chamamosabreviadamentede colasvariáveisqueintera-
gemnoeixoX,ede linasqueinteragemcomoeixoY.
5.2 D esenhando arrays
Agora,comoape çanagradeédesenhada?Jávimosqueotamanhodatela
divididopelotamanhodagradeéquemdeterminaalarguraealturadape ça
( largBlocoe altBloco).
for (int col = 0; col < grade.length; col++) {
for (int lin = 0; lin < grade[0].length; lin++) {
int valor = grade[col][lin];
if (valor == ESPACO_VAZIO)
continue;
if (valor == LINHA_COMPLETA)
g.setColor(Color.RED);
else
g.setColor(Peca.Cores[valor]);
int x = col * largBloco + ESPACAMENTO;
int y = lin * altBloco + ESPACAMENTO;
g.fillRect(x, y, largBloco - ESPACAMENTO,
altBloco - ESPACAMENTO);
}
}
102
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 125

CasadoCódigo Capítulo5. TetrisouQuatroQuadrados
Percorremosagradeobtendoeverificandoovalordecadalinhaecoluna.
Seo valorforumespa çovazio,ignoramos;casocontrário,definimoscom
qualcorape çaserápintada. Utilizamosacorvermelhaparapintarmosas
linhasqueestiveremcompletas.
Depois,achamosaposi çãodobloconatelae,deformasimilaraocapítulo
anterior,pintamosnossoblocolevandoemcontaovalordo ESPACAMENTO.
Oespaçamentoéopcional,serveapenasparadeixarumvãoentreaspe ças.
Fig.5.4:Pe çacomesemespa çamento
Dica
Aumentaroudiminuirexageradamenteoespa çamentoentreaspe ças
deixaojogocomefeitosnomínimointeressantes.
Ocódigoparadesenharape çaemjogoébemparecidocomoanterior,
levandoemconsidera çãoaposi çãodape çanoseixos:
if (peca != null) {
g.setColor(corPeca);
for (int col = 0; col < peca.length; col++) {
for (int lin = 0; lin < peca[col].length; lin++) {
if (peca[lin][col] != 0) {
int x = (col + ppx) * largBloco + ESPACAMENTO;
int y = (lin + ppy) * altBloco + ESPACAMENTO;
103
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 126

5.2. Desenhandoarrays CasadoCódigo
g.fillRect(x, y, largBloco - ESPACAMENTO,
altBloco - ESPACAMENTO);
} else if (depurar) {
g.setColor(Color.PINK);
int x = (col + ppx) * largBloco + ESPACAMENTO;
int y = (lin + ppy) * altBloco + ESPACAMENTO;
g.fillRect(x, y, largBloco - ESPACAMENTO,
altBloco - ESPACAMENTO);
g.setColor(corPeca);
}
}
}
}
Paraajudarnadepura çãodocódigo,seavariável depurarforverda-
deira,exibimosaspartesocultasdape ça(osvaloresiguaisa 0)nacorrosa.
Paraajudarnatomadadedecisãodojogador,desenhamosapróximape ça
usandoumtamanhomenorquealarguradobloco.
int miniatura = largBloco / 4;
int[][] prxPeca = Peca.PECAS[idPrxPeca];
g.setColor(Peca.Cores[idPrxPeca]);
for (int col = 0; col < prxPeca.length; col++) {
for (int lin = 0; lin < prxPeca[col].length; lin++) {
if (prxPeca[lin][col] == 0)
continue;
int x = col * miniatura + ESPACAMENTO;
int y = lin * miniatura + ESPACAMENTO;
g.fillRect(x, y, miniatura - ESPACAMENTO,
miniatura - ESPACAMENTO);
}
}
104
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 127

CasadoCódigo Capítulo5. TetrisouQuatroQuadrados
Multiplicamoscolunaelinhapelotamanhoda miniatura,semesque-
cerdeadicionaroespa çamentoparaoformatododesenhoficarparecido.
Nota
Nasaladeinformáticadocolégio,apósdescobrirqueumprofessor
haviacriadosuaprópriaversãodoTetris(emPascal,senãomeengano),
essejogopassouameintrigarmaisdoquedivertir.
Eusimplesmentenãoconseguiaentendercomoaspe çasseencaixa-
vamumasnasoutras,comoelasficavampresas,edepoissimplesmente
formavamlinhasquedesapareciam.Bem,esperoque,aofinaldesteca-
pítulo,vocêentendacomoissofuncionamelhorqueeu,oupelomenos,
tãobemquantoohackerVadimGerasimov,responsávelpeloportedo
jogoparaIBM-PC.
5.3 J ogando o código
Quandoojogadormoveape çaparaaesquerda,paraadireitaouparabaixo,
precisamosvalidaromovimentoegarantirqueanovaposi çãonãoquebreo
jogo.Nossométodo validaMovimentogarantequeissonãoaconte ça.
public boolean validaMovimento(int[][] peca, int px, int py) {
if (peca == null)
return false;
for (int col = 0; col < peca.length; col++) {
for (int lin = 0; lin < peca[col].length; lin++) {
if (peca[lin][col] == 0)
continue;
int prxPx = col + px; // Próxima posição peça x
int prxPy = lin + py; // Próxima posição peça y
if (prxPx < 0 || prxPx >= grade.length)
return false;
105
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 128

5.3. Jogandoocódigo CasadoCódigo
if (prxPy >= grade[0].length)
return false;
if (prxPy < 0)
continue;
// Colidiu com uma peça na grade
if (grade[prxPx][prxPy] > ESPACO_VAZIO)
return false;
}
}
return true;
}
Comodecostume,ignoramososvaloresiguaisa 0.Depoisdeacharmos
apróximaposi çãodape ça,verificamosseelanãoacabaforadatela,sendo
menorquezerooumaiorqueotamanhodagrade.Issoparavalida çãohori-
zontal;jánaverticalape çapodecome çarforadatela.Então,somenteverifi-
camosseafuturaposi çãonãoultrapassaotamanhodagrade,ignorandoum
valormenorquezero.
Porfim,verificamosseaposi çãocoincidecomumvalorjápreenchidona
grade.Casoissoocorra,seráummovimentoinválido,jáqueumape çanão
podesesobreporaoutra.Observequeaordemdavalida çãoéimportantee
usamosamesmavalida çãoparagirarape ça.
Verificarcolisãoéummétodosemelhanteaodevalidarmovimento,tão
semelhantequepoderiaseromesmométodocomalgumasaltera ções. En-
tretanto,separamosemdoisparadeixarclaroquandoestamosvalidandoo
movimentoequandoestamosverificandoseape çacolidiu.
private boolean colidiu(int px, int py) {
if (peca == null)
return false;
for (int col = 0; col < peca.length; col++) {
106
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 129

CasadoCódigo Capítulo5. TetrisouQuatroQuadrados
for (int lin = 0; lin < peca[col].length; lin++) {
if (peca[lin][col] == 0)
continue;
int prxPx = col + px;
int prxPy = lin + py;
// Chegou na base da grade
if (prxPy == grade[0].length)
return true;
// Fora da grade
if (prxPy < 0)
continue;
// Colidiu com uma peça na grade
if (grade[prxPx][prxPy] > ESPACO_VAZIO)
return true;
}
}
return false;
}
Nestemétodo,nãorecebemosa pecacomoparâmetro,umavezque
sempreverificamosacolisãodape çaemjogo.Masamaiordiferen çaéque
retornamosverdadeiroondeanteseraretornadofalso,alémdenãovalidar-
mosaposi çãodape çanahorizontal. Essemétodopoderiafacilmenteser
substituídopor:
private boolean colidiu(int px, int py) {
return !validaMovimento(peca, px, py);
}
Maissimplesquevalidaromovimentoousaberseape çacolidiuéverifi-
carseelaficouforadagrade:
private boolean parouForaDaGrade() {
if (peca == null)
107
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 130

5.3. Jogandoocódigo CasadoCódigo
return false;
for (int lin = 0; lin < peca.length; lin++) {
for (int col = 0; col < peca[lin].length; col++) {
if (peca[lin][col] == 0)
continue;
// Fora da grade
if (lin + ppy < 0)
return true;
}
}
return false;
}
Seape ça colidiu,nósaadicionamosnagradeeverificamosseelapre-
encheuumaoumaislinhas.Seissoocorrer,marcamosaslinhaspreenchidas:
private boolean marcarLinha() {
int multPontos = 0;
for (int lin = grade[0].length - 1; lin >= 0; lin--) {
boolean linhaCompleta = true;
for (int col = grade.length - 1; col >= 0; col--) {
if (grade[col][lin] == ESPACO_VAZIO) {
linhaCompleta = false;
break;
}
}
if (linhaCompleta) {
multPontos++;
for (int col = grade.length - 1; col >= 0; col--) {
grade[col][lin] = LINHA_COMPLETA;
}
}
}
108
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 131

CasadoCódigo Capítulo5. TetrisouQuatroQuadrados
Este loopjádiferedosanteriores.Reparebemque,alémdecome çarmos
pelaslinhas,come çamosdaúltimaparaaprimeira.
Começamosconfiantes,acreditandoqueacharemosumalinhacompleta.
Então,linhaporlinha,verificamoscadacoluna,masaoencontrarumaco-
lunavazia,falamosqueosonhodalinhacompletanãoestánaquelalinha(
linhaCompleta = false ),eignoramosasdemaiscolunas,passandopara
alinhaseguinte.
Entretanto,quandotodasascolunasestãopreenchidas,incrementamos
nossomultiplicadordepontosepercorremosamesmalinhanovamente,
marcandocadacoluna( grade[col][lin] = LINHA_COMPLETA ).
pontos += multPontos * multPontos;
linhasFeistas += multPontos;
if (nivel == 9 && linhasFeistas >= 9) {
estado = Estado.GANHOU;
} else if (linhasFeistas >= 9) {
nivel++;
linhasFeistas = 0;
}
return multPontos > 0;
}
Depoisdeverificarmoslinhasecolunasdagrade,premiamosojogador
comseuspontos,equantomaislinhasconsecutivas,maispontos.Osníveis
dojogovãode1a9,fazendoaspe çascaíremmaisrápidoconformevãoau-
mentando.Todavezqueojogadorcompleta9oumaislinhas,oníveldojogo
sobeautomaticamentee,quandoelecompletaaúltimalinhadoúltimonível,
ganhaojogo.
Precisamos saber se marcamos alguma linha, então, retornamos
multPontos > 0 ,queseráverdadeirosetivermosalgumalinhacompleta.
Tendolinhascompletas,fazemo-lasdesaparecem,easqueestavamacimade-
lasdescerem.
for (int col = 0; col < grade.length; col++) {
for (int lin = grade[0].length - 1; lin >= 0; lin--) {
109
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 132

5.3. Jogandoocódigo CasadoCódigo
if (grade[col][lin] == LINHA_COMPLETA) {
int moverPara = lin;
int prxLinha = lin - 1;
for (; prxLinha > -1; prxLinha--) {
if (grade[col][prxLinha] == LINHA_COMPLETA)
continue;
else
break;
}
for (; moverPara > -1; moverPara--, prxLinha--) {
if (prxLinha > -1)
grade[col][moverPara] = grade[col][prxLinha];
else
grade[col][moverPara] = ESPACO_VAZIO;
}
}
}
}
Esteéocódigoprincipaldométodo descerColunas(),enossofoco
agoraémaisnascolunasdoquenaslinhas.Verificamosverticalmentecada
coluna,daúltimaparaaprimeira,eosvalorescontidosemcada,jáqueuma
colunapodetermaisblocosqueoutra.Quandoachamosumaposi çãomar-
cadacomo LINHA_COMPLETA,definimosqueestaseráanovabasedaspe ças
acima( int moverPara = lin ).
Como o jogador pode fazer até quatro linhas consecutivas, usamos
prxLinhaparacontá-las.Sendoquepodemosterlinhascompletasseguidas
ouintermitentes,averifica çãoseestendeatéaprimeiracoluna(la çointerno
enquanto moverParaformaiorque -1).Enquanto prxLinhativerumva-
lorválido,sabemosquetemosblocosparadescer;senão,osblocosalocados
naqueleespaçojádesceram,deixandoumespa çovazio.
110
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 133

CasadoCódigo Capítulo5. TetrisouQuatroQuadrados
Nota
Eu acho este um dos métodos mais complexos do jogo,
a ponto de quase chamar o capítulo de T etris, o jogo do
ArrayIndexOutOfBoundsException.
Finalmentegiramosape ça,etemosduasversõesparaestemétodo. A
primeiranãorealocaape ça,entãoseelaestiverpertodemaisdaslaterais,
ojogadornãoconseguirágirá-las,igualaversõesdoTetrisparaNES(dife-
rentedaversãodaTengen,quetinhaatémodomultijogador).Simplesmente
usamosumarraytemporárioecolocamosemlinhaosvaloresqueestãoem
coluna.Porisso,osarraysdaspe çasprecisamteromesmonúmerodelinhas
ecolunas.
protected void girarPeca(boolean sentidoHorario) {
if (peca == null)
return;
final int[][] temp = new int[peca.length][peca.length];
for (int i = 0; i < peca.length; i++) {
for (int j = 0; j < peca.length; j++) {
if (sentidoHorario)
temp[j][peca.length - i - 1] = peca[i][j];
else
temp[peca.length - j - 1][i] = peca[i][j];
}
}
System.out.println("Antes:");
imprimirArray(peca);
System.out.println("Depois:");
imprimirArray(temp);
if (validaMovimento(temp, ppx, ppy)) {
peca = temp;
}
111
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 134

5.3. Jogandoocódigo CasadoCódigo
}
Seojogadorgirarape çanosentidohorário,osvaloresdaprimeiralinha
vãoparaaúltimacoluna,edaúltimalinhaparaaprimeiracoluna.Segirarno
sentidoanti-horário,osvaloresdaprimeiralinhavãoparaaprimeiracoluna.
Asoluçãoésimples,masaexecu çãopodeparecerconfusacasonãocon-
sigavisualizarasposi çõesdoarray.Logo,fazerumpassoapassonopapelvai
ajudar.Vejanossasimula çãocomumape çafictícia:
Fig.5.5:Cirandadaspe ças
Você ainda pode contar com odepurar e com o nosso método
imprimirArray,capazesdeproduziresseresultado:
112
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 135

CasadoCódigo Capítulo5. TetrisouQuatroQuadrados
Fig.5.6:Girandoape ça
Antesdeseguiremfrentecomomovimento,verificamosseape çavi-
radaestáemumaposi çãoválida,masseape çagiradaacabarforadatela,as
modificaçõesserãoignoradas.
Asegundaversãodométodoresolveesseproblema,reposicionandoa
peça:
private void girarReposicionarPeca(boolean sentidoHorario) {
if (peca == null)
return;
int tempPx = ppx;
final int[][] tempPeca = new int[peca.length][peca.length];
//... Girar a peça
// Reposiciona peça na tela
for (int i = 0; i < tempPeca.length; i++) {
for (int j = 0; j < tempPeca.length; j++) {
if (tempPeca[j][i] == 0) {
continue;
}
113
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 136

5.3. Jogandoocódigo CasadoCódigo
int prxPx = i + tempPx;
if (prxPx < 0)
tempPx = tempPx - prxPx;
else if (prxPx == grade.length)
tempPx = tempPx - 1;
}
}
if (validaMovimento(tempPeca, tempPx, ppy)) {
peca = tempPeca;
ppx = tempPx;
}
}
Seape çaacabarforadagrade,teremosum prxPxnegativooumaior
queonúmerodecolunas.Ovalorsendonegativo,subtraímosomesmova-
lorgerandoumresultadopositivo.Casoovalorsejamaiorqueoesperado,
subtraímos1de tempPx,atéquetodososblocosestejamdentrodoslimites
datela.
Utilizamosumavariáveltemporária,jáqueasalteraçõessópodemacon-
tecerseape çaestiveremumaposi çãoválida,nestecaso,nãocolidindocom
outraspeças.
Nahoradeatualizarojogo,nadamuitodiferentedoquejáfizemosnos
outros:
...
if (Jogo.controleTecla[Jogo.Tecla.ESQUERDA.ordinal()]) {
if (validaMovimento(peca, ppx - 1, ppy))
ppx--;
} else if (Jogo.controleTecla[Jogo.Tecla.DIREITA.ordinal()]) {
if (validaMovimento(peca, ppx + 1, ppy))
ppx++;
}
114
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 137

CasadoCódigo Capítulo5. TetrisouQuatroQuadrados
if (Jogo.controleTecla[Jogo.Tecla.CIMA.ordinal()]) {
girarReposicionarPeca(false);
} else if (Jogo.controleTecla[Jogo.Tecla.BAIXO.ordinal()]) {
if (validaMovimento(peca, ppx, ppy + 1))
ppy++;
}
...
Paraesquerdaouparadireita,decrementamosouincrementamos ppx
em1,movendoape çacolunaporcoluna.Aopressionarparabaixo,acelera-
mosadescidadape çaaumentando ppy,umalinhaporvez,eaopressionar
paracima,giramosape ça. Lembrandoqueaatualiza çãodessesvaloressó
ocorreseape çativerummovimentoválido.
Outrodestaquedométodo atualizar()éque,depoisdeojogador
formaralgumalinhacompleta,nãoadicionamosumanovape çaimediata-
mente,dandoumtempoparaeleversuaslinhascompletasdestacadasnacor
vermelhaantesdedesaparecerem,umapequenaanima ção.
if (animar && temporizador >= 5) {
animar = false;
descerColunas();
adicionaPeca();
} else if (temporizador >= 20) {
temporizador = 0;
if (colidiu(ppx, ppy + 1)) {
...
if (!parouForaDaGrade()) {
adicionarPecaNaGrade();
animar = marcarLinha();
peca = null;
if (!animar)
115
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 138

5.3. Jogandoocódigo CasadoCódigo
adicionaPeca();
} else {
estado = Estado.PERDEU;
}
} else
ppy++;
} else
temporizador += nivel;
Usamosovelhoeconhecido temporizadorparasabersechegouahora
deanimarouatualizarojogo.Nahoradeatualizar,verificamosseapróxima
posiçãodape çaresultaráemumacolisão.Casonãocolida,continuamosdes-
cendoape ça,deacordocomavelocidadedoníveldojogo.Casocolida,veri-
ficamossealgumblocoparouforadagrade;seissoacontecer,ojogoacaba,se
não,adicionamosape çanagradeeverificamossealgumalinhacompletafoi
formada.Então, animarrecebeovalorverdadeiroeaslinhassãomarcadas
eexibidasemoutracor,daíapagamosape ça( peca = null )paraqueela
nãosejamaisdesenhada.
Senenhumalinhacompletafoiformada, animarrecebeovalorfalso,
entãoadicionamosumanovape ça. Onosso animarnãotemanima ção,
apenasesperamosumpoucoantesdesumircomaslinhasmarcadaseadi-
cionarmosumanovape ça,masencorajovocêafazeralgomaisinteressante
aqui.
116
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 139

CasadoCódigo Capítulo5. TetrisouQuatroQuadrados
Dica
Paraajudarnostestesdojogo,adicionamosumateclaparatrocara
peçaprincipal.Ficouassim:
if (depurar && Jogo.controleTecla[Jogo.Tecla.BC.ordinal()]){
if (++idPeca == Peca.PECAS.length)
idPeca = 0;
peca = Peca.PECAS[idPeca];
corPeca = Peca.Cores[idPeca];
}
TemosaquiumaboaversãodoTetris,sendoumdosjogosmaiscomple-
tosquefizemosatéagora: cominício,meioefim;desafiosqueaumentam
gradualmente;cores,pausaepontua ção. Massinceramente,sóissonãoéo
suficiente,eumjogosempreficamelhorcomsom.
5.4 E feitos sonoros
OJavatemsuportenativoaosformatos wav, aif, rmf, aue mid.Estes
podemvariardependendodaplataforma,eoutrossãosuportadosusando
bibliotecasàparte,comooJavaMediaFramework(JMF),ondevocêconsegue
reproduzirdesdeopopular mp3atéformatosdevídeo.
Aquiveremososformatos .mid(Musical instrument Digital Interface)e
.wav(Windows Wave).
Começamospeloobjeto Clipdopacote javax.sound.sampled.
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
try {
AudioInputStream as = AudioSystem.getAudioInputStream(
new File("som/piano_quebrado.mid"));
117
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 140

5.4. Efeitossonoros CasadoCódigo
Clip clip = AudioSystem.getClip();
clip.open(as);
} catch (Exception e) {
e.printStackTrace();
}
Primeiro,carregamosoarquivo piano_quebrado.mid,queestáden-
trodapasta som,napastaraizdoprojeto.Depois,obtemosumobjeto Clip
paracontrolaroáudiocarregado. Tudoissotratandoqualquerexce çãoque
possaocorrer,jáqueaindapoderemosjogarsemsom.
Basicamente, oquefazemoscomumobjeto Clipétocarumavez,
váriasvezesoucontinuamenteoáudioe, claro, parardetocar. Aocha-
mar clip.start()ou clip.loop(0),tocamosoáudioumavez. Já
clip.loop(10)tocaoáudio11vezes(tocaumavezerepetedez).
Para tocar até não querer mais, utilize
clip.loop(Clip.LOOP_CONTINUOUSLY) e, para não tocar mais,
clip.stop(). Quando descarregar a cena, não se esqueça de parar a
músicaeliberarrecursos.
@Override
publicvoid descarregar() {
if (clip != null) {
clip.stop();
clip.close();
}
}
ComJava,vocêtembastantecontrolesobreoáudioqueestásendorepro-
duzido.RecomendoprocurarporJavaSoundAPI:JavaSoundDemo(http:
//www.oracle.com/technetwork/java/index-139508.html),ondevocêconse-
gueverexemploscomo:
• Tocarformatoswav, aif, rmf, aue mid;
• Controlarovolumedeáudio,inclusiveindividualmenteemcadacanal
(Panning);
118
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 141

CasadoCódigo Capítulo5. TetrisouQuatroQuadrados
• Gravaçãodeáudio;
• Gerarseuprópriomidcomumsimuladordepiano(comváriosefeitos,
inclusivedesomdetiro);
• Fazersolosdebateria.
Dica
Foi do Java Sound Demo que veio meu MIDI de sucesso:
piano_quebrado.
QuandofalamosdeMIDI,oobjeto Clipéparaomaisbásico,umavez
que,utilizando Sequencer,podemosmanipulararquivosMIDIcomrecur-
sosadicionais,comoaceleraroáudioalterandoasbatidasporminuto.Veja
maisemhttp://docs.oracle.com/javase/tutorial/sound/MIDI-seq-intro.html.
Paracarregarnosso .midutilizando Sequencer,nossocódigoficaria
assim:
import javax.sound.midi.MidiSystem;
import javax.sound.midi.Sequencer;
try {
Sequencer seq = MidiSystem.getSequencer();
seq.setSequence(
MidiSystem.getSequence(
new File("som/piano_quebrado.mid")));
seq.open();
} catch (Exception e) {
e.printStackTrace();
}
seq.setLoopCount(Sequencer.LOOP_CONTINUOUSLY);
seq.start();
As diferenças no código come çam no pacote. Usamos
javax.sound.midi em vez de javax.sound.sampled, e a classe
119
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 142

5.5. Tetrissonoro CasadoCódigo
MidiSystememvezdaclasse AudioSystem.Notequeutilizamosoatalho
setSequence, mesmo assim o métodoopendeve ser chamado. Não
podemosnosesquecerdechamarométodo start,jáquenãotemoso
atalho loop.
Orestantedocódigoficaparecido,apenasaten çãoparanãoconfundiro
objeto Sequencecomainterface Sequencer(queterminacomR).
Supondoquevocêqueiraaceleraroáudioquandoojogadorestivercom
linhaspróximasaotopo,oudeixaravelocidadedoáudiodeacordocomoní-
veldasfases,bastariachamar seq.setTempoInBPM(300),que,nestecaso,
aceleraamúsicaem 300batidasporminuto.
5.5 T etris sonoro
Além de uma música MIDI de fundo, adicionamos dois efeitos (
adiciona_peca.wav e 109662_grunz_success.wav): um para
quandoape çacolidir,eoutroquandoojogadorcompletarumaoumaisli-
nhas.
// Som
private AudioInputStream as;
private Clip clipAdicionarPeca;
private Clip clipMarcarLinha;
private Sequencer seqSomDeFundo;
...
@Override
public void carregar() {
try {
as = AudioSystem.getAudioInputStream(
new File("som/adiciona_peca.wav"));
clipAdicionarPeca = AudioSystem.getClip();
clipAdicionarPeca.open(as);
as = AudioSystem.getAudioInputStream(
new File("som/109662_grunz_success.wav"));
120
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 143

CasadoCódigo Capítulo5. TetrisouQuatroQuadrados
clipMarcarLinha = AudioSystem.getClip();
clipMarcarLinha.open(as);
Utilizamos dois objetos Clip, clipAdicionarPeca e
clipMarcarLinha, para nosso áudio WAV. Um efeito sonoro para
quandoadicionamosape çanagradeeoutroparaquandomarcamosas
linhasfeitas.FicamoscomoMIDIeo Sequencer seqSomDeFundo para
músicadefundo.
seqSomDeFundo = MidiSystem.getSequencer();
seqSomDeFundo.setSequence(
MidiSystem.getSequence(
new File("som/piano_quebrado.mid")));
seqSomDeFundo.open();
seqSomDeFundo.setLoopCount(Sequencer.LOOP_CONTINUOUSLY);
seqSomDeFundo.start();
} catch (Exception e) {
e.printStackTrace();
}
}
Aocontráriodosefeitosqueacontecerãoemdeterminadosmomentosdo
jogo,nossamúsicadefundoéiniciadanocarregamentoetocadadeforma
continua.
Dica
ParasaberquaisformatosseuS.O.suporta:
Type[] audioFileTypes = AudioSystem.getAudioFileTypes();
for (Type t : audioFileTypes) {
System.out.println(t.getExtension());
}
121
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 144

5.5. Tetrissonoro CasadoCódigo
Comonãoestamostocandoosclipesdeáudioemloop,temosdereiniciá-
los( setFramePosition(0))quandoeleschegamaofim.Assim,reinicia-
mosprimeiroetocamosdepois.
...
} else if (temporizador >= 20) {
temporizador = 0;
if (colidiu(ppx, ppy + 1)) {
if (clipAdicionarPeca != null) {
clipAdicionarPeca.setFramePosition(0);
clipAdicionarPeca.start();
}
...
} else
temporizador += nivel;
...
Naatualizaçãodojogo,quandoverificarmosqueape çacolidiu,inicia-
remosnossoefeitosonoro.Deformaparecida,tocaremosnossoefeitopara
completarlinhas.
private void descerColunas() {
...
if (clipMarcarLinha != null) {
clipMarcarLinha.setFramePosition(0);
clipMarcarLinha.start();
}
}
Vale notar que, se fosse um objeto Sequencer em vez de
Clip, chamaríamos o método setTickPosition(0) no lugar de
setFramePosition(0).
Porfim,antesdesairdo JogoCenario,nãoesque çadedesligarosom.
@Override
public void descarregar() {
122
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 145

CasadoCódigo Capítulo5. TetrisouQuatroQuadrados
if (clipAdicionarPeca != null) {
clipAdicionarPeca.stop();
clipAdicionarPeca.close();
}
if (clipMarcarLinha != null) {
clipMarcarLinha.stop();
clipMarcarLinha.close();
}
if (seqSomDeFundo != null) {
seqSomDeFundo.stop();
seqSomDeFundo.close();
}
}
Agoraqueestamostrabalhandocomrecursosexternos,nossojogopode
nãoiniciartãorapidamentecomoantes.Então,naclasse Jogo.java,den-
trodométodo iniciarJogo,depoisqueojogadorescolheremquefase
desejacome çar,adicionamosumamensagemparaavisardocarregamento
dopróximocenário.
if (cenario instanceof InicioCenario) {
cenario.descarregar();
cenario = null;
cenario = new JogoCenario(tela.getWidth(), tela.getHeight());
g2d.setColor(Color.WHITE);
g2d.drawString("Carregando...", 20, 20);
tela.repaint();
cenario.carregar();
...
SeestiveremdúvidasobreutilizarMIDIouWAV,leveemconsidera-
çãoqueoMIDIéfácildecriaremenor,masaqualidadesonoradepende
daplacadesom,entãopodehaverdiferen çasentrediferentescomputado-
res.JáoWAV,semcompacta ção,éumarquivomuitomaior,mastemmais
123
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 146

5.6. Programar,desenhareaindaterdecompor? CasadoCódigo
qualidadedesometendeaseromesmoemqualquercomputador.
Enquantodesenvolvia,percebique,mesmooWAVsendomaior,elecar-
regoumaisrápidoenãoteveatrasoentreachamadaeaexecu ção.Porisso,
utilizeiMIDIcomosomdefundoeWAVparaefeitossonoros.Emtodocaso,
ambososformatosparaosáudios adiciona_pecae piano_quebradoes-
tãonoprojeto,paraquevocêpossafazersuasprópriascompara çõesedecidir
oqueficamelhornoseujogo(http://www.abyssmedia.com/midirenderer/
midi-vs-wav.shtml).
5.6 P rogramar , desenhar e ainda ter de com -
por?
Temosmuitacoisaprontanainternet,emúsicaseefeitossonorospodemser
encontradosem:
• http://freesound.org;
• http://soundbible.com;
• http://www.soundjay.com;
• http://pt.audiomicro.com(pago).
Masébemprovávelqueseusarquivosprecisemdealgunsajustes,ouque
vocêosencontreemumformatoequeiraconvertê-losemoutro.Paraesses
eoutrosajustes,recomendo:
•Audacity–Editordeáudiodigitallivre(http://audacity.sourceforge.
net);
•Conversion-tool.com–Conversoronlinequevaialémdosformatosde
áudio(http://www.conversion-tool.com).
Oarquivo 109662_grunz_success.wav,usadonahorademarcar
linha,éumefeitosonorobaixadonoFreesoundeeditadonoAudacity.
124
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 147

CasadoCódigo Capítulo5. TetrisouQuatroQuadrados
5.7 C odificando o jogo
Realmentenãoimaginocomoestejogoseriaconstruídosemousodearrays,
efizemoscódigosuficienteparapercorrê-losdequasetodasasformaspos-
síveis.Tudoestádisponívelemhttps://github.com/logicadojogo/fontes/tree/
master/Cap05.
Exagerosàparte,temosumaclassenovachamada Peca.java,queficou
responsávelpelaconstruçãodaspe çasdojogo,aocontráriodanossaclasse
JogoCenario.java,ondeacomplexalógicadojogofoidivididaemméto-
dosmenoreseespecíficos.
Dentro da pasta som, você encontra os seguintes arqui-
vos: 109662_grunz_success.wav, adiciona_peca.mid,
adiciona_peca.wav, piano_quebrado.mid e
piano_quebrado.wav.
Algumasmodificaçõesnaclasse Jogo.java, InicioCenario.java
esó.
Não fizemos aqui
• Teraopçãodejogarcomesemsom,ousomenteefeitossonoros;
• Manipularamúsicadefundoduranteojogo.
Melhore você mesmo
• Adicionarumbotãoparagirarapeçanosentidohorário;
• Colocarsuaprópriamúsicadefundoeefeitossonoros.
5.8 R esumo
Nossojogode7pe çasde4quadradostemumalógicacomplexae,emnenhum
outrojogodestelivro,apalavraarrayseráusadatantasvezes.
Começamospelaspe çasquesãosimplesdeseremconstruídas. Depois,
combasenotamanhodagradeedatela,definimosalarguraealturaemque
125
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 148

5.8. Resumo CasadoCódigo
aspe çasserãodesenhadas. Mesmoelassendoadicionadasaleatoriamente,
conseguimossaberqualviránasequência. Depois,vimoscomoposicioná-
las,preenchendoedesenhandoagrade.
Duranteojogo,validamosamovimenta ção,acolisãoearota çãodape ça,
etemosduasversõesdiferentesparagirá-las:umaquereposicionaeoutraque
não.Seelapararforadagrade,ultrapassandootopodatela,ojogadorperde.
Masapós9níveise81linhasfeitas,eleganhaojogo;emboraojogadorpossa
escolheremquallevelcome çar,eleestariaabrindomãodeumapontua ção
maior.Aindaanimamosojogoecriamosalgumasformasdedepura ção.
Comojogopronto,melhoramoscomefeitossonoros,usandoasclasses
nativasdoJava. Comcerteza,amaioriadosjogosnoestiloquebra-cabe ças
(puzzle)quevocêdesenvolverserámaisfácildepoisdestecapítulo.
126
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 149

Capítulo6
Pac-Man,vulgoCome-come
CriadoporToruIwataniem1979,lan çadoem1980,Pac-Manqueriasedife-
renciardosjogosdetirodaépocaeatrairopúblicofeminino,maselecon-
seguiubemmaisqueisso,tornou-seumsímbolointernacionaldosjogosde
videogames,umsuperastroinspiradoemumpeda çodepizza.
DesenvolverumjogocomooPac-Mansemusarimagensé,nomínimo,
ofensivo,maseleenvolvemuitosconceitoscomplexosaindanãoabordados.
Então,seguindooditado“dividirparaconquistar”,nestecapítuloabordare-
mosaspectosrelacionadosàlógicadojogo,edepoisveremosasprincipais
formasdetrabalharmoscomimagens,alémde:
• PerseguiçãoefugacomInteligênciaArtificial;
• Fluxodeestadosdospersonagens;
• Colisãodeelementosemeixocomitensnoarray.
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 150

CasadoCódigo
Fig.6.1:Come-come
128
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 151

CasadoCódigo Capítulo6. Pac-Man,vulgoCome-come
6.1 C aça fantasma
Jávimoscomomontarcenáriosebrincamosbastantecomarray.Anovidade
aquiéque,emboranossocenáriosejaumarray(formandoumagradecomo
noTetris),oselementossemovempixelapixel(parecidocomnossojogoda
cobrinha),enãoemlinhasecolunas,tendoassimumamovimenta çãofluida.
Montamosalgunsníveisnocapítulo4,entãovocêjásabecomoissoserá
feitoaqui.Esteénossocenário:
Fig.6.2:Cenário
Emvezdeutilizarmosvaloresinteirosdiretamente,vamossepará-losem
constantes:
public static final int BL = 0; /* Bloco */
public static final int CN = 1; /* Comida normal */
public static final int EV = 2; /* Espaco vazio */
public static final int PI = 3; /* Ponto inicial do jogador */
public static final int LN = 4; /* Linha */
public static final int SC = 5; /* Super comida */
public static final int P1 = 6; /* Ponto inicial inimigo 1 */
public static final int P2 = 7; /* Ponto inicial inimigo 2 */
129
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 152

6.1. Caçafantasma CasadoCódigo
public static final int PF = 8; /* Ponto de Fuga */
public static final int PV = 9; /* Ponto de Volta */
Comoestamosutilizandodiversosvalores,armazená-losemconstantes
facilitaráaprogramaçãodojogo. Algunsvaloressãousadosparamontar
nossolabirinto(0a5),outrosservemparaauxiliarnamovimenta çãoecon-
figuraçãodospersonagens(6a9).Come çandopor:
•BL(BLoco),usadoparaformaraparededonossolabirinto.
•CN(Comida Normal),querepresentaaspastilhas/pílulasquedevem
serdevoradas.
•SC(SuperComida)éapílulamaiorquedápoderaopersonagem.
•EV(Espaço Vazio)éapartesemitemdocenário.
• Umapastilhaousupercomidaque,apósser“comida”,viraumespaço
vazio.
•LN(LiNha)éaparedeespecialporondesomenteosinimigospodem
passar.
Paraconfigurarojogo,temos:
•PI(Ponto Inicial)usadoparadeterminarondenossoheróicome çará.
•P1e P2,quesãoasposi çõesiniciaisdecadainimigo(nessaversãodo
jogo,sóteremosdois).
•PF(PontodeFuga)e PV(PontodeVolta),quetêmfun çõesopostas,
oprimeiroindicaondeéasaídaparaoinimigoqueestápreso(ficado
ladodeforadaprisão);osegundoserveparaqueoinimigoquevirou
fantasmasejaressuscitado(ficadoladodedentrodaprisão).
Assim,poderemosmontaralgoparecidocomojogooriginal:
130
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 153

CasadoCódigo Capítulo6. Pac-Man,vulgoCome-come
Fig.6.3:Baseadoemcenáriosreais
Agoraquevimosagradeetudooquepodemoscolocarnela,veremos
comoelaéusadanojogo.Temosaquiumarray31x28,issoé,umarraycon-
tendo31posi çõesecadaumadessasposi çõestemoutroarraycom28po-
sições. Oprimeirousadopararepresentaraslinhas( grade.length),o
segundo,ascolunas( grade[0].length).
Cadaitemnatelateráotamanhode16px,resultandonaalturade496px
(31*16)elargurade448px(28*16).Mas,paraficarmaisparecidocomojogo
original,aumentamosaalturadatelapara550px,deixandoespa çoacimae
abaixodolabirinto.Armazenamososvaloresdesseespa çamentonaconstante
estáticaJogoCenario.ESPACO_TOPO.
Nossoscírculoscoloridossãoosúnicosobjetosquesemovem,entãoeles
nãosãosimples Elementos,sãoelementos Pizza.
public class Pizza extends Elemento {
public enum Modo {
PRESO, ATIVO, INATIVO, FANTASMA, CACANDO, FUGINDO;
}
private int dx, dy;
private Modo modo = Modo.PRESO;
131
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 154

6.1. Caçafantasma CasadoCódigo
private Direcao direcao = Direcao.OESTE;
public Pizza(int px, int py, int largura, int altura) {
super(px, py, largura, altura);
}
@Override
public void desenha(Graphics2D g) {
if (modo == Modo.FUGINDO)
g.setColor(Color.LIGHT_GRAY);
else
g.setColor(getCor());
if (modo == Modo.FANTASMA)
g.drawOval(getPx(), getPy() + JogoCenario.ESPACO_TOPO,
getLargura(), getAltura());
else
g.fillOval(getPx(), getPy() + JogoCenario.ESPACO_TOPO,
getLargura(), getAltura());
}
Emboraapenasosinimigostenhammodos/estadosdiferenciados,eles
sãomuitoutilizadosduranteojogo,inclusiveparadeterminarcomoserão
desenhados:
• Círculo preenchido na cor cinza quando estão fugindo (
Modo.FUGINDO);
• Círculo sem preenchimento caso tenham virado fantasma (
Modo.FANTASMA);
• Círculopreenchidocomacorindividualpré-definidaparaosoutros
estados.
Sejaqualforoformatododesenho,levamosemcontaoespa çamento
superiorsomando-oaoeixoY.
@Override
public void atualiza() {
132
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 155

CasadoCódigo Capítulo6. Pac-Man,vulgoCome-come
incPx(getVel() * getDx());
incPy(getVel() * getDy());
}
...
}
Outranovidadeéquecontrolamosadire çãodospersonagensusando
pontoscardeais: NORTE, SUL, OESTEe LESTE.Comoadire çãoécontrola
pelojogador,nosso enum Direcao ficanaclasse JogoCenario.java.
Nossavariável direcaoémaisusadaparaindicarparaondeojogador
pretendeir,nãonecessariamenteparaondeoelementoestáindo,deixandoo
controlerealdamovimenta çãoacargode dxe dy,comojávistoemoutros
capítulos.
Falaremosmaissobreamovimenta çãodospersonagens,masantesva-
mos ver como eles são criados dentro do métodocarregarda classe
JogoCenario:
...
largEl = largura / grade[0].length; // 16px
pizza = new Pizza(0, 0, largEl, largEl);
pizza.setVel(4);
pizza.setAtivo(true);
pizza.setCor(Color.YELLOW);
pizza.setDirecao(Direcao.OESTE);
// Inimigos
inimigos = new Pizza[2];
inimigos[0] = new Pizza(0, 0, largEl, largEl);
inimigos[0].setVel(3 + Jogo.nivel);
inimigos[0].setAtivo(true);
inimigos[0].setCor(Color.RED);
inimigos[0].setDirecao(Direcao.OESTE);
inimigos[0].setModo(Pizza.Modo.CACANDO);
Primeiro,achamosoespa çodisponívelparanossoselementosnagradee
133
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 156

6.1. Caçafantasma CasadoCódigo
guardamosnavariável largEl.Nestecaso,dividimosalarguradatelapela
quantidadedecolunas,448divididopor28,resultandoem16pixels.
Emboraaalturadatelasejamaior(550px),agradeocupamenosespa ço
(496),quedivididopor31linhas,tambémresultaem16pixels.Porisso,usa-
mosessemesmovalortantoparalarguraquantoalturadospersonagens.
Nossopersonagemprincipal,carinhosamentechamadode pizza,co-
meçaativo,nacoramarela,movendo-separaaesquerda(Oeste).Paracon-
trolarosantagonistas,usamosumarray,chamado inimigos.Avelocidade
delesvariadeacordocomadificuldadeescolhidapelojogador.
inimigos[1] = new Pizza(0, 0, largEl, largEl);
inimigos[1].setVel(2 + Jogo.nivel);
inimigos[1].setAtivo(false);
inimigos[1].setCor(Color.PINK);
inimigos[1].setDirecao(Direcao.NORTE);
inimigos[1].setModo(Pizza.Modo.PRESO);
Emboraoprimeiroinimigo,nacorvermelha,comeceativoeca çando
nossojogadorpelatela,osegundo,nacorrosa,come çainativo,presoese
movemaislentamente.Todossãoiniciadosnaposi ção0,jáqueprecisaremos
percorreragradeparaobterasposi çõesiniciaisdecadaum:
for (int lin = 0; lin < grade.length; lin++) {
for (int col = 0; col < grade[0].length; col++) {
if (grade[lin][col] == Nivel.CN ||
grade[lin][col] == Nivel.SC) {
totalPastilha++;
} else if (grade[lin][col] == Nivel.PI) {
pizza.setPx(converteInidicePosicao(col));
pizza.setPy(converteInidicePosicao(lin));
} else if (grade[lin][col] == Nivel.P1) {
inimigos[0].setPx(converteInidicePosicao(col));
inimigos[0].setPy(converteInidicePosicao(lin));
} else if (grade[lin][col] == Nivel.P2) {
inimigos[1].setPx(converteInidicePosicao(col));
134
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 157

CasadoCódigo Capítulo6. Pac-Man,vulgoCome-come
inimigos[1].setPy(converteInidicePosicao(lin));
} else if (grade[lin][col] == Nivel.PF) {
pontoFugaCol = col;
pontoFugaLin = lin;
} else if (grade[lin][col] == Nivel.PV) {
pontoVoltaCol = col;
pontoVoltaLin = lin;
}
}
}
Aproveitamostambémparasomaraquantidadetotaldepastilhasque
nossojogadorterádecomerparaganharojogo,alémdeguardarmosalinha
ecolunadopontodefugaepontodevolta,queservemdebússolaparanossos
inimigossaíremevoltaremparaprisão. Observequeutilizamosafun ção
converteInidicePosicao,issoparasuavizaramovimenta çãodosnossos
personagens,poiselesmovem-senoseixosalgunspixelsporvez,enãoem
linha/coluna,comonoTetris.
Issoseriamaissimplesseosoutroselementosdojogo(comopastilhase
blocos)nãoestivessemfixosemsuaslinhasecolunas. Logo,paraissofun-
cionarcorretamente,temostambémafun ção convertePosicaoIndice,
masnãosepreocupe,elasrealmentenãopossuemnenhummistério:
private int converteInidicePosicao(int linhaColuna) {
return linhaColuna * largEl;
}
private int convertePosicaoIndice(int eixoXY) {
return eixoXY / largEl;
}
Aprimeiraconverteumíndice,posi çãodalinhaoucolunadoarray,em
eixoXouY.Asegunda,oinverso,umeixoXouYemíndice.Valelembrar
queXequivaleàcoluna,eYàlinha.Exemplificando,sequisermossaberqual
aposiçãoXdopersonagemnacoluna21,multiplicamos21pelotamanhoque
135
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 158

6.1. Caçafantasma CasadoCódigo
cadaespaçodagradeocupanatela(16),entãoXserá336.Omesmoparaa
linhaeoeixoY.
Agora,seestivermosnoeixoY250,alinhaequivalenteseria250divi-
didopor16,nestecaso15.Notequeesseresultadoseria15,625seestivéssemos
trabalhandocom floatemvezde int,e16casoarredondássemoscom
Math.round,masestenãoéocaso.Esperamosqueovalorsejarealmente
15,nemmais,nemmenos.
Ditoisso,podemos atualizarojogo,lembrandodequenossosperso-
nagenssópodemiremumadasquatrodire çõesenquantosemovem.
if (Jogo.controleTecla[Jogo.Tecla.ESQUERDA.ordinal()]) {
prxDirecao = Direcao.OESTE;
} else if (Jogo.controleTecla[Jogo.Tecla.DIREITA.ordinal()]) {
prxDirecao = Direcao.LESTE;
} else if (Jogo.controleTecla[Jogo.Tecla.CIMA.ordinal()]) {
prxDirecao = Direcao.NORTE;
} else if (Jogo.controleTecla[Jogo.Tecla.BAIXO.ordinal()]) {
prxDirecao = Direcao.SUL;
}
pizza.setDirecao(prxDirecao);
Guardamosadire çãoescolhidapelojogadornavariável prxDirecao,
convertendoateclapressionadaempontocardeal.Issoéfeitoparaajudarna
jogabilidade( gameplay),nãoobrigandoojogadoraacertaromomentoexato
emqueopersonagempoderáirnadire çãoescolhida.Porexemplo,seoper-
sonagemestiversemovendonahorizontaleojogadorpressionarparacima,
casoopersonagempossairnestadire çãonãohaveránenhumproblema,caso
contrário,jásabemosparaondeojogadorqueriretentaremosnovamenteaté
termosumamovimenta çãoválidaouojogadorescolheroutradire ção. As-
simnãodeixamosojogadorexecutarummovimentoinválidosemobrigá-lo
aexecutaromovimentonomomentoexato.
Issoficaacargodométodo atualizarDirecao,queverificaseojoga-
dorrealmentepodeirnadire çãoescolhida.
Aindaprecisamoscorrigirsuaposi ção–jáqueaosairdatelapelolado
esquerdoospersonagensaparecemnoladodireitoevice-versa–, verifi-
car se personagem andou se alimentando e, só então, chamar o método
atualizar.
136
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 159

CasadoCódigo Capítulo6. Pac-Man,vulgoCome-come
atualizaDirecao(pizza);
corrigePosicao(pizza);
comePastilha(pizza);
pizza.atualiza();
if (superPizza && temporizadorPizza > 200) {
temporizadorPizza = 0;
superPizza(false);
} else
temporizadorPizza += 1;
Seojogadorcomerapastilhaespecial,elesetransformanosuperpizza,
entãousamosumtemporizadorparacontrolarotempoemqueojogador
ficaráinvulnerável.
Chamamos superPizza(true) para transformá-lo, e
superPizza(false) para voltá-lo ao normal. Depois de tudo isso,
passamosparaosinimigos.
for (Pizza el : inimigos) {
if (el == null)
continue;
atualizaDirecaoInimigos(el);
corrigePosicao(el);
el.atualiza();
if (Util.colide(pizza, el)) {
if (el.getModo() == Pizza.Modo.CACANDO) {
reiniciar(); // Jogador perdeu
} else if (el.getModo() == Pizza.Modo.FUGINDO) {
el.setAtivo(false);
el.setModo(Pizza.Modo.FANTASMA);
pontos += 50;
}
}
}
Ométodoqueatualizaadire çãodojogadorédiferentedoqueatualiza
137
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 160

6.1. Caçafantasma CasadoCódigo
adireçãodosinimigos,afinal,ojogadorsóprecisaindicarparaondequer
ir. Entretanto,osinimigosprecisamdeumpoucodeInteligênciaArtificial,
comoveremosmaisàfrente.Porfim,quandoocorreumacolisãodoinimigo
comojogador,verificamosseoinimigoestavaca çandoojogador(eleentra
nessemodoquandoatingeopontodefuga),ouseestavafugindodele–nesse
caso,oinimigoestavaca çandoojogadorquandoestevirousuperpizza.
Quandooinimigoestáca çando,acolisãonãoresultanaperdadojogo,
todosospersonagensapenasvoltamparasuasposi çõesiniciais. Agora,se
oinimigoestavafugindo,eleviraumfantasmaque,emvezdeperseguiro
jogador,buscaopontodevoltaeojogadorganhamaispontos.
Quandoatualizamosadire çãodosnossospersonagens,precisamosvali-
daradire çãoetambémamovimenta çãodeles.Entãoveremosessesmétodos
primeiro,começandopelo validaDirecao,queapenaschamaométodo
validaMovimentocomosvalorescorrespondentesàdire çãoescolhida.
private boolean validaDirecao(Direcao dir, Pizza el) {
if (dir == Direcao.OESTE && validaMovimento(el, -1, 0))
return true;
else if (dir == Direcao.LESTE && validaMovimento(el, 1, 0))
return true;
else if (dir == Direcao.NORTE && validaMovimento(el, 0, -1))
return true;
else if (dir == Direcao.SUL && validaMovimento(el, 0, 1))
return true;
return false;
}
Sabendoparaqualdire çãoojogadorquerir,precisamostransformaressa
direçãonamovimenta çãopropriamentedita,porexemplo,Oesteequivaleà
esquerda,queequivaleasubtrairaposi çãodoelementonoeixoX.
Então,considerandoqueadire çãoescolhidafoiOeste,estamosvalidando
omovimentoutilizando-1emX,0paraYeavelocidadeparasaberquantos
138
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 161

CasadoCódigo Capítulo6. Pac-Man,vulgoCome-come
pixelsopersonagemvaisemover(nadire çãoquefordiferentedezero).
Seguindoamesmalógicaparaasdemaisdire ções,emborasomando1no
lugardesubtrairparadire çãoLestee,paraNorteeSul,subtraindoesomando
1emYrespectivamente,deixando0emX.
Setudoquevimosatéagorapareciasimples,nossopróximométododes-
toadorestantedocódigo,pelomenosàprimeiravista.Paravalidaromovi-
mento,precisamosdetectaracolisãodosnossoselementoscomosvaloresna
gradee,assimcomoadetec çãodecolisãoentreelementos,precisamoslevar
emcontaaposi çãoeotamanhodeles.
private boolean validaMovimento(Pizza el, int dx, int dy) {
// Próxima posição x e y
int prxPosX = el.getPx() + el.getVel() * dx;
int prxPosY = el.getPy() + el.getVel() * dy;
// Coluna e linha
int col = convertePosicaoIndice(prxPosX);
int lin = convertePosicaoIndice(prxPosY);
// Coluna + largura e linha + altura
int colLarg = convertePosicaoIndice(prxPosX +
el.getLargura() - el.getVel());
int linAlt = convertePosicaoIndice(prxPosY +
el.getAltura() - el.getVel());
Estamosvalidandoomovimentoqueaindanãoocorreu,entãoprecisa-
mossimularaposi çãofuturadoelemento.Paraisso,énecessárioteraposi ção
doelementomaisavelocidade(quantidadedepixelsaseremincrementados)
multiplicadapeladire ção(-1,0ou1).
Convertemosaposi çãofuturaemcolunaelinhaparasaberaposi çãodo
elementonagrade,masissonãoéosuficiente. Quandoopersonagemse
moveparaesquerdaouparabaixo,precisamoslevaremcontaseutamanho
paraacharmosacolunaelinhacorretas.Logo,somamosapróximaposi ção
noeixoXàlarguradoelemento,subtraindoavelocidade,quejáestáembutida
em prxPosX.Assim,acharemosacolunacorretadoelementoquandoele
estiversemovendoparadireita,oequivalenteparao prxPosYealturado
elementosemovendoparabaixo.
139
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 162

6.1. Caçafantasma CasadoCódigo
if (foraDaGrade(col, lin) || foraDaGrade(colLarg, linAlt))
return true;
if (grade[lin][col] == Nivel.BL ||
grade[lin][colLarg] == Nivel.BL ||
grade[linAlt][col] == Nivel.BL ||
grade[linAlt][colLarg] == Nivel.BL) {
return false;
}
Comoospersonagenspodematravessardeumladoparaooutrodolabi-
rintoaosaíremdatela,enessemomentoelesestarãoforadoarray,usamosa
função foraDaGradeparaverificarseissoocorreu–nestecaso,retornamos
verdadeiro,interrompendoavalida çãoparaqueelesnãoparemnomeiodo
caminho.
Seelenãoestiverforadagrade,verificamosseopersonagemcolidiucom
algumbloco,sejaindoparacimaeparaesquerda,paracimaeparadireita,
parabaixoeparaesquerda,ouparabaixoeparadireita.
Oquechamamosdelinha( Nivel.LN)écomosefosseumblocoespecial
ondeosinimigossópodematravessarseestivereminativosounãoestiverem
presos( Modo.PRESO).
// Validar linha branca
if (el.isAtivo() || el.getModo() == Modo.PRESO) {
if (grade[lin][col] == Nivel.LN ||
grade[lin][colLarg] == Nivel.LN ||
grade[linAlt][col] == Nivel.LN ||
grade[linAlt][colLarg] == Nivel.LN) {
return false;
}
}
return true;
}
Apenas repetimos a mesma verificação, trocando Nivel.BL por
Nivel.LN,paraqueosinimigosativoseatémesmoojogadornãoentrem
acidentalmentenajaula.Senãohouvercolisão,retornamos true,indicando
140
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 163

CasadoCódigo Capítulo6. Pac-Man,vulgoCome-come
queomovimentoéválido.Comessesmétodosemmente,chegouahorade
vermoscomoojogofunciona.
6.2 J ogando o código
Nossojogotemtrêspersonagens:nossoheróirepresentadoporumcírculo
amareloedoisinimigos,umvermelhoeumrosa. Cadapersonagemtem
suaposiçãoinicialdefinidanopróprionível,mesmoassimosdeixamosnas
posiçõessemelhantesaojogooriginal.Oinimigovermelhocome çaforada
jaula,jáoinimigorosacome çapresoedemoraumpoucoparaselibertar.
Paranossoheróiganharojogo,eletemdecomertodasaspastilhasda
tela.Porém,nãoadicionamosumfimdejogo.Aoserpegoporumfantasma,
apenasreiniciamosasposi çãodonossoheróiedeseusinimigos.
Essessãoapenasosaspectosbásicosdojogo,quequalquerjogadorcon-
segueperceber. Oqueficaporbaixodospanos,quenós,desenvolvedores,
conseguimosver,ébemmaisinteressante,comoporexemplo,ofluxodeati-
vidadesquenossosinimigosseguem:
141
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 164

6.2. Jogandoocódigo CasadoCódigo
Fig.6.4:Fluxofantasma
Emcadaumdessesseisestadosquenossosinimigospodemter,eleses-
tarãopreocupadoscomcoisasdiferentes,entãocadaestadotemumtoquede
inteligência,mesmoquesejaartificial.Porisso,teremosumase çãoprópriasó
parafalarmosdisso,masantes,veremosmaisaspectosrelacionadosaonosso
herói.
Podeocorrerdavelocidadequevocêdefinirparaalgumpersonagemaca-
barposicionando-oemumlocalinadequadodatela,comumadistânciaper-
ceptíveldaparedeouumpoucodentrodela,porexemplo. Paraevitarisso
egarantirquenossospersonagenspossamsairdaáreavisíveldatela(sendo
posicionadosdoladooposto),utilizamosumaúnicafun ção.
private void corrigePosicao(Pizza el) {
int novaPx = el.getPx(); // Nova posição x
int novaPy = el.getPy(); // Nova posição y
142
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 165

CasadoCódigo Capítulo6. Pac-Man,vulgoCome-come
int col = convertePosicaoIndice(el.getPx()) * largEl;
int lin = convertePosicaoIndice(el.getPy()) * largEl;
if (el.getDx() == 0 && novaPx != col)
novaPx = col;
else if (el.getPx() + largEl < 0)
novaPx = largura;
else if (el.getPx() > largura)
novaPx = -largEl;
Euchamariaessafun çãodeteleportesemproblemas,masaprimeirave-
rificaçãoéparasabermosseoelementonãoestásemovendonavertical(eixo
X).Assim,oresultadodavalida çãodecolisãopodetê-loposicionadoforados
16pxdeespa çamentodecadacolunae,seissoacontecer,definimosanova
posiçãocomovalordaposi çãodacolunamaispróximaparaenquadrá-lona
grade.
Depois,verificamosseopersonagemsaiutotalmentedatela,fazendoos
personagensseteletransportaremdeumladoparaooutro. Emboranosso
labirintonãotenhasaídashorizontais,deixamosummétodoequivalentepara
oteleportenoeixoY,casoprecise.
if (el.getDy() == 0 && novaPy != lin)
novaPy = lin;
else if (el.getPy() + largEl < 0)
novaPy = altura;
else if (el.getPy() > altura)
novaPy = -largEl;
el.setPx(novaPx);
el.setPy(novaPy);
}
Porfim,atualizamosasposi çõesdoelementoemseusrespectivoseixos.
Valenotarquesomamosesubtraímosovalordavariável largElporser
equivalenteaotamanhodoelemento. Muitoparecidocomnossométodo
paraverificarseopersonagemsaiudatela:
private boolean foraDaTela(Elemento el) {
if (el.getPx() < 0 || el.getPx() + el.getLargura() > largura)
143
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 166

6.2. Jogandoocódigo CasadoCódigo
return true;
if (el.getPy() < 0 || el.getPy() + el.getAltura() > altura)
return true;
return false;
}
Ecomoestamostrabalhandotambémcomaposi çãodopersonagemem
colunaelinha:
private boolean foraDaGrade(int coluna, int linha) {
if (linha < 0 || linha >= grade.length)
return true;
if (coluna < 0 || coluna >= grade[0].length)
return true;
return false;
}
Doismétodosjáconhecidos,vistosemoutroscapítulos.Aprincipalati-
vidadedonossopersonagemésealimentare,paraisso,precisamosverificar
seelecolidiucomalgumapastilha,convertendosuasposi çõesnoeixoXeY
emcolunaelinha.
private void comePastilha(Elemento el) {
int col = convertePosicaoIndice(el.getPx());
int lin = convertePosicaoIndice(el.getPy());
if (foraDaGrade(col, lin)) {
return;
}
if (grade[lin][col] == Nivel.CN ||
grade[lin][col] == Nivel.SC) {
pontos += grade[lin][col] == Nivel.CN ? 5 : 25;
totalPastilha--;
144
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 167

CasadoCódigo Capítulo6. Pac-Man,vulgoCome-come
if (totalPastilha == 0)
estado = JogoCenario.Estado.GANHOU;
else if (grade[lin][col] == Nivel.SC)
superPizza(true);
grade[lin][col] = Nivel.EV;
}
}
Seojogadorestiveremumaposi çãoválidanagradeeestacoincidircom
umapastilhanormal(quevale5pontos),oucomumasuperpastilha(quevale
25),somamosospontosedecrementamosototaldepastilhasdisponíveis.
Seelasacabarem,eleganhaojogo;senãotiveremacabadoaindaeforuma
superpastilha,eleentraemmodosuper. Oespa çoocupadopelapastilhaé
substituídoporumespa çovazio.
Nossoheróitemsomentedoismodosdejogo:normalesuper.Elecome ça
nomodonormale,aocomerumasuperpastilha,entraemmodosuperpor
algunssegundose,então,voltaaomodonormalquandoestetempoacaba–
emboraessamudan çadenormalparasuperesuperparanormalnãoaltereo
estadodonossoherói.
private void superPizza(boolean modoSuper) {
superPizza = modoSuper;
temporizadorPizza = 0;
for (Pizza el : inimigos) {
if (el == null)
continue;
if (modoSuper && el.getModo() == Pizza.Modo.CACANDO)
el.setModo(Pizza.Modo.FUGINDO);
else if (!modoSuper && el.getModo() ==
Pizza.Modo.FUGINDO)
el.setModo(Pizza.Modo.CACANDO);
}
}
Usamosomesmométodoparafazerojogadorentraresairdomodosu-
per.Usamos superPizzae temporizadorPizzaparacontrolarotempo
145
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 168

6.2. Jogandoocódigo CasadoCódigo
emqueojogadorficaránessemodo. Apenasoestadodoinimigoélevado
emconsideraçãoquandodetectarmoscolisãoentreelesenossoherói. Isso
porquepodehavercolisãocomosinimigosemdiferentesestados(quando
elesviramfantasmas,porexemplo)epodeacontecerquemesmoeleestando
comomodosuperativo,oinimigojátenhaserecuperadoevoltadoàca ça.
Passandoverdadeiro,eleentranomodosupereosinimigosficamvul-
neráveis;passandofalso,elesaidessemodo,ficandovulnerávelaosinimigos.
Emtodocaso,otemporizadorézerado,sendoquesomenteosinimigosque
estãoca çandooufugindoserãoafetadosporessamudan ça.
Jáusamosdoisinteirospararepresentaradire çãodoelementonosei-
xosXeYantes,masagora,alémde dxe dy,temostambémumavariável
direcao,querepresentaNorte,Sul,OesteeLeste.Ojogadorpodeescolher
irparaqualquerumadessasdire ções,masnossopersonagemsóacataráessa
decisãonomomentocerto.Assim,adire çãoemqueopersonagemestáindo
nemsempreseráadire çãoqueojogadorescolheu,maselanãoéignorada.
Todavezqueatualizamosojogo,verificamosseconseguimosatenderodesejo
dojogador.
private void atualizaDirecao(Pizza el) {
if (foraDaTela(el))
return;
// Temporario Direcao X e Y
int tempDx = el.getDx();
int tempDy = el.getDy();
Direcao direcao = el.getDirecao();
if (validaDirecao(direcao, el)) {
if (direcao == Direcao.OESTE)
tempDx = -1;
else if (direcao == Direcao.LESTE)
tempDx = 1;
if (direcao == Direcao.NORTE)
tempDy = -1;
146
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 169

CasadoCódigo Capítulo6. Pac-Man,vulgoCome-come
else if (direcao == Direcao.SUL)
tempDy = 1;
}
if (!validaMovimento(el, tempDx, tempDy))
tempDx = tempDy = 0;
el.setDx(tempDx);
el.setDy(tempDy);
}
Antesdeatualizarmosadire çãodojogador,verificamosseopersonagem
nãoestáforadatela,oquequerdizerqueeleentrounotúneleaparecerádo
seuladooposto.Assim,elenãoteráachancedefugirdolabirinto,quebrando
ojogo.Sópodemostrocaradire çãodopersonagemseelaforválida,eessa
verificaçãoéopapeldo validaDirecao.
Tendoumadireçãoválida,atualizamososvaloresde tempDxe tempDy,
queserãorealmenteosvaloresutilizadosnamovimenta çãodospersonagens.
Porisso,independentementedeterumadire çãoválidaounão,precisamos
validarseumovimento( validaMovimento). Senãotivermosummovi-
mentoválido,zeramosambasasvariáveis,fazendoopersonagemparardese
moveratéqueojogadorindiqueumanovadire çãoválida.
O método validaDirecao utiliza internamente o método
validaMovimento, apenas convertendo ponto cardeal em eixo. Em-
bora à primeira vista essas validações pareçam complexas, basicamente
colocamosospersonagensnaposi çãofuturaeverificamossenãoacabaram
dentrodeumaparede. Valelembrarquenossospersonagenssópodemse
movernahorizontal(Oeste,LesteoueixoX)ounavertical(Norte,Sulou
eixoY).
Jámencionamosque,quandonossojogadorépegoporuminimigo,rei-
niciamosseusestadosesuasposi ções.
public void reiniciar() {
superPizza = false;
temporizadorFantasma = 0;
prxDirecao = Direcao.OESTE;
147
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 170

6.2. Jogandoocódigo CasadoCódigo
pizza.setDirecao(Direcao.OESTE);
inimigos[0].setDirecao(Direcao.OESTE);
inimigos[0].setModo(Pizza.Modo.CACANDO);
inimigos[0].setAtivo(true);
inimigos[1].setDirecao(Direcao.NORTE);
inimigos[1].setModo(Pizza.Modo.PRESO);
inimigos[1].setAtivo(false);
Desabilitamosomodosuperdonossoheróiedeixamostodoscomose
tivéssemosacabadodecarregarojogo.Depois,achamosnovamentesuaspo-
siçõesiniciaisnagrade.
for (int lin = 0; lin < grade.length; lin++) {
for (int col = 0; col < grade[0].length; col++) {
if (grade[lin][col] == Nivel.PI) {
pizza.setPx(converteInidicePosicao(col));
pizza.setPy(converteInidicePosicao(lin));
} else if (grade[lin][col] == Nivel.P1) {
inimigos[0].setPx(converteInidicePosicao(col));
inimigos[0].setPy(converteInidicePosicao(lin));
} else if (grade[lin][col] == Nivel.P2) {
inimigos[1].setPx(converteInidicePosicao(col));
inimigos[1].setPy(converteInidicePosicao(lin));
}
}
}
}
Paraevitarpercorrertodooarraynovamente,poderíamosterguardado
asposiçõesdospersonagensemcadaelemento,masnãohánenhumanovi-
dadeaqui. Passamos,então,paraométodo desenhar,quedesenhatanto
osvaloresdagradequantonossosobjetos Pizza.
for (int lin = 0; lin < grade.length; lin++) {
for (int col = 0; col < grade[0].length; col++) {
148
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 171

CasadoCódigo Capítulo6. Pac-Man,vulgoCome-come
int valor = grade[lin][col];
if (valor == Nivel.BL) {
g.setColor(superPizza ? Color.DARK_GRAY :
Color.BLUE);
g.fillRect(col * largEl, lin * largEl + ESPACO_TOPO,
largEl, largEl);
} else if (valor == Nivel.CN) {
g.setColor(Color.WHITE);
g.fillRect(col * largEl + espLinha,
lin * largEl + espLinha + ESPACO_TOPO,
largEl - espLinha * 2,
largEl - espLinha * 2 );
} else if (valor == Nivel.SC) {
g.setColor(Color.WHITE);
g.fillRect(col * largEl + espLinha / 2,
lin * largEl + espLinha / 2 + ESPACO_TOPO,
largEl - espLinha,
largEl - espLinha);
} else if (valor == Nivel.LN) {
g.setColor(Color.WHITE);
g.fillRect(col * largEl,
lin * largEl + espLinha + ESPACO_TOPO,
largEl, largEl - espLinha * 2);
}
}
}
Nemtodososvalorescontidosnagradeserãodesenhados. Osblocos
queformamnossolabirintosãodesenhadosnacorazul,quandonossoper-
sonagemestánomodonormale,nacorcinzaescuro,paraindicarquenosso
personagementrounomodosuper.
Nacorbranca,temosnossaspastilhasesuperpastilhas,quetêmtama-
nhosdiferenteseocupammenosespa çoqueobloco,ealinhaporondeos
fantasmasentramesaemdaprisão.
149
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 172

6.2. Jogandoocódigo CasadoCódigo
Todososdesenhoslevamemconsidera çãooespa çamentosuperior,so-
mando ESPACO_TOPO.
Dica
Consideramosoespa çamentoapenasnapinturadodesenho. Isso
querdizerqueaposi çãooriginaldoselementosnãoéalterada.
Outraop çãoseriaaplicaresseespa çamentonasposi çõesdosele-
mentos,masnestecasoficariamaiscomplicadanossaintera çãocoma
grade,queéumarray.
Essaénossagradecomsuasbordasnacorbranca:
Fig.6.5:Grade
Sóparanãoesquecer,dentrodométodo desenhar,aindatemosque
exibirospontosdojogadoreospersonagensdojogo.
texto.desenha(g, "Pontos: " + pontos, 10, 20);
pizza.desenha(g);
for (Elemento el : inimigos) {
if (el == null)
continue;
el.desenha(g);
}
150
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 173

CasadoCódigo Capítulo6. Pac-Man,vulgoCome-come
Paratrazerumbomdesafioaojogador,nãobastaenchernossolabirinto
deinimigos.Precisamosqueelestenhaminteligênciasuficienteparasaíreme
voltaremparaacela,queelessaibamquandoiratrásdonossoheróiequando
fugirdele.Garanto-lhequeessanãoseráumatarefatrivial,emborafa çamos
tudoemumúnicométodo.
6.3 U m pouco de I.A. não faz mal
AInteligênciaArtificial(Artificial Intelligenceou AI)nosjogosnãoprecisaser
realmenteinteligente,mascomcertezaprecisapassaraimpressãodeser.Al-
gumasvariamdeacordocomoníveldojogador,outrassimplesmentetentam
serimpiedosasetemcasosemqueelaapenassegueumpadrão.
Seojogotiverpersonagensnãojogáveis( non-player charactersou NPCs),
umaboaIAsetornavital.QuemnuncateveraivadeumNPCburro?
AIAéaplicadaemdiversasáreasdaprograma çãoe,mesmofocandoso-
mentenasqueestãopresentesnosjogos,aindaassimprecisaríamosdeum
livrooumais,umavezquesuaaplica çãoincluidiversostópicos,como:to-
madadedecisão,movimenta ção,estratégia,aprendizadoemuitomais.Além
dealgoritmosespecíficosparadeterminadostiposdejogos,sejaumjogode
corridaouumdetabuleiro.Vocêpodevermaissobreoassuntonolivro Ar-
tificial Intelligence for games,deIanMillingtoneJohnFunge.
Aprincipaldiferen çaentreosinimigosdessejogoemrela çãoaosquejá
programamosnoscapítulosanterioreséqueseelesficaremsemovendoa
esmo,elespodem,alémdeficarempresos,nãoapresentarnenhumaamea ça
paraojogador,deixandoojogochato. Então,elesprecisamterperspicácia
suficienteparaperseguiremojogadoroufugiremdele,semprerespeitando
asregrasdojogo,issoé,sematravessarparedesoucoisadotipo.
Oqueveremosaseguiréumaversãomuito(masmuito)simplificada
de path finding,algodotipo“procurandoocaminho”.Sevocêficoucurioso
equersabermais,entreemhttp://qiao.github.io/PathFinding.js/visual. Lá,
vocêencontraumaversãobemlegalondepodetestardiferentesalgoritmos.
Parasimplificarascoisas,ocódigoficousegmentandoemcadaumdos
estadosquenossosantagonistaspodemter, comexce çãodosestadosca-
çandoefugindo. Mesmogerandocertarepeti ção,essasepara çãonosper-
151
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 174

6.3. UmpoucodeI.A.nãofazmal CasadoCódigo
mitetestareentendermelhorcadatrecho. Tudodentrodonossométodo
atualizaDirecaoInimigos,quecome çaassim:
if (foraDaTela(el))
return;
int col = convertePosicaoIndice(el.getPx());
int lin = convertePosicaoIndice(el.getPy());
Direcao direcao = el.getDirecao();
// Variáveis auxiliares
Direcao tempDir = null;
int tempDx = 0, tempDy = 0;
int xCol = 0, yLin = 0;
Nojogooriginal,umfantasmacome çaforadajaulaeoutrostrêscome-
çampresos.Então,usamossomentedoisnestejogo,umemcadamodo.
if (el.getModo() == Pizza.Modo.PRESO) {
if (el.getDirecao() == Direcao.SUL &&
!validaDirecao(Direcao.SUL, el))
el.setDirecao(Direcao.NORTE);
else if (el.getDirecao() == Direcao.NORTE &&
!validaDirecao(Direcao.NORTE, el))
el.setDirecao(Direcao.SUL);
else if (el.getDirecao() != Direcao.NORTE &&
el.getDirecao() != Direcao.SUL)
el.setDirecao(Direcao.NORTE);
if (temporizadorFantasma > 50)
el.setModo(Pizza.Modo.ATIVO);
else
temporizadorFantasma++;
Oinimigoestápreso,masnãoimóvel,eleandanadire çãoNorteaténão
podermais,entãotrocaparaadire çãoopostaaténãopodermaistambém.
152
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 175

CasadoCódigo Capítulo6. Pac-Man,vulgoCome-come
Casoadire çãonãosejanemNorte,nemSul,elaédefinidacomoNorte,utili-
zandoumtemporizadorparasaberquandomudaroestadodoinimigopara
queelesaiadaprisão.
} else if (el.getModo() == Pizza.Modo.ATIVO) {
xCol = pontoFugaCol;
yLin = pontoFugaLin;
int colLarg = convertePosicaoIndice(el.getPx() +
el.getLargura() - el.getVel());
int linAlt = convertePosicaoIndice(el.getPy() +
el.getAltura() - el.getVel());
if (lin > yLin && validaDirecao(Direcao.NORTE, el))
el.setDirecao(Direcao.NORTE);
else if (lin < yLin && validaDirecao(Direcao.SUL, el))
el.setDirecao(Direcao.SUL);
else if (col < xCol && validaDirecao(Direcao.LESTE, el))
el.setDirecao(Direcao.LESTE);
else if (col > xCol && validaDirecao(Direcao.OESTE, el))
el.setDirecao(Direcao.OESTE);
else if (col == xCol && lin == yLin &&
colLarg == xCol && linAlt == yLin) {
el.setAtivo(true);
el.setModo(Pizza.Modo.CACANDO);
}
Primeiro, achamos a saída, cujas posições foram guardadas em
pontoFugaCole pontoFugaLin,depoisverificamosseopersonagemestá
nalinhadecimaoudebaixoemrela çãoàlinhadopontodefuga,movendo-o
nadireçãoNorteouSulatéelechegaromaispróximopossível,entãofazemos
omesmoparaLesteeOeste.
Quandofinalmenteeleseposicionacompletamentenamesmalinhaeco-
lunadopontodefuga(paraisso,comparamosnãosomenteaposi ção,mas
153
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 176

6.3. UmpoucodeI.A.nãofazmal CasadoCódigo
tambémlarguraealtura),eleficaativoeprontoparaca çarnossojogadorou
fugirdele.
} else if (el.getModo() == Pizza.Modo.CACANDO ||
el.getModo() == Pizza.Modo.FUGINDO) {
xCol = convertePosicaoIndice(pizza.getPx());
yLin = convertePosicaoIndice(pizza.getPy());
// Inverte posição para fugir
if (el.getModo() == Pizza.Modo.FUGINDO) {
xCol = xCol * -1;
yLin = yLin * -1;
}
boolean perdido = rand.nextInt(100) == 35;
if (el.isAtivo() && perdido) {
tempDir = sorteiaDirecao();
} else if (direcao == null) {
direcao = sorteiaDirecao();
} else if (direcao == Direcao.NORTE ||
direcao == Direcao.SUL) {
if (xCol < col && validaDirecao(Direcao.OESTE, el))
tempDir = Direcao.OESTE;
else if (xCol > col && validaDirecao(Direcao.LESTE, el))
tempDir = Direcao.LESTE;
} else {
/* direcao = OESTE ou LESTE */
if (yLin < lin && validaDirecao(Direcao.NORTE, el))
tempDir = Direcao.NORTE;
else if (yLin > lin && validaDirecao(Direcao.SUL, el))
tempDir = Direcao.SUL;
}
if (tempDir != null && validaDirecao(tempDir, el))
154
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 177

CasadoCódigo Capítulo6. Pac-Man,vulgoCome-come
el.setDirecao(tempDir);
else if (!validaDirecao(el.getDirecao(), el))
el.setDirecao(sorteiaDirecao());
Aúnicadiferençaentreoinimigofugindoeoinimigoca çandoéque,no
primeiromodo,elevaiemdire çãoaojogador;jánosegundo,eleobtéma
direçãodojogadoreinverte-a,indonadire çãooposta.
Paraosinimigosnãoacabaremfazendoomesmomovimento,unsdos
outros,ouacabarememumapersegui çãoimpiedosa,devezemquandofa-
zemosoinimigoirparaqualquerlado,comoseestivesseperdido.
Aprincipaldiferen çaaquiéqueelesnãoficamnamesmadire çãoatécoli-
diremcomumaparede,elesestãosempretentandomudardedire çãonomeio
docaminho,masnãoparaadire çãooposta;casocontrário,dependendoda
posiçãodojogador,elesacabariamsemsairdolugar.Quandochegamaum
becosemsaída,elesficamláatésortearemumadire çãoválida. Quandoo
jogadorentranomodosuperecolidecomoinimigo,transforma-oemum
fantasma.
} else if (el.getModo() == Pizza.Modo.FANTASMA) {
xCol = pontoFugaCol;
yLin = pontoFugaLin;
if (direcao == Direcao.NORTE || direcao == Direcao.SUL) {
if (xCol < col && validaDirecao(Direcao.OESTE, el))
tempDir = Direcao.OESTE;
else if (xCol > col && validaDirecao(Direcao.LESTE, el))
tempDir = Direcao.LESTE;
} else {
if (yLin < lin && validaDirecao(Direcao.NORTE, el))
tempDir = Direcao.NORTE;
else if (yLin > lin && validaDirecao(Direcao.SUL, el))
tempDir = Direcao.SUL;
}
if (tempDir != null && validaDirecao(tempDir, el))
el.setDirecao(tempDir);
else if (!validaDirecao(el.getDirecao(), el))
155
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 178

6.3. UmpoucodeI.A.nãofazmal CasadoCódigo
el.setDirecao(trocaDirecao(el.getDirecao()));
if (col == xCol && lin == yLin)
el.setModo(Pizza.Modo.INATIVO);
Nomodofantasma,oinimigonãooferecemaisperigoparaojogadore
temdevoltarparaaprisãoparaserecuperar(maisprecisamente,opontode
volta).Primeiro,eledevevoltaraopontodefuga,jáquedalisóprecisairem
linhareta,cruzaralinhabrancaechegaratéopontodevolta.
Paraisso,eleusapartedoalgoritmousadonapersegui çãodojogador,
massemficarseperdendonomeiodocaminho,sendoqueseeleacabarem
umaposiçãoinválidanavertical,eletrocaparaumadire çãonahorizontal.
Umavezquecruzandoalinhabranca,elevoltaaoseuaspectonormaleentra
nomodoinativo.
} else if (el.getModo() == Pizza.Modo.INATIVO) {
xCol = pontoVoltaCol;
yLin = pontoVoltaLin;
if (lin > yLin && validaDirecao(Direcao.NORTE, el))
el.setDirecao(Direcao.NORTE);
else if (lin < yLin && validaDirecao(Direcao.SUL, el))
el.setDirecao(Direcao.SUL);
else if (col < xCol && validaDirecao(Direcao.LESTE, el))
el.setDirecao(Direcao.LESTE);
else if (col > xCol && validaDirecao(Direcao.OESTE, el))
el.setDirecao(Direcao.OESTE);
else if (col == xCol && lin == yLin)
el.setModo(Pizza.Modo.PRESO);
}
Essaéamesmalógicadomodoativo,eocódigoquaseidêntico.Masem
vezdechegarnalinhaecolunadopontodefuga,estamosmirandonalinha
ecolunadopontodevoltae,umavezlá,oinimigovoltaaomodopreso,
iniciandonovamenteociclosemfim.
156
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 179

CasadoCódigo Capítulo6. Pac-Man,vulgoCome-come
Antesdeométodo atualizaDirecaoInimigosacabar,precisamos
atualizaradire çãodopersonagemcasoelasejaválida.
if (validaDirecao(el.getDirecao(), el)) {
if (el.getDirecao() == Direcao.NORTE)
tempDy = -1;
else if (el.getDirecao() == Direcao.SUL)
tempDy = 1;
else if (el.getDirecao() == Direcao.OESTE)
tempDx = -1;
else if (el.getDirecao() == Direcao.LESTE)
tempDx = 1;
}
el.setDx(tempDx);
el.setDy(tempDy);
Valenotarqueoalgoritmoparaoinimigosemoverlevaemconsidera ção
que,nolabirinto,elesópodeandarnoeixoXouY,masdentrodajaulaeletem
maisespaço. Devemoslevarissoemcontaparaelenãoacabarsemovendo
nadiagonal.Nãoesque çadeconsiderarissoaocriarseuspróprioslabirintos.
Osdoisúltimosmétodosauxiliaresqueprecisamosverrealmentenãofa-
zemnadademais.
private Direcao trocaDirecao(Direcao direcao) {
if (direcao == Direcao.NORTE)
return Direcao.OESTE;
else if (direcao == Direcao.OESTE)
return Direcao.SUL;
else if (direcao == Direcao.SUL)
return Direcao.LESTE;
else
return Direcao.NORTE;
}
private Direcao sorteiaDirecao() {
return Direcao.values()[rand.
nextInt(Direcao.values().length)];
}
157
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 180

6.4. Codificandoojogo CasadoCódigo
Oprimeirométodotrocaadire çãoseminvertê-la,apenaspassandoda
horizontalparaavertical,oudaverticalparahorizontal.Osegundoapenas
pegaumadire çãodeformaaleatória.Assim,abordamososprincipaispon-
tosdocódigodessejogoetalvez,depoisdisso,vocêpeguemaislevecomo
desenvolvedorquandoderdecaracomumbugdeIA.
6.4 C odificando o jogo
Temosbastantecódigoaquiparaquenossoheróipossapercorrerseulabi-
rintoatrásdecomida,emaiscódigoparaqueelesejaperseguidoporseus
inimigos. Valelembrarqueumaversãoprontacomtrêsníveisdedificul-
dadesdiferenteslheesperaem:https://github.com/logicadojogo/fontes/tree/
master/Cap06.
Naclasse Jogo.java,apenasotamanhodatelamuda(448delargura
por550dealtura)emrela çãoaojogoanterior. Seguindoopadrão,todaa
lógicadojogoficouem JogoCenario.java.
Novasclasses Nivel.javae Pizza.javaforamcriadas,etemospou-
casmudançasem InicioCenario.java,quepermiteaojogadorescolher
omododejogo(fácil,normaledifícil).
Não fizemos aqui
• Terafamíliadequatrofantasmascompleta;
• Reiniciarocenárioaocomertodasaspastilhas;
• Criarumacópiadocenárioparanãoperderaconfiguraçãoinicial.
Melhore você mesmo
• Adicionarfrutasqueaumentemapontuaçãodojogador.
6.5 R esumo
Começamospelolabirinto,emboraeletenhasidocriadocombasenocódigo
jádiscutidonocapítulo4.Destavez,utilizamosmaisop çõescomvaloresque
158
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 181

CasadoCódigo Capítulo6. Pac-Man,vulgoCome-come
vãode0até9,guardadosemconstantes.
Carregamosojogadoreosinimigosemduasetapas:primeiroconfigu-
ramosaspectosbásicos,edepoispercorremosonívelembuscadasposi ções
iniciais,pontodefugaedevolta,comotambémsomamostodasaspastilhas
queojogadorterádecomerparaconcluirojogo.
Trabalhamoscomelementosemeixocolidindocomelementosnoarray,
convertendoíndiceemposi ção,eposi çãoemíndice. Parafacilitaramovi-
mentação,usamospontoscardeaisnadire çãodospersonagens. Aovalidar
suasmovimentações,temosdeconsideraraposi çãoeotamanhodeleseveri-
ficaracolisãonagrade,semelhanteàdetec çãodecolisãoentredoiselementos.
Vimosquenossosfantasmastêmseisestágiosduranteojogo:preso,ativo,
caçando,fugindo,fantasmaeinativo.Enossoherói,mesmoquetemporari-
amente,entranomodosuperpizza.Temospraticamenteumalgoritmopara
cadaestadodoinimigo,sejaparaelessaíremevoltaremparaacela,ouper-
seguiremefugiremdonossoherói.Mesmoassim,apenasarranhamosasu-
perfíciedoassuntosobreInteligênciaArtificial.
Mesmodepoisdetantocódigo,ojogonãoficoutãoparecidocomoorigi-
nalcomoesperávamos,porisso,faremosmelhoriaseusaremosimagenspara
deixarojogomaisbonito.Nãopercaopróximocapítulo!
159
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 182

E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 183

Capítulo7
Come-comeeosbitmaps
Atéagora,usamoscódigoparacriarnossosdesenhos,mastrabalharcomima-
gensmaiscomplexasedetalhadasexigiriamuitomaisprograma ção.Aforma
maisfácildeutilizarmosdesenhoscomplexosdentrodosnossosjogosécriá-
losusandoumaferramentaapropriada,porexemplo,Gimp,Photoshopou
Fireworks,eimportá-losdeumarquivoexternoparadesenhá-losnatela.
Nestecapítulo,trabalharemoscom:
• Imagens;
• Sprites;
• Tiles.
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 184

CasadoCódigo
Fig.7.1:Come-comecomimagens
OJavafacilitanossavidacomoobjeto javax.swing.ImageIcon,que
aceitadiversosformatoscomoBMP( Bitmap),JPGePNG,masutilizaremos
somenteoPNG( Portable Network Graphics),quesuportafundotransparen-
162
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 185

CasadoCódigo Capítulo7. Come-comeeosbitmaps
tes(canalalfa).
Aqui,faremosumjogotemático,eotemaescolhidoéomundodapizza,
ondenossoprotagonistaseráumapizzapropriamenteditaeseusinimigos
sãolegumes.Asbordassetranformaramemcanudos,aspastilhaspequenas
viraramazeitonaseasmaiores,pepperoni.
Comomantivemosasmesmasdimensõesdojogoanterior,asimagens
estãopequenas,epodesernecessárioapelarparaaimagina çãoparaconseguir
distinguirascoisas.
7 .1 U ma imagem v ale mais do que mil linhas de
código
Sprites e Tiles
Spriteéumaimagemqueagrupadiversasimagens,geralmentecom
amesmaalturaelargura,esãousadospararepresentaroestadodoper-
sonagemoucriaranima ções.
Tileéparecidocomosprite,massãousadosparamontarcenáriosou
objetosestáticosdojogo. Aspartesdeumtilepodemformarcenários
diferentesdependendodacombina ção,ouusandomaisoumenospartes
paraformarobjetoscomdiferentestamanhos.
RecomendoqueprocureimagensnoGoogleusandoasseguintespa-
lavras:“spritessonic”e“tilessupermariobros”.
Desenharimagensnonossojogoérealmentemuitofácil.Nósprecisamos
deumaimagem,umobjeto ImageIconechamarométodo drawImagedo
objeto Graphics2D.
ImageIcon azeitona = new ImageIcon("imagens/azeitona.png");
public void desenhar(Graphics2D g) {
g.drawImage(azeitona.getImage(), 10, 30, null);
}
163
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 186

7.1. Umaimagemvalemaisdoquemillinhasdecódigo CasadoCódigo
Paracarregarumarquivoexterno,precisamosdoseucaminho. Neste
caso,passamosocaminhorelativo,jáqueapasta imagensestánomesmo
diretóriodonossoprojeto,semelhanteàformacomocarregamosarquivos
deáudionocapítulo5.
Para desenhá-la na tela, usamos o métododrawImage, mas
poderíamos usar o método paintIcon do próprio ImageIcon:
azeitona.paintIcon(null, g, 10, 30) . Oprimeiroparâmetrodo
método drawImage é um objeto da classe abstrataImage, que o
ImageIconnosfornece.
Depois,temosasposi çõesemeixoondeaimagemserádesenhada. O
últimoparâmetroéumobjeto ImageObserver,quenãousaremosneste
livro,entãopassamos null.
O método paintIcon pede como primeiro argumento um objeto
Componentparausarcomo ImageObserver,depoisoobjeto Graphics
seguidopelasposi çõesnoseixos.Nosdoisexemplos,desenhamosaimagem
naposição10doeixoX,e30doeixoY.
Dica
Sequisertrabalhardiretamentecomoobjeto Image,podeusaro
java.awt.Toolkitparacarregá-las:
public void desenhar(Graphics2D g) {
Toolkit tk = Toolkit.getDefaultToolkit();
Image imagem = tk.getImage("imagens/azeitona.png");
g.drawImage(imagem, 0, 0, null);
}
Nossasimagens( azeitona.pnge pepperoni.png)têmomesmo
tamanho,18x18pixels,masaáreaqueaazeitonaocupadotamanhototalda
imagemédeapenasde8x8.Assim,ficamaisfácilparadesenhar,jáquenão
teremosdeconsiderarasdiferen çasdetamanho.
Valeacrescentarque18x18éotamanhodocorredorqueospersonagens
percorremnolabirinto.
164
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 187

CasadoCódigo Capítulo7. Come-comeeosbitmaps
Fig.7.2:Imagenssimples
Dessaforma,desenhamosasazeitonaseospepperonis.Quandofalamos
deumaúnicaimagememumarquivo,ésimplesassim,masquandoumar-
quivorepresentamaisdeumaimagem(umsprite),ocódigoficamaisinte-
ressante.Vejaumexemplonafigura:
Fig.7.3:Spritesimples
Essessãoosquatroestágiosdonossopersonagememumúnicoarquivo.
Seporacasoutilizarmosométodocitado,ojogadorveráessetremdepiz-
zasmas,emvezdisso,queremosqueelevejaumformatodepizzadecada
vez,dandoaimpressãodeanima ção. Parafazermosissodaformacorreta
esemprecisarusarváriasimagens,teremosdeusarummétododaclasse
Graphicsumpoucomaior:
public abstract boolean drawImage(Image img,
int dx1, int dy1, int dx2, int dy2,
int sx1, int sy1, int sx2, int sy2,
ImageObserver observer);
Essadeclaraçãodemétodoveiodiretodadocumenta ção,sendoqueos
quatroprimeirosinteiros( int)sãoreferentesaodestinodaimagemeos
quatroúltimosreferentesàimagemdeorigem.Emvezdereproduziraexpli-
caçãovindadaprópriadocumenta ção,vamosexplicarcomexemplos.
Paracomeçar,imagineosquatroprimeirosparâmetroscomoumamol-
duraondequeremosquenossaimagemapare çanatela.
165
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 188

7.1. Umaimagemvalemaisdoquemillinhasdecódigo CasadoCódigo
Fig.7.4:Moldura
Nestecaso,nossatelatem100pixelsdelarguraealtura,enossamoldura
50x50px. Usamososprimeirosparâmetrosparaposicionaredimensionar
amolduranatela,representadapeloquadradovermelho.Osdoisprimeiros
sãoaorigem,eosdoisúltimosodestinodoquadrado,enãoalarguraealtura.
Issoquerdizerquedevemoslevaremcontaasposi çõesiniciaisesomá-lasàs
posiçõesfinais.
Osquatroúltimossãoreferentesaospontosdeorigemetamanhonaima-
gem:
Fig.7.5:Marcaçãoderecorte
Asdimensõesdanossaimagem( sprite_simples.png)são: 300x
79px,enossoquadradoazultem79x79pxcomdeslocamentode10pixelsno
eixoX.Dessaforma,aplicamosumrecortenaimagem,jáquesomenteoque
estiverdentrodoquadradoserádesenhado.
Nossocódigopararecortaraimagemedesenhá-lanatelanoseixos15xe
20yficariaassim:
ImageIcon img = new ImageIcon("imagens/sprite_simples.png");
@Override
166
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 189

CasadoCódigo Capítulo7. Come-comeeosbitmaps
public void desenhar(Graphics2D g) {
g.drawImage(img.getImage(),
15, 20, 15 + 79, 20 + 79,
10, 0, 10 + 79, 0 + 79, null);
}
Observequesomamososvaloresusadosnodeslocamentoparadefiniras
posiçõesfinaisdamolduraedaimagem,tendocomoresultadoamoldurana
posição15x,20y,eaimagem10x,0y–ambascomlarguraealturade79px.
Fig.7.6:Resultadodorecorte
Emborapossaparecerconfusotantosparâmetros,usaremostantasvezes
essemétododuranteocapítuloquevocêacabaráseacostumado,assimes-
pero.Lembre-sedequetemosdoisparâmetrospararepresentarasposi ções
iniciaisdaimagem,edoispararepresentarasposi çõesdedestino,enãolar-
guraealtura.
Seesquecerdelevaremconsidera çãoasposi çõesiniciasnahoradedefinir
asposiçõesdedestino,achamadadométodoescalonaráaimagem(seelaficar
distorcida,vocêjásabeomotivo).
Umexemplopráticodissoéquandofazemosumasele çãocomomouse:
vocêclica,seguradefinindoasposi çõesiniciaisemoveomouseemqual-
querdireçãoparadefiniraposi çãodedestino.Avantagemdissonométodo
drawImageéquepodemosinverteraimagemsimplesmenteinvertendoos
parâmetros:
ImageIcon img = new ImageIcon("imagens/copo_mshake.png");
// Normal
g.drawImage(img.getImage(), 0, 0, 78, 138, 0, 0, 78, 138, null);
167
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 190

7.1. Umaimagemvalemaisdoquemillinhasdecódigo CasadoCódigo
// Invertido
g.drawImage(img.getImage(), 0, 0, 78, 138, 78, 0, 0, 138, null);
Naprimeirachamada,opontodeorigemé0,opontofinaldoeixoXé78
eoeixoYé138,tantonaposi çãodamolduraquantonadaimagem.
Nasegundachamadadométodo,invertemosasposi çõesiniciaisdoeixo
X,ficandocom78naorigeme0nafinal,espelhandoaimagem.
Fig.7.7:Imagemespelho
JáconsegueimaginaroqueaconteceriaseinvertêssemosoeixoY?Isso
mesmo,aimagemficariadepontacabe ça.
Masnãosepreocupe,esseseoutrosfeitosdosmétodosdedesenhodo
Javanãoserãousadosnestejogo,apenassentimosqueesseeraumpontoa
servisto.
Poroutrolado,ospritequeusaremosnojogoéumpoucomaior(emais
complicado). Elecontémasquatropizzasemtodasasdire çõesemqueo
jogadorpodeirduranteojogo:
168
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 191

CasadoCódigo Capítulo7. Come-comeeosbitmaps
Fig.7.8:Pizzaspraquetequero
Trabalharemoscomspritescomoseelesfossemumagradecomlinhase
colunas.Nestecaso,ospritedonossoheróitem4linhase4colunas.
Aprimeiraesegundalinhacorrespondemaomovimentodojogadorpara
adireita(Leste)eparaesquerda(Oeste). Aterceiraequartalinha,omovi-
mentoparacima(Norte)eparabaixo(Sul).
Enquantoojogadorestiveremmovimento,percorreremosascolunasdo
sprite,nalinhareferenteàdire çãoescolhida,animandoamovimenta çãodo
personagem.Vamosaoexemplo:
@Override
public void desenhar(Graphics2D g) {
ImageIcon img = new ImageIcon("imagens/sprite_pizza.png");
int coluna = 3;
int linha = 0;
int largMoldura = img.getIconWidth() / 4;
169
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 192

7.1. Umaimagemvalemaisdoquemillinhasdecódigo CasadoCódigo
int altMoldura = img.getIconHeight() / 4;
int largImg = largMoldura * coluna;
int altImg = altMoldura * linha;
g.drawImage(img.getImage(),
0, 0, largMoldura, altMoldura,
largImg, altImg, largImg + largMoldura,
altImg + altMoldura, null);
}
Utilizamosnossaimagem sprite_pizza.png,ondetemos4linhase
4colunas.Ascolunaselinhassãoreferenciadascomooíndicedeumarray,
começandono0.Aodefinir colunacomovalor3e linhacom0,carre-
garemosafiguradaúltimacolunadaprimeiralinha.
Mesmosabendoquetodasasfigurasdentrodospritetêmomesmota-
manho(28px),nãoutilizaremosvaloresfixos,assimficamaisfácilfazeralte-
raçõesnaimagem.
Paraacharmosalarguraealturadamoldura,bastadividirmosalargura
ealturadaimagem,obtidascom getIconWidth()e getIconHeight()
respectivamente,pelaquantidadetotaldelinhasecolunas.Eparaacharmos
aposi çãocorretadacolunaelinhaquequeremosdesenhar,multiplicamos
largMoldurapela coluna,e altMoldurapela linha.
Emtermosmaispráticos,nossospritetem112x112pixels,entãonóstemos
umamoldurade28x28pixels(112/4),queéotamanhodecadafigura.Nossa
colunacomeçanopixel84(28*3),nossalinhanopixel0(28*0),eterminam
em112(84+28)e28(0+28),respectivamente.
Mesmocomtantamatemática,aindanãoestamosconsiderandooposi-
cionamentonatela,masdestaformaficamaisfácilpegarpartedaimagem,
bastaalterarovalorde linhae coluna.
Aplicaremosumcódigosemelhanteemoutrasimagensdojogo:
170
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 193

CasadoCódigo Capítulo7. Come-comeeosbitmaps
Fig.7.9:Olhosfantasma–1colunae4linhas
Alémdeindicaradire çãoemqueofantasmaestáindo,osolhossãoa
únicacoisaquesobraquandoeleédevoradopelanossasuperpizza.
Fig.7.10:Inimigos–4colunase2linhas
Tomate,Repolho-roxo,PimentãoamareloeBrócolisrepresentamcada
umdosnossospersonagens. Apenasinvertemosascoresparaindicarem
queestadoestão(ca çandooufugindo),eaindanãotemos100%decertezase
Tomateéumlegume.
Fig.7.11:Cenário–5linhase9colunas
Nossocenárioécompostopordiversasimagens. Cadapartedelevem
deumpeda çodestafiguraemvezdediversasimagensseparadasconforme
veremosadiante,bemcomomaisalgunstruquesconformemelhoramose
evoluímosnossojogo.
171
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 194

7.2. Jogandoocódigo CasadoCódigo
7 .2 J ogando o código
Fazalgunsjogosquenãomexemosnonossocódigobase,então,vamostirar
apoeiradanossaclasse Elemento,adicionandotrêsnovaspropriedades:
public class Elemento {
private int dx;
private int dy;
private ImageIcon imagem;
public void desenha(Graphics2D g) {
if (imagem == null) {
g.setColor(cor);
g.fillRect(px, py, largura, altura);
} else {
g.drawImage(imagem.getImage(), px, py, null);
}
}
...
Tanto dxquanto dyjásãonossosconhecidos,utilizamosemquaseto-
dososjogosparadirecionarnossospersonagensnatela.Amaioriadosnos-
soselementosteráumaimagem,entãonadamelhordoqueusarmosuma
variávelparaguardá-laemnossaclasse Elemento,deixandonossométodo
desenhacomumaimplementa çãopadrãoqueexibaalgumdesenhocaso
nossoobjeto imagemsejanulo,oudesenheaprópriaimagem.
Ocultamosaquiasdemaisvariáveisemétodos,inclusiveos getse sets
daspropriedadesnovas.
Dica
Nossasvariáveis dxe dysãodotipo int,maspoderiamserdotipo
byte,jáquesópossuemtrêsvalores:-1,0e1.
Naprimeiraversãodojogo,usamosomesmoobjetoparatodososper-
sonagens,masdestavezelesserãoatualizadosedesenhadosdeformadife-
172
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 195

CasadoCódigo Capítulo7. Come-comeeosbitmaps
rentes,alémdeterempropriedadesdistintas.Nossoheróicontinuarásendo
representadopelaclasse Pizza,nossosinimigospelaclasse Legume.
public class Pizza extends Elemento {
private Direcao direcao = Direcao.OESTE;
public Pizza() {
super(0, 0, 16, 16);
setImagem(new ImageIcon("imagens/sprite_pizza.png"));
}
private int linha;
private int coluna;
Ocontroledopersonagemnãoaltera linhae colunadiretamente,isso
éfeitonométodo atualiza,queposicionanalinhacorretadeacordocom
adireçãodefinida.
@Override
public void atualiza() {
incPx(getVel() * getDx());
incPy(getVel() * getDy());
if (getDx() == 1)
linha = 0;
else if (getDx() == -1)
linha = 1;
else if (getDy() == -1)
linha = 2;
else if (getDy() == 1)
linha = 3;
if (getDx() + getDy() != 0)
coluna++;
if (coluna > 3)
coluna = 0;
}
173
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 196

7.2. Jogandoocódigo CasadoCódigo
...
}
Lembrandodequeadire çãorealécontroladapor dxe dy,eseoper-
sonagemestiveremmovimento,umououtroteráovalor0.Quandoosdois
estiveremcomovalor0,opersonagemestaráparado,entãonãomudamosa
colunadosprite.
Ométododedesenhoésemelhanteaojávistoanteriormente,oquemuda
agoraéqueconsideramosaspropriedadesdojogo,comoaposi çãodoperso-
nagemnatelaeoespa çamentodocenário,porexemplo.
@Override
public void desenha(Graphics2D g) {
int pX = getPx() - 6;
int pY = getPy() + JogoCenario.ESPACO_TOPO - 6;
// Largura e altura da moldura
int largMoldura = getImagem().getIconWidth() / 4;
int altMoldura = getImagem().getIconHeight() / 4;
// Largura e altura do recorte da imagem
int largImg = largMoldura * coluna;
int altImg = altMoldura * linha;
g.drawImage(getImagem().getImage(),
pX, pY, pX + largMoldura, pY + altMoldura,
largImg, altImg,
largImg + largMoldura,
altImg + altMoldura, null);
}
Reduzimosamargemesquerdae,levandoemconsidera çãooespa çoen-
treagradeeotopodatela,reduzimosamargemsuperior(subtraindo6pixels
emcadaeixo),issoparanossopersonagemter12pixelsdedesenhoamaisque
emsuaversãoanterior.
Otamanhodoelemento(edecadaespa çonagrade)continuasendo16
por16px,mascadafiguradonossospritetem28por28pixels.Esteéotruque
174
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 197

CasadoCódigo Capítulo7. Come-comeeosbitmaps
parausarmosumaimagemmaior:aumentamosotamanhodopersonageme
diminuímosotamanhodasparedesdolabirinto,comoveremosmaisàfrente.
Asvariáveis pXe pYsãoreferentesàposi çãodoelementonatela,ondepo-
sicionaremosnossamoldura.
Osinimigosleguminososdãoumpoucomaisdetrabalho:
public class Legume extends Elemento {
public enum Modo {
PRESO, ATIVO, INATIVO, FANTASMA, CACANDO, FUGINDO;
}
public enum Tipo {
VERMELHO, ROXO, AMARELO, VERDE;
}
private Tipo tipo;
private Modo modo = Modo.PRESO;
private Direcao direcao = Direcao.OESTE;
private int linha;
private int coluna;
private int lnOlhos; // Linha olhos
Osmodosquenossoobjetopodeassumircontinuamsendoosmesmos
dojogoanterior,masagoraeletemum Tipoqueusamosparasaberqual
colunadospritequeremos,jáquecadaumarepresentaumpersonagemem
seumodoca çandoefugindo.
private static ImageIcon olhos;
private static ImageIcon sprite;
static {
olhos = new ImageIcon("imagens/olhos.png");
sprite = new ImageIcon("imagens/sprite_inimigos.png");
}
public Legume(Tipo tipo) {
super(0, 0, 16, 16);
175
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 198

7.2. Jogandoocódigo CasadoCódigo
this.tipo = tipo;
this.coluna = tipo.ordinal();
}
Asimagensparaosolhoseparaosinimigossãoestáticas,pertencemà
classe,enãoàinstânciadela. Omelhorseriaterumaclasseseparadapara
gerenciarasimagensdojogo,masassimmantemosascoisassimpleserea-
proveitamosasmesmasinstânciasdo ImageIconparaosquatroinimigos.
Nossaimagem olhostemapenasumacoluna,entãosóprecisamosnos
preocuparcomaslinhasquevariamdependendodadire çãodopersonagem,
semelhanteaoquefazemoscomnossoherói.
@Override
public void atualiza() {
incPx(getVel() * getDx());
incPy(getVel() * getDy());
if (getDx() == -1)
lnOlhos = 0;
else if (getDx() == 1)
lnOlhos = 1;
else if (getDy() == -1)
lnOlhos = 2;
else if (getDy() == 1)
lnOlhos = 3;
if (modo == Modo.FUGINDO)
linha = 1;
else
linha = 0;
}
}
Utilizamosumaimagemdiferenteseoinimigoestiverfugindo,represen-
tadapelasegundalinhadosprite.Nãoexistemistérionométodo desenha.
Valenotarque,quandooinimigoviraumfantasma,nãodesenhamosa
imagemprincipal,logo,veremosapenasumpardeolhosvagandopelatela.
176
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 199

CasadoCódigo Capítulo7. Come-comeeosbitmaps
@Override
public void desenha(Graphics2D g) {
int pX = getPx() - 6;
int pY = getPy() + JogoCenario.ESPACO_TOPO - 6;
int largMoldura = sprite.getIconWidth() / 4;
int altMoldura = sprite.getIconHeight() / 2;
int largImg = largMoldura * coluna;
int altImg = altMoldura * linha;
if (modo != Modo.FANTASMA)
g.drawImage(sprite.getImage(),
pX, pY,
pX + largMoldura, pY + altMoldura,
largImg, altImg, largImg + largMoldura,
altImg + altMoldura, null);
largMoldura = olhos.getIconWidth();
altMoldura = olhos.getIconHeight() / 4;
altImg = altMoldura * lnOlhos;
g.drawImage(olhos.getImage(),
pX, pY,
pX + largMoldura, pY + altMoldura,
0, altImg, largMoldura,
altImg + altMoldura, null);
}
Emboratenhamostrabalhodobradonométodo desenha, criarum
spritecomtodasascombina çõesdefiguraspossíveisficariainviávele,como
podemosver,fazermesclasdeimagensésimplesmentedesenharumasobre
aoutra.Lembrandodequeaprimeiraaserdesenhadaficaráporbaixo.
Nossaimagem olhos.pngtemlarguraealturaprópriaparaquecada
figurafiquenaposi çãocorretano“rosto”dopersonagem.
177
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 200

7.2. Jogandoocódigo CasadoCódigo
Fig.7.12:Sobrepondoimagens
Depoisdeusarmosumspriteparatermosumpardeolhosolhandoem
cadadireção,chegouahoradevocêperguntarseusarimagenspreviamente
rotacionadaséoúnicojeitodefazermosisso.Paranossasorte,não,essanão
éaúnicaforma.
Mascomoissonãoéumassuntotrivial,veremosnopróximojogo. E
agoracom5linhase9colunas,ostilesqueformamocenáriodonossojogo:
Fig.7.13:Cenárioempartes
Temos um novo problema aqui. Na primeira versão do jogo, nossa
gradesóprecisavadeumúnicovalorpararepresentarasparedesdola-
birinto, porém, nestaversão, precisaremosarmazenarumvalorqueindi-
que a coluna e linha referente à figura que queremos em nossa imagem
tiles_cenario.png.
Adotaremosumasolu çãobemsimplesutilizandoamatemática.Primei-
ramente,todososcódigosquenãoformemasparedesdolabririntopassarão
aterumvalornegativo.Depois,usaremosvalorescujadivisãoerestodadivi-
sãopor10nosindiqueacolunaealinha.Tome,porexemplo,ovalor46,que
178
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 201

CasadoCódigo Capítulo7. Come-comeeosbitmaps
divididopor10resultaem4,6.Assim,sabemosque4éalinhaquequeremos,
e6acoluna.
...
int valor = grade[lin][col];
if (valor >= 0) {
int linha = 0;
int coluna = valor;
if (valor > 9) {
linha = valor / 10;
coluna = valor % 10;
}
...
} else {
// Outros itens do cenário
...
}
Dessaforma,nóssabemosque,seovalordagradeformaiorque9,então
alinhaseráovalordivididopor10,eacolunaseráorestodadivisãopor10.
Olhandonovamenteafigura7.13,notequecadaespa çonaimagem(qua-
dradospontilhados)tem16pixelsdelarguraealtura,masosdesenhosnão
ocupamoespa çotodo.Porisso,nossospersonagens,mesmosendomaiores
queotamanhopadrão,circulamolabirintosemsobreporocenário.
Parafacilitaracria çãodeníveis,asparedesdaprimeiralinhacome çam
comaletra Aevãode0até7,dasegundalinhacomaletra Bevãode10até17,
eassimpordiante.Logo,D6temovalorde36,queequivaleàlinha3ecoluna
6daimagem.Valelembrarquenossacontagemcome çaem0.Utilizamosde
0a7jáquenãotemosacoluna9,edeixamosacoluna8casovocêqueirafazer
modificações.
public static final int A0 = 0;
public static final int A1 = 1;
...
public static final int E0 = 40;
179
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 202

7.2. Jogandoocódigo CasadoCódigo
public static final int E2 = 42;
public static final int LN = 44; // E4
public static final int E5 = 45;
public static final int E6 = 46;
public static final int E7 = 47;
Aconstante LNpoderiaser E4,masfogearegraparafacilitaraleitura
emoutraspartesdocódigo,assimcomonossasantigasvariáveiscomvalores
novos:
public static final int BL = -1; /** Bloco */
public static final int CN = -2; /** Comida normal */
public static final int EV = -3; /** Espaco vazio */
public static final int PI = -4; /** Ponto inicial do jogador */
public static final int SC = -5; /** Super comida */
public static final int P1 = -6; /** Ponto inicial inimigo 1 */
public static final int P2 = -7; /** Ponto inicial inimigo 2 */
public static final int P3 = -8; /** Ponto inicial inimigo 1 */
public static final int P4 = -9; /** Ponto inicial inimigo 2 */
public static final int PF = -10; /** Ponto de Fuga */
public static final int PV = -11; /** Ponto de Volta */
Etudojunto,formandoumbelocenário,ficouassim:
180
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 203

CasadoCódigo Capítulo7. Come-comeeosbitmaps
Fig.7.14:Novocenário
Ocódigodaclasse JogoCenario.javasofreualgumasmudan ças,mas
amaioriaserefereàsepara çãodospersonagensnaclasse Pizzae Legume.
Então,vamosnosfocarnasmudan çasmaisimportantes.
Começamospelométodo desenhar,quefaztodootrabalhoquetemos
manipulandoimagemvalerapena.
for (int lin = 0; lin < grade.length; lin++) {
for (int col = 0; col < grade[0].length; col++) {
int valor = grade[lin][col];
if (valor >= 0) {
int linha = 0;
int coluna = valor;
if (valor > 9) {
linha = valor / 10;
coluna = valor % 10;
}
181
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 204

7.2. Jogandoocódigo CasadoCódigo
int pX = col * largEl;
int pY = lin * largEl + ESPACO_TOPO;
Valoresmaioresouiguaisazerosãoaspartesdocenárioquecompõem
olabirinto,eseovalorformaiorque9,sabemosque,paraacharalinhae
coluna,temosdedividirpor10.
int largMoldura = cenario.getIconWidth() / 9;
int altMoldura = cenario.getIconHeight() / 5;
int largImg = largMoldura * coluna;
int altImg = altMoldura * linha;
g.drawImage(cenario.getImage(), pX, pY,
pX + largMoldura, pY + altMoldura,
largImg, altImg,
largImg + largMoldura, altImg + altMoldura, null);
Nosso cenario( tiles_cenario.png)tem9colunase5linhas,fora
isso,édesenhadocomoqualqueroutrospritedojogo.Seovalorformenos
que0,verificamosseéumacomidanormalousupercomida.
} else {
if (valor == Nivel.CN)
g.drawImage(azeitona.getImage(),
col * largEl, lin * largEl + ESPACO_TOPO, null);
else if (valor == Nivel.SC)
g.drawImage(pepperoni.getImage(),
col * largEl, lin * largEl + ESPACO_TOPO, null);
}
}
}
texto.desenha(g, "Pontos: " + pontos, 10, 20);
pizza.desenha(g);
for (Elemento el : inimigos) {
if (el == null)
182
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 205

CasadoCódigo Capítulo7. Come-comeeosbitmaps
continue;
el.desenha(g);
}
Outrométodomodificadoquemereceumpoucomaisdeaten çãoéo
validaMovimento.
private boolean validaMovimento(Elemento el, int dx, int dy) {
// Próxima posição x e y
int prxPosX = el.getPx() + el.getVel() * dx;
int prxPosY = el.getPy() + el.getVel() * dy;
int col = convertePosicaoIndice(prxPosX);
int lin = convertePosicaoIndice(prxPosY);
int colLarg = convertePosicaoIndice(prxPosX +
el.getLargura() - el.getVel());
int linAlt = convertePosicaoIndice(prxPosY +
el.getAltura() - el.getVel());
if (foraDaGrade(col, lin) || foraDaGrade(colLarg, linAlt))
return true;
Nossavalidaçãodemovimentonãoserestringemaisapenasaosobjetos
daclasse Pizza,eleaceitaqualquerobjetoqueforum Elemento,masso-
menteos Legumespodemcruzaralinhaparaentraresairdajaula.Logo,
verificamosseo Elementoaservalidadoéumainstânciadaclasse Legume,
efazemoso castparaverificarseoobjetoestánomodo PRESO.
// Validar linha branca
if (el instanceof Legume) {
if (grade[lin][col] == Nivel.LN ||
grade[lin][colLarg] == Nivel.LN ||
grade[linAlt][col] == Nivel.LN ||
grade[linAlt][colLarg] == Nivel.LN) {
if (el.isAtivo() ||
((Legume) el).getModo() == Modo.PRESO)
183
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 206

7.2. Jogandoocódigo CasadoCódigo
return false;
return true;
}
}
if (grade[lin][col] >= Nivel.BL ||
grade[lin][colLarg] >= Nivel.BL ||
grade[linAlt][col] >= Nivel.BL ||
grade[linAlt][colLarg] >= Nivel.BL) {
return false;
}
return true;
}
Antes,tínhamosumúnicovalorpararepresentaraparededocenário,
masagoraqualquervalormaiorouiguala Nivel.BL(queé-1)representa
umobstáculo.Assim,agoratemosdiversosblocosedevemosconsiderarque
umdelespodeseratravessadodependendodoestadodopersonagem.
Parasimplificarascoisas,apenasmarcamosaposi çãodessebloconava-
riável Nivel.LN,everificamosprimeiramentesealgum Legumecolidiu
comessebloco,jáquesomenteosinimigospodematravessaressaparede.
Depois,verificamossehouvecolisãocomqualqueroutrobloco.
Porfim,nossa gradeagoraéumacópiade Nivel.cenarioparaque,
aocarregarnovamenteojogo,todasaspastilhasquejáforamcomidasvoltem
aoseulugar.
...
grade = copiaNivel(Nivel.cenario);
...
private int[][] copiaNivel(int[][] cenario) {
int[][] temp = new int[cenario.length][cenario[0].length];
for (int lin = 0; lin < cenario.length; lin++) {
for (int col = 0; col < cenario[0].length; col++) {
temp[lin][col] = cenario[lin][col];
}
184
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 207

CasadoCódigo Capítulo7. Come-comeeosbitmaps
}
return temp;
}
Apenascopiamososvaloresdeumarrayparaooutro,trabalhandoem
novainstânciaparanãomodificaroarrayoriginal.Sevocêficoucomavon-
tadedecriarseuspróprioscenárioseimagens(eeurealmenteesperoque
tenhaficado),ousimplesmentequeiramodificarosarquivosdojogo,você
podeusaroGimp(http://www.gimp.org),queéumeditordeimagensgra-
tuito.
Dica
Commuitoesforço,PixelArtéotipodedesenhoqueeuconsigofazer.
Porsorte,existemuitomaterialnainternet,comoacomunidadePixel
Join(conteúdoeminglês):http://pixeljoint.com/.
7 .3 C odificando o jogo
Nossoobjeto ImageIconéagrandenovidadedestecapítulo,enãoperdemos
tempoemusá-lonométodo desenhar,chamando drawImage(comseus
dezparâmetros)doobjeto Graphics2Dparaisso.
Mal começamos a utilizar imagens e já trabalhamos com sprites
e tiles, aplicando recortes, espelhando e sobrepondo as imagens, que
não são poucas: azeitona.png, olhos.png, pepperoni.png,
sprite_inimigos.png, sprite_pizza.pnge tiles_cenario.png.
Emesmonossocenáriosendocompostoporváriasfiguras,usamosopoder
damatemáticapara,apartirdovalordagrade,saberquallinhaecolunade-
vemosdesenhar.
Na primeira versão do jogo, trabalhamos apenas com um objeto
querepresentavatantooprotagonistaquantoosantagonistas, masagora
cada um deles é representado por sua própria classe,Pizza.java e
Legume.java. Fizemos uma pequena revisão nos códigos alterados
185
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 208

7.4. Resumo CasadoCódigo
da classe JogoCenario.java, e nenhuma mudança em nossas classes
Jogo.javae JogoCenario.java.
Jáfaziaalgunscapítulosquenãoexpandíamosnossabiblioteca,entãoadi-
cionamosemnossaclasse Elemento.javamelhoriasparatrabalharcoma
direçãodoobjetoeimagens. Confiraem:https://github.com/logicadojogo/
fontes/tree/master/Cap07.
Não fizemos aqui
• Aplicarrotaçãonasimagens;
• Apresentarospersonagensnaintroduçãodojogo.
Melhore você mesmo
• Apliqueefeitossonoros;
• Utilizesuasprópriasimagensparapersonalizerojogo.
7 .4 R esumo
Vimoscomotrabalharcomimagens,comoéfácilcarregarumaimagemsim-
plesequesegmentarporlinhasecolunaspodeajudarnautiliza çãodeima-
genscomplexasquerepresentemmúltiplasfiguras. Esperoqueagoravocê
consigatrabalharcomspritesetilessemterdequebraracabe ça.
Nossamanipulaçãodeimagensestáapenasnocome ço,masmuitomais
podeserfeitocomJavaquenãocaberianestelivro.Atémesmoporqueesta-
mosnoscaminhandoparaosúltimoscapítulos.Então,vamosnosfocarno
queforútilparaosnossosjogos.
186
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 209

Capítulo8
Umjogodeânguloserota ções
AntesdefalarmosdeAsteroids,vamosfalardamatemáticaenvolvidanele.
Isso,éclaro,semfalarmuitodematemática(oupelomenosnãotantoquanto
seuprofessorgostaria),jáqueaclasse java.lang.MathqueoJavanos
provêécheiaderecursos.
Começamoscomefeitosderota ção,escalonamentoeposicionamento,
depoiscriamosumjogochamado Nave Quebrada, paratestarmosoque
aprendemos.Prepare-separa:
• Rotação;
• Escalonamento;
• Transição;
• Ângulos.
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 210

8.1. Rotação CasadoCódigo
Fig.8.1:JogoNaveQuebrada
8.1 R otação
Aclasse Graphics2Dnosoferecedoismétodospararota çãodosdese-
nhoseimagens. Oprimeiroé rotate(double theta), eosegundo
rotate(double theta, double x, double y) ,sendoque thetaé
oângulodarota çãoemradianos.
Como trabalharemos com valores em graus, utilizamos
Math.toRadians(graus) para conversão. Come çando com exem-
plos,vamosdesenharumquadradocinzadefundo,aplicarumarota çãode
180°,edepoisdesenharumquadradomenornacoramarela,ambosnoeixo
0.
Considerequeasaltera çõesnoobjeto g2drefletememtodaanossatela
depintura:
188
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 211

CasadoCódigo Capítulo8. Umjogodeânguloserota ções
@Override
publicvoid paintComponent(Graphics g) {
Graphics2D g2d = (Graphics2D) g;
g2d.setColor(Color.GRAY);
g2d.fillRect(0, 0, 200, 200);
float anguloEmRadiano = (float) Math.toRadians(180);
g2d.rotate(anguloEmRadiano);
g2d.setColor(Color.YELLOW);
g2d.fillRect(0, 0, 40, 40);
}
Oquadradocinzanãoserárotacionado,umavezquefoidesenhadoantes
dachamadadométodo rotate.Eoquadradoamareloacabaráforadatela,
issoporquearota çãofoifeitacombasenascoordenadas0doseixosXeYda
tela:
Fig.8.2:Giropadrão
Afiguraanteriorexemplificamaisoumenosondeodesenhofoiparar
aousarumarota çãode90°. Maséclaroquetemosmaneirasdefazeruma
rotaçãolevandocomobaseoeixocentral,umadelaséreposicionarnossa
telaantesdeaplicararota çãoedepoisvoltá-laaposi çãooriginal.
Paraalteraraposi çãodatela,usamosométodo translate,querecebe
comoparâmetrooeixoXeYdanovaposi ção. Ateladeveserposicionada
189
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 212

8.1. Rotação CasadoCódigo
deformaquesuascoordenadas 0xe 0yfiquemnocentrodajanelaantese
depoisdarota ção.Paraisso,usamosmetadedalarguraealturadatelacomo
parâmetros,quenestecasotêmomesmovalorde TAMANHO_TELA:
int meio = TAMANHO_TELA / 2;
float anguloEmRadiano = (float) Math.toRadians(180);
g2d.translate(meio, meio);
g2d.rotate(anguloEmRadiano);
g2d.translate(-meio, -meio);
g2d.setColor(Color.YELLOW);
g2d.fillRect(0, 0, 40, 40);
Primeiro,reposicionamosateladeixandoascoordenadas( 0, 0)aocen-
tro,depoisefetuamosarota çãoe,então,voltamosatelaparaopontodeori-
gem. Assim,nossoquadradoamareloserádesenhadocomoseestivessegi-
randoemtornodatela,mesmosemalteraraposi çãododesenhonométodo
fillRect,algoparecidocom:
Fig.8.3:Girocentral
Inicialmente,temosatelanaposi çãooriginalcomumquadradoama-
relonocantosuperioresquerdo. Atelaéreposicionadacom translate,
eapontadoquadradoamareloficaposicionadaaocentro,assimpodemos
aplicararota ção.
Depois,reposicionamosnovamenteatela,subtraindoametadedotama-
nhodelanoseixosXeY.Comofazemosissodeumasóvez,visualizamos
190
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 213

CasadoCódigo Capítulo8. Umjogodeânguloserota ções
apenasodesenhofinal,masveremoscomofazerissodeformaquevireuma
animação.
Dica
Umaanalogiaseriavocêpensaremumpintorengessadodacabe ça
aospésquesóconseguemexeramão,limitadoadesenharsemprena
mesmaposição. Então,paratermosaquelemesmodesenhoinclinado,
emvezdepedirparaopintorsemover,vocêgiraateladepinturae,
quandoeleacabar,vocêvoltaatelaparaaposi çãooriginal.
Observequeprimeiroaplicamosaaltera çãonatelae,depois,pintamoso
desenho,executandoduaschamadasaométodo translate.Parafacilitar
ascoisas,asegundachamadadométodo rotatenospoupadessetrabalho
dereposicionamento:
int meio = TAMANHO_TELA / 2;
float anguloEmRadiano = (float) Math.toRadians(180);
g2d.rotate(anguloEmRadiano, meio, meio);
g2d.setColor(Color.YELLOW);
g2d.fillRect(0, 0, 40, 40);
Realmentesabercomoissofuncionaetodaamatemáticaenvolvidanão
énecessárioparaqualquercapítulodestelivro,masterano çãodecomoes-
sesdoismétodossecomportamajudarámuitonodesenvolvimentodestee
dequalqueroutrojogoemquevocêqueiragirarobjetospelatela. Porisso
exemplificamos,mesmoquesuperficialmente.
Atéagora,nósaplicamosarota çãonatelatoda,masesequisermosro-
tacionaroselementosindividualmente? Sãoosmesmosconceitos,sóque
levandoemconsidera çãootamanhoeaposi çãodoelemento.
final int TAMANHO_TELA = 250;
int px = 10;
int py = 0;
191
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 214

8.1. Rotação CasadoCódigo
int metadeLargEl = 200 / 2;
int metadeAltEl = 220 / 2;
g2d.rotate(anguloEmRadiano, metadeLargEl + px, metadeAltEl + py);
g2d.setColor(Color.YELLOW);
g2d.fillRect(px, px, larg, alt);
Nossoquadradoamareloagoratemasdimensões200por220. Sendo
que metadeLargElémetadedalargura( metadeAltElmetadedaaltura)
doelemento,queestáposicionadoem10xe0y.Aposi çãodoelementodeve
serlevadaemconsidera ção,nãosomentealarguraealtura.Comoestamos
somandoaoseixosmetadedalarguraealtura,oresultadoseráoquadrado
amarelogirandoemseueixocentral.
Masagrandequestãovemquandotemosdoisoumaisobjetosnatela,já
queapósachamadadométodo rotate(oudeoutrométodoquetransforme
atela)asaltera çõesoudesenhosquevierememseguidalevamemcontaos
valoresaplicadosanteriormente,fazendocomqueaordememquesãoapli-
cadosgereresultadosdiferentes.
É agora que entra em cena a classe
java.awt.geom.AffineTransform, representada pela variávelaf.
Sem desmerecê-la, ela resumidamente serve como um recipiente para
aplicarmosastransformadas.
int px = 0;
int py = 0;
int largEl = 200;
int altEl = 200;
int metadeLargEl = largEl / 2;
int metadeAltEl = altEl / 2;
AffineTransform af = g2d.getTransform();
Obtemosumainstânciadoobjeto AffineTransformdopróprioobjeto
Graphics2D,masessaésóumadasváriasformasdeobtê-la.Faremosdesta
veztrêsdesenhos,quadradosdamesmalarguraealtura(200,200),nascores
amarelo,verdeevermelho,posicionadosnotopoaoladoesquerdo,centroe
nabaseaoladodireitodatela,respectivamente.
192
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 215

CasadoCódigo Capítulo8. Umjogodeânguloserota ções
// Quadrado Amarelo
g2d.rotate(anguloEmRadiano, metadeLargEl + px, metadeAltEl + py);
g2d.setColor(Color.YELLOW);
g2d.fillRect(px, px, largEl, altEl);
Atéaquitudocerto,desenhamosnossoquadradoamarelonotopodatela
aplicandoumarota ção.Mas,antesdedesenharmosoquadradoverde,preci-
samosretirarastransforma çõesaplicadas,voltandoatelaparaaposi çãoori-
ginal.Logo,chamamos setTransformpassandoumatransformada“vazia”,
obtidanoiníciodométodo.
// Quadrado Verde
g2d.setTransform(af);
px = TAMANHO_TELA / 2 - metadeLargEl;
py = TAMANHO_TELA / 2 - metadeLargEl;
g2d.rotate(anguloEmRadiano, metadeLargEl + px, metadeAltEl + py);
g2d.setColor(Color.GREEN);
g2d.fillRect(px, py, largEl, altEl);
// Quadrado Vermelho
g2d.setTransform(af);
px = TAMANHO_TELA - largEl;
py = TAMANHO_TELA - altEl;
g2d.translate(metadeLargEl + px, metadeAltEl + py);
g2d.rotate(anguloEmRadiano);
g2d.translate(-metadeLargEl - px, -metadeAltEl - py);
g2d.setColor(Color.RED);
g2d.fillRect(px, py, largEl, altEl);
Asvariáveis pxe pyagorarepresentamocentrodatela,entãodesenha-
mosnossoquadradoverde. Fazemosomesmoparaoquadradovermelho,
masoposicionamosnoladoinferiordireito,eutilizamosoprimeiroexem-
plodométodo rotate.
193
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 216

8.1. Rotação CasadoCódigo
Fig.8.4:Testerota çãonoeixocentraldodesenho
Comoo AffineTransformservederecipiente,nósnãoprecisamos
aplicarasaltera çõesdiretono Graphics2D,porexemplo:
AffineTransform af = new AffineTransform();
af.rotate(anguloEmRadiano, metadeLargEl + px, metadeAltEl + py);
g2d.setTransform(af);
g2d.setColor(Color.YELLOW);
g2d.fillRect(px, px, largEl, altEl);
Aplicamos a rota ção no objeto af, e depois usamos
g2d.setTransform para aplicarmos o efeito em nosso desenho. Po-
deríamosutilizarsomenteorecipiente:
af.setToIdentity();
af.translate(metadeLargEl + px, metadeAltEl + py);
af.rotate(anguloEmRadiano);
af.translate(-metadeLargEl - px, -metadeAltEl - py);
g2d.setTransform(af);
g2d.setColor(Color.RED);
g2d.fillRect(px, py, largEl, altEl);
Estecódigotemomesmoefeitodocódigoanteriormenteusadopara
desenharoquadradovermelho,masaplicamosastransforma çõesnanossa
194
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 217

CasadoCódigo Capítulo8. Umjogodeânguloserota ções
própria instância do AffineTransform, e não diretamente no ob-
jeto Graphics2D. Importante notar que, depois que usamosaf uma
vez, voltamos a transformação ao estado original chamando o método
setToIdentity().
Vimosalgumasmaneirasdetrabalharcomessasduasclassescheiasde
recursos,eaindaexistemoutrasformasediversosmétodosquenãocitamos.
Principalmentenaclasse AffineTransform,queenglobadiversosméto-
dosparaaplicarmostransforma çãoemnossasimagens,inclusive4versões
dométodo rotate(semcontaro quadrantRotate).
Falaremosmaisaolongodocapítulo,masnãocobriremostudo,jáque
fugiríamosdoescopodolivro. Recomendoquevejaadocumenta çãopara
conhecermais.
Recomendo também que dê uma olhada na classe
RotacaoTeste.java e teste o código. Faça alterações e veja coisas
estranhasacontecendoquandonãoapagamosastransforma çõesanteriores
antesdeaplicarmosumanova.
8.2 E scalonamento e transição
DepoisdetantocódigoemetáforaspararotacionarcoisasnoJava,falarde
escalonamentoetransi çãonãoénenhumcarnaval. Come çandopelatran-
siçãocomométodo translate,tantodaclasse Graphics2Dquantoda
AffineTransform.
Falandodeformaresumidaeincompleta,elereposicionaatelanasco-
ordenadasXeY,etudooquefordesenhadodepoislevaráemconsidera ção
essascoordenadas. Porexemplo,ocódigoaseguirdesenhaumquadrado
amareloem25xe25y:
g2d.translate(15, 25);
g2d.setColor(Color.YELLOW);
g2d.fillRect(10, 0, larg, alt);
Movemosatela15pixelsparaadireitae25pixelsparabaixo,entãoas
coordenadasiniciaisnãosãomais(0,0).Aopreencheroquadradonaposi ção
(10,0),atelavailevaremconsidera çãosuanovaposi ção,queagoraé(15,25).
Portanto,oquadradoserádesenhadonoeixo25x(15+10)e25y(25+0).
195
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 218

8.2. Escalonamentoetransição CasadoCódigo
Escalonaréumaformaderedimensionarodesenhoouimagem,econ-
seguimosissousandoométodo scale,tambémdisponívelemambasas
classes.Paradesenharnossoquadradocomodobrodotamanho,podemos
fazerdaseguinteforma:
g2d.scale(2, 2);
g2d.setColor(Color.YELLOW);
g2d.fillRect(0, 0, 40, 40);
Nossoquadradovaiserdesenhado2vezesmaiornalarguraealtura,logo,
mesmoqueseutamanhoseja40por40,natelaaparecerácom80px.Também
podemosdiminuiraoinvésdeaumentar:
g2d.scale(0.5, 0.5);
g2d.setColor(Color.YELLOW);
g2d.fillRect(0, 0, 40, 40);
Agoraoquadradoamareloterá50%dotamanhooriginal, 20por20.
Você pode passar valores diferentes para largura e altura, por exemplo
g.scale(2, 0.5),desdequeosvaloressejamdiferentesde0.Sendoiguais
a1,oresultadoseráotamanhooriginal.
Dica
Amaiorvantagememutilizar scalee translateestáquando
aplicamosnojogocomoumtodo,podendocriarinúmerosefeitos,en-
quantoaplicaremelementosisoladamentepodecausarerros.Umexem-
ploseriaumelementoqueestáemumaposi çãonoseixosXeYqueco-
lidacomoutro,masqueacabesendodesenhadoemoutrapartedatela,
atrapalhandoojogador.
Adicaé:semprepensenadetec çãodecolisãoaoaumentaroudimi-
nuirotamanhodosseuselementos.
Naclasse RotacaoTeste.java,temosummodoque,alémdegirar,
aumentaediminuiotamanhododesenho:
196
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 219

CasadoCódigo Capítulo8. Umjogodeânguloserota ções
int metadeLargEl = largEl / 2;
int metadeAltEl = altEl / 2;
// g2d.scale(escala, escala); // Chamada A
g2d.translate(TAMANHO_TELA / 2, TAMANHO_TELA / 2);
g2d.rotate(anguloEmRadiano);
g2d.scale(escala, escala); // Chamada B
g2d.translate(-metadeLargEl, -metadeAltEl);
// g2d.scale(escala, escala); // Chamada C
g2d.setColor(Color.YELLOW);
g2d.fillRect(0, 0, largEl, altEl);
Aordememqueaplicamosatransforma çãonodesenhoinfluenciadi-
retamenteoresultado. Parademonstrarisso,existemtrêschamadasparao
método scale(chamadaA,BeC),então,secomentaralinhadachamada
BedescomentaradachamadaAouC,vocêteráanima çõesdistintas.
Fig.8.5:Girareescalonar
Porserapenasumaclassedeteste,mantivemosascoisasbemsimplese
nãovamosnosaprofundaremseuscódigos.Porém,valecomentarque,para
criarasanima çõesdaclassedeteste,nossarota çãovaide0a360graus,e
aumentamosaté9vezesedepoisdiminuímosaté10%otamanhododesenho
197
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 220

8.3. Umjogoparagirareatirar CasadoCódigo
original.
If (System.currentTimeMillis() >= prxAtualizacao) {
graus += inc;
if (graus > 360)
graus = 0;
else if (graus < 0)
graus = 360;
escala += incEscala;
if (escala > 9f || escala < 0.1f)
incEscala = -incEscala;
tela.repaint();
prxAtualizacao = System.currentTimeMillis() + FPS;
}
Terminamosaintrodu ção,enadamelhorquecriarumjogoparasanar
qualquerdúvida.Casoqueiravermaisexemplos,acessehttp://abrindoojogo.
com.br,eprocurepor AffineTransformousimplesmenteJava.
8.3 U m jogo para girar e atirar
Ojogo Nave Quebradaésobreumpilotoquetevesuanavedanificadaenão
conseguemaissairdolugar,masporsorteaindapodegirareatirar.Conve-
nientemente,eleparounocentrodatela,masinimigosvermelhosaparecem
detodososlados,girandoeindoemsuadire çãoemdiferentesvelocidades.
Nota
Atéadatadepublica çãodestelivro,ojogoqueremeteaAsteroids
maisrecentechama-se Galak-Z: The Dimensional,criadopela17-BIT
(http://17-bit.com).
Paragrandescoberturassobreesteeoutrosjogos,recomentoosite
independente Overloadr(http://overloadr.com.br),queabrangeampla-
menteomundodosvideogames.
198
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 221

CasadoCódigo Capítulo8. Umjogodeânguloserota ções
Todavezqueuminimigoacertaanave,elatrocadecorediminuiseu
tamanho(2pixelsamenossemusar scale),apontoquefiquetãopequena
queojogoacabe. Emborausemosumaimagemdefundo,oselementosdo
jogoserãotodosdesenhados.
Teremos 3 elementos no jogo: Asteroide, Nave e Tiro.
Além da classe AffineTransform, utilizaremos bastante a classe
java.lang.Mathe,emboraamaioriadosmétodosdaclasse Mathtra-
balhemcomvaloresemradianosetipos double,parafacilitarnossolado,
trabalharemoscomângulosde0a360°etipos float.Issoporquenãopre-
cisamosdetantaprecisãoeaindaconsumimosmenosmemória.
Aplicaremosrotaçãonanaveeemnossosasteroides,issoquerdizerque
usaremostransformaçõesemcadaelementoindividualmente.Paraumaalte-
raçãonãosobrescreveroutra,utilizamos afAnteriorparaguardarovalor
originaledepoisrestaurá-lo. Paraasaltera çõesindividuaisetemporárias,
usamosavariável af.Ambasasvariáveissãoestáticaseobtidaspormeioda
nossaclasse Elemento.
...
public class Elemento {
public static AffineTransform afAnterior;
protected static final AffineTransform af =
new AffineTransform();
...
Outramudançaimportantenaclasse Elementoéque,paratermosuma
movimentaçãomaissuave,nossasvariáveis pxe pyserãotransformadasde
inteirosparaflutuantes( intpara float).
private float px;
private float py;
public void setPx(float px) {
this.px = px;
}
public void setPy(float py) {
this.py = py;
}
199
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 222

8.3. Umjogoparagirareatirar CasadoCódigo
Essamudançanãofazdiferen çanahoradedefinirovalor,apenaspara
obtê-lo,entãomantivemosoretornocompatívelcomaversãoanterior,fa-
zendoo cast(convertendo)de floatpara int,ecriamosmétodosnovos
pararetornarovalorcomo float.
public int getPx() {
return (int) px;
}
public int getPy() {
return (int) py;
}
public float getMovPx() {
return px;
}
public float getMovPy() {
return py;
}
OmotivodissoéqueosmétodosdedesenhodoJavautilizammedidas
empixele,porconsequência,valoresinteiros.Masoscálculosqueusamosna
movimentaçãopodemresultaremvaloresdepontoflutuante.Dessaforma,
agradamostantoaclasse Mathquantoaclasse Graphics2D.
Nossaclasse Nave.javatemapenasduasvariáveis:umaparacontrolar
oângulousadonarota ção(variável angulo),e inverteCorparaindicar
quandoanaveforatingida:
public class Nave extends Elemento {
private float angulo;
private boolean inverteCor;
...
public float getAngulo() {
return angulo;
}
public void setAngulo(float angulo) {
this.angulo = angulo;
}
200
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 223

CasadoCódigo Capítulo8. Umjogodeânguloserota ções
public void inverteCor() {
inverteCor = !inverteCor;
}
}
Énométodo desenhaqueascoisasficammaisinteressantes.Entretanto,
antesdedesenharmosqualquercoisa,guardamosastransforma çõesatuais,
jáqueprecisamosmanteromesmoestadoparaqueospróximoselementos
sejamdesenhadoscorretamente.
@Override
public void desenha(Graphics2D g) {
afAnterior = g.getTransform();
float rad = (float) Math.toRadians(getAngulo());
af.setToIdentity();
af.rotate(rad, getLargura() / 2 + getPx(),
getAltura() / 2 + getPy());
g.setTransform(af);
Depois,convertemosnossoânguloemgrauspararadianos,pararotaci-
onarmosnossodesenho. Comoavariável afécompartilhadacomoutros
elementos,resetamo-lacomométodo setToIdentity().Nestecaso,es-
tamosignorandoqualquertransformadaanterior.
if (inverteCor)
g.setColor(Color.BLUE);
else
g.setColor(Color.YELLOW);
g.fillRect(getPx(), getPy(), getLargura(), getAltura());
g.setColor(Color.GREEN);
g.fillRect(getPx() + getLargura() / 2,
getPy() + getAltura() / 4,
getLargura() / 2, getAltura() / 2);
g.setTransform(afAnterior);
}
201
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 224

8.3. Umjogoparagirareatirar CasadoCódigo
Inicialmente,nossanaveéamarela,masseestivercomacorinvertida,
serádesenhadanacorazul.Desenhamosumquadradomenornacorverde
paraindicaraorigemdodisparo.Depois,restauramosatransforma çãoan-
terior,obtidanocome çodométodo.
Fig.8.6:Naveantesedepoisdacolisão
Comooânguloinicialé0º(ou360º),consideramoscomofrentedanave
oladodireitodoquadrado,ondeposicionamosumsegundoquadradoverde
commetadedalarguraealturadoprimeiro,deformacentralizada.
Dica
Estamos apagando as transformações com setToIdentity(),
mas também podemos “acumular” transformações usando
af.setTransform( afAnterior ) .
Nossaclasse Asteroideéumquadradovermelhoquenãoinverteacor,
mastemrota çãoconstante,gerenciadapelavariável anguloRotacao,que
éincrementadaconstantemente.
public class Asteroide extends Elemento {
private float angulo;
private float anguloRotacao;
@Override
public void desenha(Graphics2D g) {
if (!isAtivo())
return;
afAnterior = g.getTransform();
202
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 225

CasadoCódigo Capítulo8. Umjogodeânguloserota ções
af.setToIdentity();
af.rotate(anguloRotacao,
getLargura() / 2 + getPx(),
getAltura() / 2 + getPy());
g.setTransform(af);
g.setColor(Color.RED);
g.fillRect(getPx(), getPy(),
getLargura(), getAltura());
g.setTransform(afAnterior);
}
Agrandenovidadedessaclasse(edessejogo)estánométodo atualiza.
Nóssimplesmentenãoutilizamosvariáveis dxe dyparacontrolaradire ção
doelementonoseixosXeY,comonosjogosanteriores.Emvezdisso,calcu-
lamosadire çãocombasenoângulo.
@Override
public void atualiza() {
if (!isAtivo())
return;
float cos = (float) Math.cos(
Math.toRadians(angulo));
float sen = (float) Math.sin(
Math.toRadians(angulo));
setPx(getMovPx() + cos * getVel());
setPy(getMovPy() + sen * getVel());
anguloRotacao++;
if (anguloRotacao == 360)
anguloRotacao = 0;
}
Paracontrolaradire çãoemqueoasteroidesemove,usamosumaforma
maissofisticada,queépormeiodo senoe cossenocombasenoângulo,que
podeserentreoasteroideeanavedojogador,porexemplo.
203
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 226

8.3. Umjogoparagirareatirar CasadoCódigo
Usamosafun ção Math.sinparacalcularoseno,e Math.cospara
ocosseno. Ambasasfun çõespedemoânguloemradianos,entãofazemos
aconversãonachamadadosmétodos. Umavezcomosvaloresde cose
sen,definimosanovaposi çãosomandoaposi çãoatual(empontoflutuante)
multiplicadapelavelocidadedoelemento.
Podemosobteroânguloentreosdoiselementos(comumafun çãoqueve-
remosmaisadiante),assimcalculamosocossenoesenoparasaberoquanto
devemosnosmovernoseixosXY(cossenoparaoeixoX,esenoparaoeixo
Y)parachegarmosaodestino,fazendoassimosasteroidesiremnadire ção
desejada,independentedesuaslocaliza çõesnatela.
Usamosumavelocidadedemovimentovariadaparacadaasteroide,e
anguloRotacaoparagirá-lorapidamente(semconvertê-loemradianos).
Elesnãotêmmuitacriatividadeparagirar,mastêmumefeitode shurikene
sãodestruídosportiros.Vejanossaclassemaissimples:
public class Tiro extends Elemento {
private float angulo;
...
@Override
public void atualiza() {
if (!isAtivo())
return;
float cos = (float) Math.cos(
Math.toRadians(angulo));
float sen = (float) Math.sin(
Math.toRadians(angulo));
setPx(getMovPx() + cos * getVel());
setPy(getMovPy() + sen * getVel());
}
...
}
A classe Tiro utiliza o método de desenho padrão (da classe
Elemento),esuaúnicapreocupa çãoésaberemqualânguloojogadores-
204
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 227

CasadoCódigo Capítulo8. Umjogodeânguloserota ções
tavaquandoefetuouodisparo,quesegueemúnicadire çãoatéencontrarum
asteroideousairdatela–emambososcasos,ficandoinativo.
Vimosqueoânguloéachavedarota çãoemovimenta çãodoselementos
dessejogo,entãoprecisamosobtê-locorretamente.Paraisso,pedimosmais
umavezajudadoJavaesuaclasse Math,conformeveremosaseguir.
8.4 J ogando o código
Nossaclasse JogoCenario.java,ondecome çamosojogocomumanave,
vinteecincotirosecinquentaaerólitos(issomesmo,nãosãoasteroides,são
aerólitos).
private Nave nave;
private Tiro[] tiros = new Tiro[25];
private Asteroide[] aerolitos = new Asteroide[50];
private Texto texto = new Texto();
private Random rand = new Random();
private Estado estado = Estado.JOGANDO;
private int pontos;
private int adiciona = 2;
private int contadorTiro;
private int intervalo = 60;
private int temporizador = 0;
private float graus;
Usamosavariável adicionaparasaberquantosinimigosadicionamos
natelaacada intervalode60atualiza çõesou3segundos. Valelem-
brarquedefinimosnosso FPScom20atualiza çõesporsegundo.Avariável
contadorTiroéusadacomoíndicedoarray tiros.
Todososobjetossãoinstanciadosnométodo carregar,enãodinami-
camenteduranteojogoconformeasintera çõesforemocorrendo.Issopode-
riaserfeito,mascriarumanovainstânciateráumcustooperacionalmaior
doquejáteroobjetoeapenasativá-lo(lembrandodequeestamosfalando
demilissegundos).
205
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 228

8.4. Jogandoocódigo CasadoCódigo
@Override
public void carregar() {
texto.setCor(Color.WHITE);
for (int i = 0; i < tiros.length; i++) {
tiros[i] = new Tiro(5, 5);
tiros[i].setVel(5);
}
for (int i = 0; i < aerolitos.length; i++) {
aerolitos[i] = new Asteroide();
}
nave = new Nave(0, 0, 40, 40);
nave.setAtivo(true);
nave.setCor(Color.YELLOW);
Util.centraliza(nave, largura, altura);
}
Dessa forma, além de reaproveitarmos os objetos, deixamos claro o
quantoderecursosprecisamos,diminuindooriscodeojogoficarlentocom
opassardotempo.
206
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 229

CasadoCódigo Capítulo8. Umjogodeânguloserota ções
Dica
Nãopudedeixardetestarojogocomgrandesquantidadesdeelemen-
tosnatela,entãoaumenteiaquantidadedetirospara2.500,com5.000
asteroidessendoadicionados25porvezenãotivesensa çãodelentidão
outravamento.Oefeitoficoulegal:
Fig.8.7:Tiros,muitostiros
Avidadojogadoréotamanhodapróprianavequediminuiconformeé
atingida,eeleperdeseelaficarmuitopequena.Paradarchanceaojogador,
osinimigossãoadicionadosemquantidadeseintervalospré-definidospelas
variáveisadicionae intervalo.
207
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 230

8.4. Jogandoocódigo CasadoCódigo
@Override
public void atualizar() {
if (estado != Estado.JOGANDO) {
return;
}
if (nave.getLargura() < 5) {
estado = Estado.PERDEU;
return;
}
if (temporizador == intervalo) {
temporizador = 0;
maisAerolitos();
} else
temporizador++;
Otamanhomínimodojogadoré5pixels,enovosaerólitossãoadicio-
nadosaojogoquandoo temporizadorseigualaao intervalo.Anave
nãosemovimentapelatela,masquandoojogadorpressionaparaesquerda
oudireitaparagirá-la,diminuímosouaumentamososgrausdanavesem
extrapolarnossorange.
if (Jogo.controleTecla[Jogo.Tecla.ESQUERDA.ordinal()])
graus -= 10;
else if (Jogo.controleTecla[Jogo.Tecla.DIREITA.ordinal()])
graus += 10;
if (graus < 0)
graus += 360;
else if (graus > 360)
graus -= 360;
nave.setAngulo(graus);
Aopressionarobotãodea ção(mapeadoparaateclaespa ço),chama-
mosométodo adicionarTiroquecolocanovostirosnatela.Parasaber
208
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 231

CasadoCódigo Capítulo8. Umjogodeânguloserota ções
paraondeelaestáapontada,levamosemconsidera çãoseuângulo,queusao
mesmoânguloparadirecionarotiro.
if (Jogo.controleTecla[Jogo.Tecla.BC.ordinal()]) {
adicionarTiro(nave.getAngulo());
Jogo.liberaTecla(Jogo.Tecla.BC);
}
Nossosaerólitoscome çamnapartesuperiorouinferiordatela,masinici-
almenteforadela,eelesvagamaleatoriamenteouemdire çãoanave.Quando
elescolidemcomotirooucomanave,ousimplesmentecruzamparaforada
telaalémdopontodeorigem,sãodestruídos(inativados).
for (Asteroide ast : aerolitos) {
if (!ast.isAtivo())
continue;
// Asteroides começam fora da tela
if (ast.getPy() < ast.getAltura() * -2 ||
ast.getPy() > ast.getAltura() + altura) {
ast.setAtivo(false);
continue;
}
if (ast.getPx() + ast.getLargura() < 0 ||
ast.getPx() > largura) {
ast.setAtivo(false);
continue;
}
Parasaberseestãoforadaáreapermitida,verificamosseaposi çãodo
objetoestáalémouaquémdaposi çãoinicialdoelemento,comumpouco
maisdemargemnoeixoY.Ojogadorganhapontosquandooasteroideé
atingidoporumtirodeacordocomavelocidadedele,entãoasteroidesmais
rápidosdãomaispontos.
for (Tiro tiro : tiros) {
if (Util.colide(ast, tiro)) {
209
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 232

8.4. Jogandoocódigo CasadoCódigo
ast.setAtivo(false);
tiro.setAtivo(false);
pontos += ast.getVel();
break;
}
}
if (Util.colide(ast, nave)) {
ast.setAtivo(false);
nave.setLargura(nave.getLargura() - 2);
nave.setAltura(nave.getAltura() - 2);
nave.inverteCor();
Util.centraliza(nave, largura, altura);
continue;
}
ast.atualiza();
}
Quandooasteroideatingeanave,elaficadoispixelsmenornalargura
ealtura,etemsuacorinvertida. Comoseutamanhofoialterado,precisa-
moscentralizá-lanatelanovamente. Porfim,verificamosseostirosrema-
nescentes(queestãoativos)acabaramnoespa ço(saíramdatela)paraserem
inativados,ouatualizados.
for (Tiro tiro : tiros) {
if (!tiro.isAtivo())
continue;
if (Util.saiu(tiro, largura, altura))
tiro.setAtivo(false);
else
tiro.atualiza();
}
Osdoismétodosauxiliaresqueveremosaseguir, adicionarTiroe
maisAerolitos,sãoosresponsáveispelodesafiodojogo. Emboranosso
210
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 233

CasadoCódigo Capítulo8. Umjogodeânguloserota ções
arraydetirostenhaumtamanhofixo,nãolimitamososdisparosdojoga-
dor.Utilizamoso contadorTiroparairdoúltimoatéoprimeiroíndicedo
array,eentãovoltamosparaoúltimo.
Comoestamosreaproveitandoamesmainstânciadaclasse Tiro,pode
acontecerdeotirosumirdatelaantesdesairdelaoudecolidircomumini-
migo.Paraevitarqueissoaconte ça,poderíamospercorreroarrayembusca
deumtiroinativoemvezdeusarmosumcontador(faremosalgosimilarcom
os asteroides).
Oparâmetro anguloquerecebemoséoqueconsideramosserafrente
danave,ondedesenhamosoquadradoverde.Paraodisparosaircentralizado
comanave,usamosaposi çãodanavemaismetadedasualarguramenosa
metadedalarguradotiroparaposicioná-lonoeixoX,oequivalenteparao
eixoY.Issoésimilaraoquefizemosparacentralizaroselementosnatela.
private void maisAerolitos() {
int contador = 0;
for (int i = 0; i < aerolitos.length; i++) {
if (contador == adiciona)
break;
Asteroide ast = aerolitos[i];
if (ast.isAtivo())
continue;
contador++;
ast.setAtivo(true);
A quantidade de aerólitos a serem adicionados depende do valor de
adiciona(fixadoem2),maspodeacontecerdenãoadicionarmosnenhum
inimigocasotodosestejamativos.
Osasteroidespossuem5tamanhosdiferentes,de10até50pixels,eco-
meçam em qualquer ponto do eixo X. Mas, no eixo Y, ou começam na
parte superior ou inferior da tela, resultado que obtemos multiplicando
rand.nextInt(2)(queretorna0ou1)pela alturadatela,subtraindo
aalturadoelementoseelecome çarnapartesuperior.
211
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 234

8.4. Jogandoocódigo CasadoCódigo
ast.setAltura((rand.nextInt(4) + 1) * 10);
ast.setLargura(ast.getAltura());
ast.setPx(rand.nextInt(largura));
int py = rand.nextInt(2) * altura;
if (py == 0)
py = py - ast.getAltura();
ast.setPy(py);
ast.setVel(rand.nextInt(3) + 1);
Outravaria çãoocorrenavelocidadedosinimigos,quevaide1até3e
influenciamnapontua ção. Porém,aprincipalvaria çãoestánasele çãodo
mododejogoondetemososfamosos:fácil,normaledifícil.
switch (Jogo.nivel) {
case 0:
// Modo Facil: vai para qualquer lado
ast.setAngulo(rand.nextInt(360));
break;
case 1:
// Modo Normal: vai em ângulos próximos
// a nave do jogador
if (ast.getPy() <= 0)
ast.setAngulo(90);
else
ast.setAngulo(270);
break;
Noprimeiromodo,osaerólitosvãoemqualquerdire çãoaleatoriamente
emuitospassamlongedojogador. Jánosegundo,elesvãoemângulosre-
tos,tendomaischancesdeatingiranave.Omododifícil,tambémchamado
de Teleguiado,nãotemessenomeàtoa,jáquetodososinimigosvãona
direçãodojogador.
Comoelestêmposiçõesaleatórias,precisamoscalcularoângulocombase
naposiçãodoaerólitoedanave,obtidacom Math.atan2.
212
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 235

CasadoCódigo Capítulo8. Umjogodeânguloserota ções
default:
// Modo Dificil: todos vão em direção a
// nave do jogador
float arco = (float) Math.atan2(
nave.getPy() - ast.getPy(),
nave.getPx() - ast.getPx());
float angulo = (float) Math.toDegrees(arco);
ast.setAngulo(angulo);
break;
}
}
}
Passamosdoisparâmetrosparaafun ção Math.atan2,ambosenvol-
vendoaposi çãodosnossosobjetos,sendoelesodestinosubtraídopelaori-
gem.Nestecaso,odestinoénossoobjeto nave,eaorigem,nossoasteroide
ast.
ObservequepassamosnoprimeiroparâmetrooeixoY,aocontrárioda
maioriadasfun çõesqueutilizamos,foraisso,bastalembrardequesubtraí-
mosaposi çãoparaondequeremosirdaposi çãoondeestáoobjetoquevai
semover,anãoserquesequeirairparaoladooposto,útilemalgoritmosde
fuga.
Comoestamostrabalhandocomângulosemgraus,convertemosoresul-
tadocom Math.toDegreese,depois,nahorademovimentaroelemento
dentrodoseumétodo atualiza,convertemosnovamenteemradianoscom
Math.toRadians.Então,quandosesentirmaisàvontadeaotrabalharcom
ângulos,prefirausarradianosparafazermenosconversões.
Vimosométodo Math.atan2naprática,masseprecisardeumpouco
de teoria, recomendo http://gamedev.stackexchange.com/questions/14602/
what-are-atan-and-atan2-used-for-in-games(conteúdoeminglês).
8.5 C odificando o jogo
Primeiro, vimos como aplicar efeitos de rotação, escalonamento e
transição aos nossos desenhos, utilizando as classesGraphics2D e
213
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 236

8.5. Codificandoojogo CasadoCódigo
AffineTransform. Criamosalgunsexemplosquevocêpodeconferirna
classe RotacaoTeste.java,emhttps://github.com/logicadojogo/fontes/
tree/master/Cap08,dentrodopacoteteste.
Nossa classe Elemento agora mantém uma instância de
AffineTransform para aplicarmos efeitos em nossos novos objetos
deformatemporária: Asteroide, Navee Tiro. Antesdeaplicarmos
qualquertransformada,usamos afAnteriorparamanterastransforma-
dasanterioresdoobjeto Graphics2D,mesmoqueaindanãoestejamos
aplicandonenhumefeito(queveremosnopróximocapítulo).
Nãoestamosutilizandoasvariáveis dxe dy,easvariáveis pxe pyagora
sãodotipo float,paratermosumamovimenta çãomaisfluidaparanossos
elementosqueusamângulos.
Utilizamosvaloresemgrausde0ºa360º,masasprincipaisfun çõesmate-
máticasdaclasse Mathquevimostrabalhamcomradianos.Assim,usamos
Math.toRadiansparaconvertergrausemradianos,e Math.toDegrees
pararadianosemgraus.
Alógicamaisinteressantedessejogoestáemfazerosasteroidesperse-
guiremanavedojogador.Paraisso,primeiroobtemosoângulocorretoen-
treosdoisobjetoscom Math.atan2,depoispassamosesseângulopara
Math.cose Math.sin,quenosretornamocossenoeseno,respectiva-
mente.Porfim,usamosessesvaloresparaatualizarmosamovimenta çãodo
nossopersonagem,cossenoparaoeixoXesenoparaoeixoY.
Temosumbomexemplodecomocriarníveisdiferentesdedificuldade
paraojogador,quenomeamoscomo: Sem radar(fácil),Com radar(normal)
e T eleguiado(difícil).Naprimeiraop ção,oanguloéqualquercoisaentre0ºe
359º,entãomuitospassarãolongedojogador,podendonemchegaraaparecer
natela.Nasegundaop ção,aomenosgarantimosqueosinimigoscruzarãoa
telanavertical.Jáaúltimaéimplacável,obtemosascoordenadasdanavee
direcionamostodasaspedrasespaciaisparaela.
Não fizemos aqui
• Movimentaranavepelatela;
• Controlaranavecomomouse.
214
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 237

CasadoCódigo Capítulo8. Umjogodeânguloserota ções
Melhore você mesmo
• Contaracertosseguidosparaaumentarapontuaçãodojogador;
• Formasdetiroqueusemângulosdiferentes;
• Utilizarimagens.
8.6 R esumo
Vimosnestecapítulocomoaplicartransformadasemnossosdesenhoseama-
temáticanecessáriaparaojogofuncionar.Usaremosmaisdoquefoiapresen-
tadonopróximocapítuloe,mesmoassim,ambosostópicossãomaisabran-
gentesdoqueconseguiremoscobrir.
Graçasàstransforma çõesdodesenho,nósconseguimoscriardiversos
efeitosdentrodoprópriojogo,incluindoanima ções.Jogosqueenvolvamge-
ometriaefísicaficammaisfáceiscomasclassesemétodosqueoJavanos
fornece,epossodizerpormimquesenoecossenonuncasefizeramtãoúteis
antesdeutilizá-losemjogos.
215
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 238

E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 239

Capítulo9
Asteroids:ojogoquesabe
representarafísica
LyleRainsdeuaideia,eEdLoggacolocouemmaisde70milmáquinasde
jogosnosEstadosUnidosem1979,vendidaspelaAtari. Porém,onúmero
maisimpressionanteéodeumgarotoquejogouAsteroidspor36horasantes
decansar.
Utilizandográficosvetoriais,ojogosediferenciavadamaioriadosjogos
daépoca(queerampixelizados),tendovelocidadeenitidez,alémdeguardar
asiniciais(ou3letrasquaisquer)dosjogadoresquepontuassemmaise,é
claro,eradeumafísicadesafiadora.
Guardamosparaestecapítulo:
• AnimaçãodeSprite;
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 240

9.1. Umébom,doisémultiplayer CasadoCódigo
• Efeitodeaproximação(zoom);
• Melhoriasnoloopdojogo.
Fig.9.1:Ângulos:ojogo
9.1 U m é bom , dois é multiplayer
Asteroidspodeserantigo,masseusconceitossãousadoseminúmerosjo-
gosatuais,inclusivenojogodocapítuloanterior.Anossaversãodestecapí-
tulotambémbrincarábastantecomrotaçõeseângulos,masdestavezusando
imagens,alémdapossibilidadededoisjogadores(modomultijogadorou
multiplayer)–oprimeirocontroladopeloteclado,eosegundopelomouse,
disputandoquemdestróimais(ouerramenos)asteroides.
Concentramostodasasimagensdojogoemobjetosestáticosnaclasse
Recursos.java:
218
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 241

CasadoCódigo Capítulo9. Asteroids:ojogoquesaberepresentarafísica
public enum Imagem {
FUNDO, JOGADOR_A, JOGADOR_B, TIRO_A, TIRO_B,
AST_A, AST_B, AST_C, EXPLOSAO_AST, COLISAO_AST
}
private static final String DIR_IMG = "imagens/";
private static ImageIcon[]
imagens = new ImageIcon[Imagem.values().length];
Centralizamos todas as imagens aqui, e quem precisar pede um
ImageIconutilizandoopróprio enumdaclasse. Assim,sequisermosre-
nomearousubstituirumaimagem(ouatémesmorefazertodaalógicade
carregamento),sóprecisamosalterarumarquivo.
public static void carregarImagens() {
imagens[Imagem.FUNDO.ordinal()] =
new ImageIcon(DIR_IMG + "fundo.png");
imagens[Imagem.JOGADOR_A.ordinal()] =
new ImageIcon(DIR_IMG + "nave_jogador_1.png");
imagens[Imagem.JOGADOR_B.ordinal()] =
new ImageIcon(DIR_IMG + "nave_jogador_2.png");
imagens[Imagem.TIRO_A.ordinal()] =
new ImageIcon(DIR_IMG + "tiro.png");
imagens[Imagem.TIRO_B.ordinal()] =
new ImageIcon(DIR_IMG + "tiro.png");
Amaioriadasimagensfoiobtidanestegranderepositóriochamadointer-
net,emumabuscaporEspa çoSideral,MeteoritoseBattlestarparaasnaves
dosjogadores,queapenastêmcordiferente.Nósmesmosfizemosostirose
asexplosõese,mesmootirosendoomesmoparaosdoisjogadores,nossa
classejáestápreparadaparacarregarimagensdiferentesparacadaum.
imagens[Imagem.AST_A.ordinal()] =
new ImageIcon(DIR_IMG + "asteroide_grande.png");
imagens[Imagem.AST_B.ordinal()] =
new ImageIcon(DIR_IMG + "asteroide_medio.png");
imagens[Imagem.AST_C.ordinal()] =
new ImageIcon(DIR_IMG + "asteroide_pequeno.png");
219
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 242

9.1. Umébom,doisémultiplayer CasadoCódigo
imagens[Imagem.EXPLOSAO_AST.ordinal()] =
new ImageIcon(DIR_IMG + "explosao_asteroid.png");
imagens[Imagem.COLISAO_AST.ordinal()] =
new ImageIcon(DIR_IMG + "colisao_asteroid.png");
}
public static ImageIcon getImagem(Imagem img) {
return imagens[img.ordinal()];
}
Ométodo carregarImagenséchamadoantesdequalquercenárioser
iniciadoecarregatodasasimagensdojogo. Sefosseumjogomaior,com
diversoscenáriosecompostospormuitasimagens,oidealseriacarregaras
imagensespecíficasdecadacenário,enãotodasdeumavez,masestenãoé
ocaso.
Veremosalgumasdessasimagensaolongodocapítulo,lembrandodeque
todasestãonapasta imagens,naraizdoprojeto.
Nossabibliotecadecódigoaumentou,etodaamatemáticanecessária
(vistanocapítuloanterior)foimovidaparaaclasse MatUtil.java:
public static float moveAnguloEmX(float angulo) {
return (float) Math.cos(Math.toRadians(angulo));
}
public static float moveAnguloEmY(float angulo) {
return (float) Math.sin(Math.toRadians(angulo));
}
Paramovimentarospersonagenscombaseemseusângulos,usaremos
moveAnguloEmXe moveAnguloEmY,quefazemaconversãopararadianos
ede doublepara float.Dessaforma,calculamosoânguloemcadaeixo
separadamente,mastambémtemosummétodoparaaplicaromovimento
diretamenteno Elemento:
public static void move(Elemento el, float angulo, int vel) {
float cos = (float) Math.cos(Math.toRadians(angulo));
220
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 243

CasadoCódigo Capítulo9. Asteroids:ojogoquesaberepresentarafísica
float sen = (float) Math.sin(Math.toRadians(angulo));
el.setPx(el.getMovPx() + cos * vel);
el.setPy(el.getMovPy() + sen * vel);
}
public static float corrigeGraus(float graus) {
if (graus < 0)
graus += 360;
else if (graus > 360)
graus -= 360;
return graus;
}
Comoestamosconvertendonossovaloremgrauspararadianos,nãopre-
cisamosnospreocuparseovalorpassadofogedonossorangede0ºa360º.
Mesmoassim,utilizamosafun ção corrigeGrausparatermaiorcontrole
sobreele.
Nojogoanterior,calculamosadire çãoentreoasteroideeanave,mas
nesteprecisamoscalcularadire çãoentreanavedosegundojogadoreoclique
domouse.
public static float calculaDirecao(int xDestino, int yDestino,
int xOrigem, int yOrigem) {
return (float) Math.toDegrees(
Math.atan2(yDestino - yOrigem,
xDestino - xOrigem) );
}
public static float calculaDirecao(Elemento origem,
Elemento destino){
return (float) Math.toDegrees(
Math.atan2(destino.getPy() - origem.getPy(),
destino.getPx() - origem.getPx()) );
}
Aprimeirachamadadométodo calculaDirecaorecebequatrointei-
rosquerepresentamoseixosXeYdopontodedestinoedeorigem.Sendo
221
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 244

9.1. Umébom,doisémultiplayer CasadoCódigo
queodestinoseráocliquedomouseeaorigemaposi çãodanavenomo-
mentodoclique.Asegundachamadadométodofazomesmo,levandoem
consideraçãoaposi çãoentredoiselementos,nãoutilizadanessaversãono
jogo.
Oselementosquecompõemojogosãoosmesmosdojogoanterior(
Nave, Tiroe Asteroide),mascomcomportamentosdiferentes. Além
disso,implementamosumefeitodezoomusando scalee translate,
queocorrerátodavezqueasnavesdosjogadoressechocarem.
Essastransformaçõessãofeitasantesdedesenharmososelementos,en-
tão,éprecisoagregarastransformadasemvezdeapagá-las.Exploramostrês
formasdiferentesdefazermosessaagrega ção,ecadaumdostrêselementos
utilizauma.
Quandoumanaveatingeumasteroide,ojogadorganhapontos,equando
elaatingeváriosseguidossemerrar,ojogadorganhamaispontosainda.Para
saberqualnaveefetuouodisparo,o Tiroguardaareferênciadoobjeto
Nave:
public class Tiro extends Elemento {
private Nave nave;
private float angulo;
@Override
public void atualiza() {
if (!isAtivo())
return;
MatUtil.move(this, angulo, getVel());
}
Paradesenharotiro,usamosdoisobjetos AffineTransform:umpara
guardarmosatransforma çãodoobjeto Graphics2Dantesdeaplicarmos
asnossastransforma ções( afAnterior),eoutroparaaplicarmosastrans-
formaçõesreferentesaotiro( af),issodepoisdemesclamosatransformada
anteriorcom af.setTransform(afAnterior).
@Override
public void desenha(Graphics2D g) {
222
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 245

CasadoCódigo Capítulo9. Asteroids:ojogoquesaberepresentarafísica
if (!isAtivo())
return;
afAnterior = g.getTransform();
af.setTransform(afAnterior);
af.rotate(Math.toRadians(angulo),
getLargura() / 2 + getPx(),
getAltura() / 2 + getPy());
af.translate(getPx(), getPy());
g.setTransform(af);
g.drawImage(getImagem().getImage(), 0, 0, null);
g.setTransform(afAnterior);
}
Esseéoprimeirodostrêsexemploseéapiorpráticaparaestecaso,já
queusamosdoisobjetos AffineTransform–agora,vocêsabeoquenão
fazer.Nostrêselementos,ométodo setImagemajustaalarguraealturado
elementodeacordocomaalturaelarguradaimagem:
@Override
public void setImagem(ImageIcon img) {
super.setImagem(img);
super.setAltura(img.getIconHeight());
super.setLargura(img.getIconWidth());
}
public float getAngulo() {
return angulo;
}
public void setAngulo(float angulo) {
this.angulo = angulo;
}
public Nave getNave() {
return nave;
}
223
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 246

9.1. Umébom,doisémultiplayer CasadoCódigo
public void setNave(Nave nave) {
this.nave = nave;
}
}
Nosso Asteroidetemquatrotamanhos:grande,médio,pequenoepo-
eira.Elecome çanotamanhograndee,todavezquecolidecomotirooua
nave,diminui(divide),atéchegaraotamanhopoeira.
public class Asteroide extends Elemento {
public enum Tamanho {
GRANDE, MEDIO, PEQUENO, POEIRA;
}
private float angulo;
private float anguloRotacao;
private Tamanho tamanho = Tamanho.GRANDE;
@Override
public void atualiza() {
if (!isAtivo())
return;
MatUtil.move(this, angulo, getVel());
anguloRotacao = MatUtil.corrigeGraus(
anguloRotacao + getVel());
}
Nesteexemplo,usandosomenteumobjeto AffineTransform:
@Override
public void desenha(Graphics2D g) {
if (!isAtivo())
return;
af.setTransform(g.getTransform());
af.rotate(Math.toRadians(anguloRotacao),
getLargura() / 2 + getPx(),
getAltura() / 2 + getPy());
af.translate(getPx(), getPy());
224
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 247

CasadoCódigo Capítulo9. Asteroids:ojogoquesaberepresentarafísica
g.drawImage(getImagem().getImage(), af, null);
}
...
Essemétododedesenhoparecebemmelhorqueaformaquefizemos
paradesenharotiro. Notequenãoinserimosnossastransforma çõesno
Graphics2D,apenasapassamoscomoparâmetronométodo drawImage.
Ométodo divide,alémdeacharopróximotamanhodoasteroide,re-
tornafalsoseelenãopudermaisserdividido.
public boolean divide() {
switch (tamanho) {
case GRANDE:
tamanho = Tamanho.MEDIO;
setImagem(Recursos.getImagem(
Recursos.Imagem.AST_B));
break;
case MEDIO:
tamanho = Tamanho.PEQUENO;
setImagem(Recursos.getImagem(
Recursos.Imagem.AST_C));
break;
case PEQUENO:
tamanho = Tamanho.POEIRA;
default:
break;
}
return tamanho != Tamanho.POEIRA;
}
Alémdemudarmosaimagem(econsequentementeotamanhodoele-
mento),otamanhotambéminfluencianospontosqueojogadorrecebe:
...
public short getPonto() {
switch (tamanho) {
case GRANDE:
225
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 248

9.1. Umébom,doisémultiplayer CasadoCódigo
return 10;
case MEDIO:
return 15;
case PEQUENO:
return 20;
case POEIRA:
default:
return 0;
}
}
}
Ométodo getPontogarantequeaspedrasmenoresdeemmaispontos
queasmaiores.Porúltimo,masnãomenosimportante,nossaclasse Nave.
Dessavez,nossanavesemovepelatela,vagandopelagaláxiasemfreio.
Então,quandoojogadoraceleraemumadire ção,eleficanessadire çãoaté
aceleraremoutra,oucolidircomoutroobjeto.
public class Nave extends Elemento {
public static final float ROTACAO_VEL = 5f;
public static final float LIMITE_VEL = 9f;
private float angulo;
private float velEmX;
private float velEmY;
private short pontos;
private short erros;
private short seguidos;
Paracontrolaravelocidadedarota çãodanave,usamos ROTACAO_VEL
e,paraelanãoganharvelocidadeinfinitamente, LIMITE_VEL.Paraelades-
lizarsobreatelacomoumdiscodehóquei,utilizamos velEmXe velEmY,
quemantêmasvelocidadesdemovimenta çãonoseixos.Alémdesomaros
pontosdojogador,somamosos erroseosacertos seguidos.
@Override
public void atualiza() {
226
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 249

CasadoCódigo Capítulo9. Asteroids:ojogoquesaberepresentarafísica
if (!isAtivo())
return;
setPx(getPx() + velEmX);
setPy(getPy() + velEmY);
}
Mantemosanavesempreemmovimentoatualizandosuaposi ção. Em
nossaterceiraversãodométodo desenha, tambémusamosapenasum
AffineTransformparaguardamosastransforma çõesanteriores. Entre-
tanto,essaversãolevavantagem,porquenãocriamosumnovoobjeto,apenas
usamos afAnteriorcomorecipientedareferênciadoobjetojáexistente.
@Override
public void desenha(Graphics2D g) {
if (!isAtivo())
return;
float rad = (float) Math.toRadians(getAngulo());
afAnterior = g.getTransform();
g.rotate(rad,
getLargura() / 2 + getPx(),
getAltura() / 2 + getPy());
g.translate(getPx(), getPy());
g.drawImage(getImagem().getImage(), 0, 0, null);
g.setTransform(afAnterior);
}
Ospontossãomultiplicadospelaquantidadedetirosseguidos,quesem-
prevoltapara0quandoojogadorerraouéatingido. Consideremosqueo
jogadorerrouotiroquandoelesairdatela,entãoincrementamosocontador
deerros.
...
public void somaPontos(short p) {
seguidos++;
227
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 250

9.1. Umébom,doisémultiplayer CasadoCódigo
pontos += p * seguidos;
}
public void errou() {
seguidos = 0;
erros++;
}
Consertamosnossanave,eagoraelapodesemover.Porém,sem hyper-
drive,elanãopodealcan çaravelocidadedaluz,entãolimitamosavelocidade
máximanosmétodos setVelEmXe setVelEmY.
...
public float getVelEmX() {
return velEmX;
}
public void setVelEmX(float vel) {
if (vel > LIMITE_VEL)
vel = LIMITE_VEL;
else if (vel < -LIMITE_VEL)
vel = -LIMITE_VEL;
this.velEmX = vel;
}
public float getVelEmY() {
return velEmY;
}
public void setVelEmY(float vel) {
if (vel > LIMITE_VEL)
vel = LIMITE_VEL;
else if (vel < -LIMITE_VEL)
vel = -LIMITE_VEL;
this.velEmY = vel;
}
228
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 251

CasadoCódigo Capítulo9. Asteroids:ojogoquesaberepresentarafísica
//... Outros getters e setters
public void danos() {
errou();
velEmX = velEmX * -0.5f;
velEmY = velEmY * -0.5f;
}
}
Quandoocorrercolisõesdanavecomosasteroides,elasofrerádanos
esuapuni çãoseránapontua çãocomumefeitodeimpactofazendo-aper-
dervelocidade. Paraisso,chamamosométodo errou(),emultiplicamos
velEmXe velEmYpor -0.5.
Nota
Asteroidsguardavaapenastrêsletrasdevidoàlimita çãodehardware
daépoca,masnãoconsigoimaginaromotivodeosdiversosjogosde
fliperamaquevieramdepoiscontinuaremaceitandoapenastrês.
9.2 D ividir para destruir
Mesmoquenãotenhasomnoespa ço,nossojogoteráexplosõese,paranão
ficarfeioperanteojogooriginal–noqualanavedojogadorseparteempe-
daçospelocosmos–,teremosduasanimaçõesbásicas:umaparaquandoum
tiroacertaumasteroide,eoutraquandoasrochasespaciaisacertamnossas
naves.
A primeira sequência de imagens (explosao_asteroid.png)
é para quando um tiro atinge um asteroide, e a segunda (
colisao_asteroid.png) é para quando a nave colide com um aste-
roide.
229
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 252

9.2. Dividirparadestruir CasadoCódigo
Fig.9.2:Colisãodanavecomasteroides
Fig.9.3:Destruindoasteroides
Nossasexplosõessãocontroladaspelanovaclasse Animacao.java,que
apenaspercorrecolunaporcolunadonossospritecomumpequenointervalo
entrecadaquadro.
public class Animacao extends Elemento {
private short coluna;
private short temporizador;
public Animacao(ImageIcon imagem) {
super.setImagem(imagem);
}
@Override
public void atualiza() {
if (!isAtivo())
return;
if (coluna == 6) {
setAtivo(false);
} else if (temporizador == 2) {
coluna++;
temporizador = 0;
} else {
230
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 253

CasadoCódigo Capítulo9. Asteroids:ojogoquesaberepresentarafísica
temporizador++;
}
}
Utilizamos colunaparaobteraimagemquequeremosdesenhardo
sprite,e temporizadorparacontrolarotempodesuaexibi ção. Nossos
doisspritessãosimples,amboscomumalinhaeseiscolunas.Assim,quando
nosso temporizadorforiguala2,incrementamosacolunadosprite,ede-
poisdeexibirmosaúltima,encerramosaanima ção.
@Override
public void desenha(Graphics2D g) {
if (!isAtivo())
return;
// Largura da moldura
int largMoldura = getImagem().getIconWidth() / 6;
// Largura e altura do recorte da imagem
int largImg = largMoldura * coluna;
int altImg = getImagem().getIconHeight();
g.drawImage(getImagem().getImage(),
getPx(), getPy(),
getPx() + largMoldura,
getPy() + altImg, largImg,
0, largImg + largMoldura,
altImg, null);
}
@Override
public void setAtivo(boolean ativo) {
super.setAtivo(ativo);
coluna = 0;
temporizador = 0;
}
}
Paradesenharcadaquadro,usamosnossajáconhecidafórmulaparaob-
231
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 254

9.2. Dividirparadestruir CasadoCódigo
teraparteaserdesenhadadosprite.Quandoativamosoelemento,reinici-
amosaanima ção,assimreaproveitamosomesmoobjetoporumlado;por
outro,interrompemosaanima çãocasoelaaindanãotenhaterminado.
Aoseratingido,oasteroidesedivideemdoisatéquenãopossamaisser
dividido.Emvezdecriarmosnovasinstânciasdaclasse Asteroideacada
divisãoduranteojogo,criamosumnúmeroequivalentejánoinícioeasdei-
xamosinativadas.Tambémreaproveitamosainstânciadoobjetoaoinvésde
destruí-lo.
Comodesenhamosapenastrêstamanhosdeasteroides(grande,médioe
pequeno),paracadaelementoprecisaremosdemais3,tendoumtotalde4
novasinstânciasaototal.Então,seiniciarmosojogocom5rochasgrandes,
precisamosdeixarespa çonoarraypara20(5*4).
Fig.9.4:Dividirereaproveitar
Paracada Asteroidequeteremosnatela,precisamosdequatronovas
instâncias,quesãorepresentadosnaimagempelasrochascomafrase“Novo”.
Mesmosenósnãoestivéssemoseconomizandomemória,evitandocriar
novosobjetos,nossojogo,portertãopoucoselementos,nãoficarialento.
Essamedi çãoéfeitapormeiodataxadequadrosporsegundo,quepode
oscilar,masnãoficarabaixodoquefoidefinido–nossos20quadrospor
segundo(FPS).
232
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 255

CasadoCódigo Capítulo9. Asteroids:ojogoquesaberepresentarafísica
Comoébemprovávelqueojogoquevocêvaidesenvolverfiquetão
grandequeprecisefazeressamedi ção,dedicamosaúltimapartedapróxima
seçãoparafalardisso.
9.3 J ogando o código
Vimososelementosquecompõemnossojogo,agoraveremoscomoaclasse
JogoCenario.javaorquestraessasinfoniaespacial.Vamosgerenciarnos-
sosdoisjogadoresrepresentadospor navJogUme navJogDoisdeforma
individual.Setivéssemosmaisjogadores,faríamosdiferente,utilizandoum
array.
Começamosojogocom10asteroidesgrandes( qtdeInicial),masa
quantidadefinalderochasnatelapodechegaraquatrovezesaquantidade
inicial.
public class JogoCenario extends CenarioPadrao {
...
private Nave navJogUm;
private Nave navJogDois;
private int qtdeInicial = 10;
private int contadorTiro;
private int contadorAsteroides;
private Tiro[] tiros = new Tiro[16];
private Asteroide[] aerolitos =
new Asteroide[qtdeInicial * 4];
private Animacao colisaoAst;
private Animacao explosaoAst;
...
private float graus;
private boolean ampliar;
private boolean reduzir = false; // Apenas exemplo
private final float escala = 5 / 100f;
// 5% do tamanho da tela
233
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 256

9.3. Jogandoocódigo CasadoCódigo
private static final AffineTransform AF_VAZIO =
new AffineTransform();
Duranteojogo,usamosapenasdoisobjetosparagerenciarnossasduas
animações,umparacadatipodecolisão. Então,emboraelastenhamuma
curtíssimaduração,algumasvezesaanima çãoéinterrompidaecome çaem
outraposiçãodatela.Nomododedoisjogadores,quandoasnavescolidirem
entresi,definimos ampliarcomoverdadeiro,aplicandoumefeitodezoom
de5%nateladojogo,valordavariável escala.
Deixamosumexemplodecomoaplicaroefeitoinversoe,paratestá-lo,
bastaalterar reduzirpara true. UtilizamosAF_VAZIOparadesfazero
efeitodeaproxima ção.
Aprincipaldiferen çadométodo carregardestejogoedojogoanterior
équeusamosimagens,todasobtidaspormeiodaclasse Recursos.java,e
nossasrochassãocriadascomvelocidade,ânguloeposi çãorandômicas.
// método carregar:
fundo = Recursos.getImagem(Recursos.Imagem.FUNDO);
texto.setCor(Color.WHITE);
colisaoAst = new Animacao(
Recursos.getImagem(Recursos.Imagem.COLISAO_AST));
explosaoAst = new Animacao(
Recursos.getImagem(Recursos.Imagem.EXPLOSAO_AST));
for (int i = 0; i < tiros.length; i++) {
tiros[i] = new Tiro();
tiros[i].setVel(15);
tiros[i].setImagem(Recursos.
getImagem(Recursos.Imagem.TIRO_A));
}
for (int i = 0; i < aerolitos.length; i++) {
aerolitos[i] = new Asteroide();
aerolitos[i].setImagem(Recursos.
getImagem(Recursos.Imagem.AST_A));
234
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 257

CasadoCódigo Capítulo9. Asteroids:ojogoquesaberepresentarafísica
if (i < qtdeInicial) {
aerolitos[i].setAtivo(true);
aerolitos[i].setVel(rand.nextInt(3) + 3);
aerolitos[i].setAngulo(rand.nextInt(360));
aerolitos[i].setPx(rand.nextInt(largura));
aerolitos[i].setPy(rand.nextInt(altura));
contadorAsteroides++;
}
}
Asnavesdosjogadoresiniciamnocentrodatela,sendoqueanavedo
segundojogadorsóficaráativaseaop çãodoisjogadores–valorsalvoem
Jogo.numeroJogadores–forescolhidanatelainicial.
Osegundojogadorpodeentraraqualquermomentoduranteojogopres-
sionandoobotãodetiro,configuradoparaocliquedobotãoprincipaldo
mouse.
navJogUm = new Nave();
navJogUm.setAtivo(true);
navJogUm.setImagem(Recursos.
getImagem(Recursos.Imagem.JOGADOR_A));
navJogDois = new Nave();
navJogDois.setAtivo(Jogo.numeroJogadores > 0);
navJogDois.setImagem(Recursos.
getImagem(Recursos.Imagem.JOGADOR_B));
Util.centraliza(navJogUm, largura, altura);
Util.centraliza(navJogDois, largura, altura);
navJogUm.setPy(navJogUm.getPy() - navJogUm.getAltura() / 2);
navJogDois.setPy(navJogDois.
getPy() + navJogDois.getAltura() / 2);
Apóscentralizarmososjogadores,aplicamosumespa çoentreelespara
quenãoestejamcolidindonoiníciodojogo.Ométodo atualizarmudou
bastantee,nessamudan ça,cadajogadorganhouummétodoseparadopara
235
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 258

9.3. Jogandoocódigo CasadoCódigo
interaçõesdecontrole,jáquecontrolarpelotecladodiferedocontrolepelo
mouse.
@Override
public void atualizar() {
if (estado != Estado.JOGANDO) {
return;
}
controlaJogadorUm();
controlaJogadorDois();
if (Util.colide(navJogUm, navJogDois)) {
ampliar = true;
navJogUm.setAngulo(
MatUtil.corrigeGraus(navJogUm.getAngulo() + 90));
navJogDois.setAngulo(
MatUtil.corrigeGraus(navJogDois.getAngulo() - 90));
} else {
ampliar = false;
}
navJogUm.atualiza();
navJogDois.atualiza();
colisaoAst.atualiza();
explosaoAst.atualiza();
corrigePosicao(navJogUm);
corrigePosicao(navJogDois);
Sedetectarmoscolisãoentreasnaves,alémdeampliaratela,bagun ça-
mossuasnavega çõessomandoesubtraindo90ºgrausdecadaumarespec-
tivamente. Paranossasnavesnãosumirempelouniversoaosaíremdatela,
corrigimossuaposi çãofazendo-asapareceremdoladooposto,issogra çasao
método corrigePosicao,movidoparaclasse Util.
236
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 259

CasadoCódigo Capítulo9. Asteroids:ojogoquesaberepresentarafísica
Todavezqueumtirocolidircomumasteroide,posicionamosereini-
ciamosaanima ção explosaoAst. Fazemosomesmocom colisaoAst
quandooasteroidecolidecomanave.
for (int i = 0; i < contadorAsteroides; i++) {
Asteroide ast = aerolitos[i];
if (!ast.isAtivo())
continue;
for (Tiro tiro : tiros) {
if (Util.colide(ast, tiro)) {
tiro.setAtivo(false);
explosaoAst.setAtivo(true);
explosaoAst.setPx(ast.getPx());
explosaoAst.setPy(ast.getPy());
if (ast.divide())
novaParteAsteroide(ast);
else
ast.setAtivo(false);
tiro.getNave().somaPontos(ast.getPonto());
break;
}
}
Emambasascolisões,verificamosseépossíveldividiro Asteroide
antesdeativarmosmaisumpeda ço,masasomadepontosocorresomente
nacolisãocomotiro. Acolisãodanavecomosasteroideséparecida,mas
quandoelaocorre,anavesofredanos.
Comoo Tirosabedequenavefoidisparado,édelequeobtemosa Nave
parasomarospontos. Alógicaestánopróprio Asteroidequedefineo
pontodeacordocomseutamanho.
if (Util.colide(ast, navJogUm)) {
navJogUm.danos();
237
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 260

9.3. Jogandoocódigo CasadoCódigo
colisaoAst.setAtivo(true);
colisaoAst.setPx(navJogUm.getPx());
colisaoAst.setPy(navJogUm.getPy());
if (ast.divide())
novaParteAsteroide(ast);
else {
ast.setAtivo(false);
continue;
}
} else if (Util.colide(ast, navJogDois)) {
navJogDois.danos();
colisaoAst.setAtivo(true);
colisaoAst.setPx(navJogDois.getPx());
colisaoAst.setPy(navJogDois.getPy());
if (ast.divide())
novaParteAsteroide(ast);
else {
ast.setAtivo(false);
continue;
}
}
ast.atualiza();
corrigePosicao(ast);
}
Seoasteroidejáviroupoeira,inativamo-loepulamosparaapróxima
iteraçãodola ço. Apenasrepetimosacondi çãotrocando navJogUmpor
navJogDoisparanãosepararmosessapartedocódigoemumnovomé-
todo,facilitandoaleitura.
Nofimdola ço,atualizamosecorrigimosaposi çãodonossoobjeto.En-
tretanto,antesdeterminarmosométodo atualizar,precisamosverificar
ostirosremanescentes.
for (Tiro tiro : tiros) {
if (!tiro.isAtivo())
238
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 261

CasadoCódigo Capítulo9. Asteroids:ojogoquesaberepresentarafísica
continue;
if (Util.saiu(tiro, largura, altura, 20)) {
tiro.setAtivo(false);
tiro.getNave().errou();
} else
tiro.atualiza();
}
}
Verificamosseotiroaindaestánolimitedatela;senãoestiver,consulta-
mosanavedeorigemdodisparoparadaratristenotíciadequedeelaerrou.
Notequeessaéumanovaversãodométodo Util.saiu,querecebeumpa-
râmetroamais,usadosomenteparadarumamargem(de20pixels)dolimite
datela,ficandoassim:
public static boolean saiu(Elemento e, int largura,
int altura, int margem) {
if (e.getPx() < -margem ||
e.getPx() + e.getLargura() > largura + margem)
return true;
if (e.getPy() < -margem ||
e.getPy() + e.getAltura() > altura + margem)
return true;
return false;
}
Hora de nos concentrarmos nos métodos menores, começando pela
formadepilotarcadanave.
public void controlaJogadorUm() {
graus = navJogUm.getAngulo();
if (Jogo.controleTecla[Jogo.Tecla.ESQUERDA.ordinal()])
graus -= Nave.ROTACAO_VEL;
239
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 262

9.3. Jogandoocódigo CasadoCódigo
else if (Jogo.controleTecla[Jogo.Tecla.DIREITA.ordinal()])
graus += Nave.ROTACAO_VEL;
navJogUm.setAngulo(graus);
Arotaçãoficoumaissimplificada,jáquepassamosalgunsmétodospara
aclasse MatUtil. Quandoopiloto/jogadorpressionarparacima,anave
aceleraránadireçãoemqueestiverapontada.
Elepodeatiraraomesmotempoemqueacelera,então,paranãoficar
estranho,émelhorqueotirosejamaisrápidoqueanave.
if (Jogo.controleTecla[Jogo.Tecla.CIMA.ordinal()]) {
float vx = navJogUm.getVelEmX();
float vy = navJogUm.getVelEmY();
vx += MatUtil.moveAnguloEmX(navJogUm.getAngulo());
vy += MatUtil.moveAnguloEmY(navJogUm.getAngulo());
navJogUm.setVelEmX(vx);
navJogUm.setVelEmY(vy);
}
if (Jogo.controleTecla[Jogo.Tecla.BC.ordinal()]) {
adicionarTiro(navJogUm);
Jogo.liberaTecla(Jogo.Tecla.BC);
}
}
Notequeométodo adicionarTiroagorarecebecomoparâmetroa
Naveresponsávelpelodisparo. Trocandootecladopelomouse,ocontrole
dosegundopilotoficouassim:
public void controlaJogadorDois() {
if (!navJogDois.isAtivo()) {
if (Jogo.controleTecla[Jogo.Tecla.MOUSE_A.ordinal()]) {
navJogDois.setAtivo(true);
Jogo.liberaTecla(Jogo.Tecla.MOUSE_A);
240
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 263

CasadoCódigo Capítulo9. Asteroids:ojogoquesaberepresentarafísica
}
return;
}
graus = MatUtil.calculaDirecao(Jogo.pxyMouse.x,
Jogo.pxyMouse.y,
navJogDois.getPx(),
navJogDois.getPy());
graus = MatUtil.corrigeGraus(graus);
navJogDois.setAngulo(graus);
Seanavenãoestiverativa(mododeapenasumjogador),eojogador
pressionarobotãodedisparo,anaveapareceránojogo;casocontrário,ig-
noramosorestantedocódigo.Alémdafun ção Math.atan2teridoparar
dentroda MatUtil.calculaDirecao,agrandenovidadeincluiqueusa-
mosaposi çãodoponteirodomousenatelapararotacionaranave.Então,a
navedosegundojogadorapontanadire çãodoponteirodomouse.
if (Jogo.controleTecla[Jogo.Tecla.MOUSE_A.ordinal()]) {
adicionarTiro(navJogDois);
Jogo.liberaTecla(Jogo.Tecla.MOUSE_A);
}
if (Jogo.controleTecla[Jogo.Tecla.MOUSE_B.ordinal()]) {
float vx = navJogDois.getVelEmX();
float vy = navJogDois.getVelEmY();
vx += MatUtil.moveAnguloEmX(navJogDois.getAngulo());
vy += MatUtil.moveAnguloEmY(navJogDois.getAngulo());
navJogDois.setVelEmX(vx);
navJogDois.setVelEmY(vy);
}
}
Ocliquedobotãoprincipalefetuadisparos,edobotãosecundárioace-
leraanave.Valelembrarque,aochamar Jogo.liberaTecla,impedimos
241
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 264

9.3. Jogandoocódigo CasadoCódigo
disparosseguidosmesmoseojogadordeixarpressionadoobotãodedisparo.
Falandoemdisparos:
private void adicionarTiro(Nave jogador) {
if (contadorTiro > 1)
contadorTiro--;
else
contadorTiro = tiros.length - 1;
Tiro t = tiros[contadorTiro];
if (t.isAtivo())
return;
t.setNave(jogador);
t.setAngulo(jogador.getAngulo());
Util.centraliza(t, jogador);
t.setAtivo(true);
}
Dica
Limitamosnossajogabilidadeaoscliquesprimáriosesecundários,
masamaioriadosmousestemobotãoderolagem(ealgunsaindamais
botões),quepodeaumentarasa çõesdojogador.
Paraumaversãomaissofisticadadojogo,ondecadanaveteriaseupró-
priotiroousimplesmenteumcontroleindividualdeles,cadaobjetoteriaseu
próprioarraydetiros.Porém,vocêpodeaumentarotamanhodoarraycom-
partilhadoparaqueasnavesdisparemàvontade.
Fazemosadivisãodoasteroidequandoelecolideativandoeconfigurando
um Asteroideinativoereconfigurandooobjetoanterior.Issoficouacargo
dométodo novaParteAsteroide,quesóéchamadoseeleaindapuderser
dividido.
242
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 265

CasadoCódigo Capítulo9. Asteroids:ojogoquesaberepresentarafísica
private void novaParteAsteroide(Asteroide ast) {
Asteroide novoAst = aerolitos[contadorAsteroides];
novoAst.setAtivo(true);
novoAst.setPx(ast.getPx());
novoAst.setPy(ast.getPy());
novoAst.setImagem(ast.getImagem());
novoAst.setTamanho(ast.getTamanho());
novoAst.setVel(rand.nextInt(3) + 5);
float angulo = ast.getAngulo();
ast.setAngulo(MatUtil.corrigeGraus(angulo + 90));
novoAst.setAngulo(MatUtil.corrigeGraus(angulo - 90));
contadorAsteroides++;
}
Pegamosopróximoelementodafila( novoAst)ecopiamosalgumasin-
formaçõesdoasteroideabatido( ast),quejáestácomopróximo tamanho
(quepodeser MEDIOou PEQUENO)definido.Porfim,aumentamosaschan-
cesdonovo astterumavelocidademaior,ecolocamosambosemângulos
opostos.
O último método da classeJogoCenario.java, nosso método
desenhar:
//método desenhar:
g.setTransform(AF_VAZIO); // Comentar para um zoom cada vez maior
if (ampliar) {
g.scale(1 + escala, 1 + escala); // 1,05
g.translate(-largura * escala / 2f + 1,
-altura * escala / 2f + 1); // Centralizar
} else if (reduzir) {
// Apenas exemplo
243
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 266

9.3. Jogandoocódigo CasadoCódigo
g.setColor(Color.WHITE);
g.fillRect(0, 0, largura, altura);
g.scale(1 - escala, 1 - escala); // 1 - 0,05 = 0,95
g.translate(largura * escala / 2f + 1,
altura * escala / 2f + 1); // Centralizar
}
Primeirozeramosqualquertransforma çãoanteriorusando AF_VAZIO,
depoisverificamossevamosescalonarnossosdesenhosem5%dotamanho
normalusando scalee,então, translateparacentralizaratelaampliada.
Nãousamosoefeitoderedu ção,ficandoapenascomoexemplo.
Senãozerarmosastransforma çõesanteriores,osefeitosseacumulam
gerandoumzoomcadavezmaior.Ficoucurioso?Bastacomentaralinha.
g.drawImage(fundo.getImage(), 0, 0, null);
texto.desenha(g, "Tupã | " + navJogUm.getPontos(), 10, 20);
texto.desenha(g, "Îasy | " + navJogDois.getPontos(),
largura - 120, 20);
if (navJogUm.getSeguidos() > 2)
texto.desenha(g, "x" + navJogUm.getSeguidos(), 10, 40);
if (navJogDois.getSeguidos() > 2)
texto.desenha(g, "x" + navJogDois.getSeguidos(),
largura - 120, 40);
Desenhamosaimagemdefundoeapontua çãodosjogadores.Estamos
usandopraticamenteamesmafonte,tamanhoecor,então,nestecaso,não
fazdiferençachamar g.drawStringou texto.desenha.
Apartirdoterceiroacertoseguido,exibimosaquantidadedeacertosse-
guidosquecadanavefez.Emseguida,desenhamosostiroseaerólitosativos.
for (int i = 0; i < tiros.length; i++) {
if (tiros[i].isAtivo())
tiros[i].desenha(g);
}
244
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 267

CasadoCódigo Capítulo9. Asteroids:ojogoquesaberepresentarafísica
for (int i = 0; i < contadorAsteroides; i++) {
if (aerolitos[i].isAtivo())
aerolitos[i].desenha(g);
}
navJogUm.desenha(g);
navJogDois.desenha(g);
colisaoAst.desenha(g);
explosaoAst.desenha(g);
Paraficarsobreosoutroselementos,desenhamosporúltimoasnavesdos
jogadoreseasanima çõesdecolisãoeexplosão.
Fig.9.5:Exibindoacertosseguidos
Dica
Você pode deixar o placar com mais cara de árcade usando:
String.format("Tupã | %04d", navJogUm.getPontos()) ,
emque %04drepresentaráapontuaçãocom 4dígitos,preenchendoos
espaçosvazioscom 0.
Aolongodoscapítulos,nãofizemosnenhumagrandealtera çãonaclasse
Jogo.java. Mudamosotamanhodatelaparaalgunsjogos,adicionamos
botõesounovasentradasemoutros,masdestavezfizemosmuitasaltera ções
nanossaclasse Jogo.java.Começamospelocontroledosegundojogador.
245
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 268

9.3. Jogandoocódigo CasadoCódigo
...
public enum Tecla {
CIMA, BAIXO, ESQUERDA, DIREITA, BA, BB, BC,
MOUSE_A, MOUSE_B
}
...
public static int numeroJogadores;
public static final Point pxyMouse = new Point();
Para controlar o segundo jogador, que estará disponível se
numeroJogadores for igual a 1 (segunda opção do menu), adiciona-
mosmaisdoisvaloresaonosso enum Tecla: MOUSE_Ae MOUSE_B.
Também,usamosavariável pxyMouseparaguardaraposi çãodomousena
tela,usandoum java.awt.Point.
Em nosso construtor, adicionamos ouvintes para detectar não só o
clique ( MouseListener), como também o movimento do mouse (
MouseMotionListener).
public Jogo() {
...
tela.addMouseMotionListener(new MouseMotionListener() {
@Override
public void mouseMoved(MouseEvent e) {
pxyMouse.x = e.getX();
pxyMouse.y = e.getY();
}
@Override
public void mouseDragged(MouseEvent e) {
}
});
Observequeemnossaimplementa çãodo mouseMoved,poderíamosob-
terumobjeto Pointdiretamentecom e.getPoint(),porém,emvez
disso,armazenamososvaloresinteirosdiretamenteparareaproveitarmoso
mesmoobjeto.
246
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 269

CasadoCódigo Capítulo9. Asteroids:ojogoquesaberepresentarafísica
Deformasimilaraoquefazemosparacontrolarasteclaspressionadas,
usamos mouseReleasede mousePressedparaverificaroscliquesdo
mouse.Seforobotãoprincipal( MouseEvent.BUTTON1),anaveatira;se
forqualqueroutro,elasemove.
tela.addMouseListener(new MouseListener() {
@Override
public void mouseReleased(MouseEvent e) {
if (e.getButton() == MouseEvent.BUTTON1)
controleTecla[Tecla.MOUSE_A.ordinal()] = false;
else
controleTecla[Tecla.MOUSE_B.ordinal()] = false;
}
@Override
public void mousePressed(MouseEvent e) {
if (e.getButton() == MouseEvent.BUTTON1)
controleTecla[Tecla.MOUSE_A.ordinal()] = true;
else
controleTecla[Tecla.MOUSE_B.ordinal()] = true;
}
@Override
public void mouseExited(MouseEvent e) {
}
@Override
public void mouseEntered(MouseEvent e) {
}
@Override
public void mouseClicked(MouseEvent e) {
}
});
...
}
Ignoramosoutrasa çõesdomouse,quepodemserrelembradasnoscapí-
247
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 270

9.3. Jogandoocódigo CasadoCódigo
tulos1e3.Emboraestesejanossoúnicojogomultijogador,alógicaaplicada
aquipodeserusadaemquasetodososjogosquejáfizemos.
Deixamosparaofinalumamelhoriaopcional,queusamosparatestara
taxadequadrosdonossojogo.
Fizemosnossojogoprevendoqueteríamos20framesporsegundo(
private static final int FPS = 1000 / 20 ),masseráquereal-
mentetemosemumsegundo20execu çõesdosmétodos atualizare
desenhar?
Paratiraressadúvida,melhoramosnossomotordejogo,eagoraconse-
guimosverquantosquadrossãodesenhadosporsegundo.
...
public static int atraso = 0;
public static int somaFPS = 0;
private static final SimpleDateFormat sdf =
new SimpleDateFormat("ss:SSSS");
private static final boolean depurar = true;
Na variável atraso, armazenamos os milésimos de segundo que
se passaram entre o início e o fim do processamento do jogo e, na
variável somaFPS, quantos processamentos temos a cada 1 segundo
ou 1000 milésimos de segundo. Para ainda mais informação, usa-
mos o SimpleDateFormatpara exibir o tempo corrente (obtido com
System.currentTimeMillis())emsegundosemilissegundos,quando
depurarforverdadeiro.
Nãoimportaoquantoseuprocessadorsejarápido,elevaiprecisardeal-
gunsmilissegundos(nanossegundosseestelivrodemoroumuitoparaseres-
crito)paraprocessar(atualizaredesenhar)nossojogo. Utilizamos agora
paraarmazenarotemponoiníciodoprocesso,edepoismedirmososmilé-
simosdesegundoquesepassaram.
public void iniciarJogo() {
long agora;
int contadorFPS = 0;
long prxAtualizacao = 0;
248
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 271

CasadoCódigo Capítulo9. Asteroids:ojogoquesaberepresentarafísica
long prxSegundo = System.currentTimeMillis() + 1000;
while (true) {
agora = System.currentTimeMillis();
if (agora >= prxAtualizacao) {
verificaTeclas();
g2d.setColor(Color.BLACK);
g2d.fillRect(0, 0, JANELA_LARGURA, JANELA_ALTURA);
if (!Jogo.pausado)
cenario.atualizar();
cenario.desenhar(g2d);
Incrementamos contadorFPSacadafinaldeprocessamento,sendoque
somaFPSrecebeovalorde contadorFPSacada1segundo,antesdeeleser
zerado. AvariávelprxAtualizacaoénossavelhaconhecida,usadapara
sabermosquandoprocessarnovamentenossojogo.
Alémdeimprimirmosalgunsdadosnoconsole,desenhamosnocanto
esquerdoinferiordatelaovalorarmazenadonavariável somaFPS.
if (!Jogo.pausado)
cenario.atualizar();
cenario.desenhar(g2d);
if (Jogo.pausado) {
g2d.setColor(Color.WHITE);
g2d.drawString("Pausado",
tela.getWidth() / 2 - 30, 30);
}
if (depurar) {
g2d.setColor(Color.WHITE);
g2d.drawString("FPS " + somaFPS, 10,
249
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 272

9.3. Jogandoocódigo CasadoCódigo
JANELA_ALTURA - 10);
}
tela.repaint();
contadorFPS++;
atraso = (int) (System.currentTimeMillis() - agora);
prxAtualizacao = System.currentTimeMillis() + FPS;
}
Medimosoatrasonaexecu çãodojogosubtraindo,aofinaldoprocessa-
mento,otempocorrentepelovalorarmazenadoantesdeiniciarmosopro-
cessamento.Assim,definimosovalordavariável atraso.
Todavezqueprocessamosojogo(quando agoraformaiorouigual
a prxAtualizacao),incrementamos contadorFPSe,acadasegundo
(quando agoraformaiorouigual prxSegundo),armazenamosoresul-
tadoem somaFPSereiniciamosacontagem.
if (depurar && agora >= prxSegundo) {
System.out.println("Atraso = " + atraso);
System.out.println("FPS = " + contadorFPS);
System.out.println("Segundos: " + sdf.format(agora));
somaFPS = contadorFPS;
contadorFPS = 0;
prxSegundo = System.currentTimeMillis() + 1000;
}
}
}
Dessaforma,quando depurarforverdadeiro,alémdemostramosna
telaataxadequadrosporsegundo,imprimirmosquantosmilésimosdese-
gundocustaparaprocessarnossojogo.
Seacontagemdequadrosestivermenorqueoesperado,fa çatestesau-
mentandoseu FPS,de20para21,porexemplo. Masobservequeaveloci-
dadedosnossosjogosébaseadaempixelsporFPS,então,amenosqueesteja
250
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 273

CasadoCódigo Capítulo9. Asteroids:ojogoquesaberepresentarafísica
aplicandoumefeitodeacelera ção(oudesacelera ção),mudardrasticamente
ataxadequadrosfaráojogoparecerquebrado.
Dica
Emboranãoabordemos,outraformacomumdecontrolaraveloci-
dadedojogo,independentedoFPS,envolvelevaremconsidera çãoo
tempoantesedepoisdoprocessamento,eusaressadiferen ça(conhe-
cidacomo delta time)namovimenta çãodoselementos.
Porserumjogopequeno,oatrasoentreumprocessamentoeoutroé
quaseinsignificante,massaibaqueexistemdiversastécnicasparacompensar
atrasos(curtosoulongos),quepodemserbemsimplesoubemcomplexas.
Falando simplificadamente de duas dessas técnicas, a primeira é
forçar mais o processador, fazendo o próximo processamento aconte-
cer mais cedo, isso é, subtraindo oatraso do tempo de espera
para a próxima atualização. Um exemplo seria prxAtualizacao =
System.currentTimeMillis() + FPS - atraso .
Asegundatécnicaconsisteemfazerocontráriodaprimeira:pularafase
dedesenho–quegeralmenteconsomemaisrecursos–dopróximoproces-
samentoquandoojogoacumularmuitosatrasosparaaliviaroprocessadore
tentarrecuperarotempoperdido.Masissosomentequandoojogonãotem
umgráficoextremamentesimplescomumainteligênciaartificialcomplexa,
ouummododemúltiplosjogadoresemrede.
Existemuitadiscussãosobreesteassuntonainternetemuitostutoriais,
comoemhttp://www.pontov.com.br. Assim,recomendoprocurarmaisso-
bre,evocênotaráqueafaltadeconsistêncianataxadequadroséumpro-
blemaatémesmoparajogosrecentesdegrandesprodutoras.
9.4 C odificando o jogo
Semrepetirmosoquefoivistonocapítuloanterior,temostrêsnovasclas-
ses: MatUtil.java (que está no pacotebase), Recursos.java e
251
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 274

9.4. Codificandoojogo CasadoCódigo
Animacao.java.Criamos MatUtil.javaparasimplificaralgumascha-
madasaosmétodosdaclasse Math,econtinuamosutilizandosomentegraus
paracontrolarnossosângulos.
Nossaclasse Recursos.javaconcentratodasasimagensdojogo,que
estãonapasta imagensnaraizdoprojeto,mastambémpodeserusadapara
concentraroutrosrecursosdojogo,comosonse,quemsabe,vídeos.
Paracontrolarnossapequenaanima çãodeexplosão,usadanascolisões,
criamosaclasse Animacao.java,quepercorreumspritesimplesdentrode
umintervalopré-determinado.
Agora,nosso Asteroide.javavagasemrumopeloespa çoe,aocolidir
comanaveouseracertadoporumtiro,sedivideindodotamanhogrande
paraomédio,domédioparaopequeno,edepoisvirandopoeira.
O Tiro.javaagorasabedequenavefoidisparado,influenciandona
pontuaçãodojogador.Quandoalgumjogadoralcan çarmaisdedoisacertos
seguidos,apresentamosumaindica çãovisualdequeeleestáindobem.
Nossa Nave.java,quecome çaparadanocentrodatela,agorasemove
porelae,umavezquetenhasaídodolugar,requerhabilidadeparaexecutar
manobraseperdemocontroleaocolidirem. Cadanaverecebeuumnome
quepegamosemprestadodaculturaTupiGuarani.
Ojogoganhouummodoparadoisjogadores:umcontroladopeloteclado
eoutropelomouse. Tambémaplicamosumefeitodeaproxima çãonatela
comoumtodo,mudandoodesenhofinal. Essassãoasnovidadesnaclasse
JogoCenario.java.
Depoisdetudoisso,alteramosaclasse Jogo.javaparatermosmais
informaçõesacercadaconstânciadojogo,entãomelhoramosnossomotore
agoraconseguimosverquantosquadrossãodesenhamosporsegundo.
Adicionamos o métodocorrigePosicao e uma nova versão do
método saiu na classe Util.java. Também temos uma classe
RotacaoTeste.java,quefazamesmalógicadaclassedocapítuloante-
riorcomimagens.
Confira tudo isso em https://github.com/logicadojogo/fontes/tree/
master/Cap09.
252
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 275

CasadoCódigo Capítulo9. Asteroids:ojogoquesaberepresentarafísica
Não fizemos aqui
• Modojogadorversusjogador;
• Tirodiferenteparaosegundojogador.
Melhore você mesmo
• Exibirplacarfinalnaintroduçãodojogo;
• Contarmáximodeacertosseguidos.
9.5 R esumo
Senossaversãochegaaospésdojogooriginal,sóvocêpodedizer,mascom
certezahonramosonomeAsteroidsadicionandoconceitosdefísica,umpe-
quenoefeitodeanima çãoeapossibilidadededoisjogadores.
Temospequenosproblemas,comoporexemplo,ojogadorcomomouse
levavantagemjáqueconseguegiraranavemuitomaisrápidoqueojogador
noteclado. Alémdenãotermosdadoinvulnerabilidademomentâneaaos
jogadoresnoiníciodojogoeaoserematingidos,causandomúltiplascolisões.
Jávimosformasdeimplementaressasfuncionalidadesemoutrosjogose,
aojuntaremisturarosjogosdecadacapítulo,acabarácriandonovosjogos.
253
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 276

E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 277

Capítulo10
Últimafase,últimochefee
próximosjogos
Vimosbastantecoisaatéaqui,foram6jogos(semcontarmososprotótipos),
maisde44classes,alémdealgumasmúsicaseimagens.Vocêtemcódigosu-
ficientepararecriaroutrosjogosde Arcade,muitosdelesapenasmisturando
oualterandoosjogosdeumoumaiscapítulos.Além,éclaro,decódigopara
criarseusprópriosjogosoriginais,inclusiveemoutrasplataformaselingua-
gensdeprograma ção.
Sevocêouviunossassúplicasepersonalizou,melhorououamplioualgum
jogovistonestelivro,porfavor,contribuasubmetendosuasaltera çõespara
orepositórioquecriamosexatamenteparaquevocêfizesseisso,em:https:
//github.com/logicadojogo.Todaequalquercontribui çãoserábenquista.
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 278

10.1. Desafios CasadoCódigo
10.1 D esafios
Depoisdeconstruirmosnossaversãodojogo,nofinaldecadacapítulo,dei-
xamosalgunsdesafiosparavocêleitor.Alógicapararesolvê-losfoimostrada
emcapítulosposteriores,evocêpodeterobtidoomesmoresultadousando
umcódigooulógicadiferente. Mesmoassim,vamosrever,deformaresu-
mida,algunspontosquemerecemumpoucomaisdedestaque.
Nocapítulo2,nãocriamosasbarreirasparecidascomadojogoorigi-
nal.Podemosfazerissodamesmaformaquecriamoscenáriosnocapítulo4,
então,naclasse Nivel.javacriamososeguintearray:
Fig.10.1:Barreirasdojogo
As barreiras poderiam ser mais simples, mas optamos por homena-
gearojogooriginal. Modificamosométodo carregarJogodaclasse
256
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 279

CasadoCódigo Capítulo10. Últimafase,últimochefeepróximosjogos
Jogo.java,lembrandodequenestecapítuloaindanãotínhamosaclasse
JogoCenario.java:
private void carregarJogo() {
int total = 0;
int _LARG = 10;
for (int i = 0; i < Nivel.niveis.length; i++) {
char[][] n = Nivel.niveis[i];
for (int linha = 0; linha < n.length; linha++) {
for (int coluna = 0; coluna < n[0].length; coluna++){
if (n[linha][coluna] == '0')
total++;
}
}
}
nivel = new Elemento[total];
for (int i = 0; i < Nivel.niveis.length; i++) {
char[][] n = Nivel.niveis[i];
for (int linha = 0; linha < n.length; linha++) {
for (int coluna = 0; coluna < n[0].length; coluna++){
if (n[linha][coluna] != ' ') {
Elemento e = new Elemento();
e.setAtivo(true);
e.setCor(Color.LIGHT_GRAY);
e.setPx(_LARG * coluna + 30 + (200 * i));
e.setPy(_LARG * linha +
JANELA_ALTURA - 300);
e.setAltura(_LARG);
e.setLargura(_LARG);
257
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 280

10.1. Desafios CasadoCódigo
nivel[--total] = e;
}
}
}
}
Cadapedaçodabarreiraseráumobjeto Elemento.Depois,sóprecisa-
mosdesenhareverificaracolisãodos tiroscomabarreira:
for (Elemento e : nivel) {
if (!e.isAtivo())
continue;
for (int i = 0; i < tiros.length; i++) {
if (tiros[i].isAtivo() && Util.colide(tiros[i], e)) {
e.setAtivo(false);
tiros[i].setAtivo(false);
}
}
g2d.setColor(e.getCor());
e.desenha(g2d);
}
Gerandooseguinteresultado:
258
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 281

CasadoCódigo Capítulo10. Últimafase,últimochefeepróximosjogos
Fig.10.2:Barreirasemhomenagemaojogooriginal
Paraimpedirojogadordesairdatela,temosométodo saiudaclasse
Util.javae,paraencerrarojogoquandootanqueperdertodasasvidas,
podemosusaromesmoexemplodocapítulo4ou5.
No capítulo 3, deixamos de calcular o ângulo da bola na rebatida,
masvimoscomotrabalharcomângulonocapítulo9. Paraexibirasúlti-
maspontua çõesnocenáriodeintrodu çãodojogo, vocêpodeusarnossa
classe Texto.java,chamandoométodo texto.desenha,oudiretamente
g.drawString(vejaumexemplomaisadiantenestecapítulo). Ficoupor
suacontacriarummododejogoseu.
Nocapítulo4,parairparaopróximonívelquandoojogadorganhar,
temosumbomexemplonocapítulo5e,paradefiniraposi çãoinicialdaser-
pentedeacordocomafase,fizemosalgoparecidonocapítulo6. Inclusive,
adicionandomaisvaloresaoarraydeníveisparacriarcenárioscommaisco-
res. Paracriarseupróprionível,vocêpodeeditarouadicionarmaisarrays
bidimensionaisaoarray niveisdaclasse Nivel.java.
Nocapítulo5,podemosadicionarumnovomenuparateraop çãode
jogarcomesemsom,ousomenteefeitossonoros.Vejacomoexemploomenu
259
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 282

10.1. Desafios CasadoCódigo
docapítulo4.Paramanipularamúsicadefundoduranteojogo,vocêpode
aumentarabatidaporminutodeacordocomoníveldojogo,porexemplo:
seqSomDeFundo.setTempoInBPM(seqSomDeFundo.getTempoInBPM()
* nivel);
Para adicionar um botão para girar a peça no sentido horá-
rio, você pode mapear a tecla espaço para chamar o método
girarReposicionarPeca(true) ou girarPeca(true), lembrando
que, no anti-horário, você passa o valorfalse. No próprio capítulo,
deixamosdicasparaacharoucriarsuaprópriamúsicadefundoeefeitos
sonoros.
Nocapítulo6,tantoparaterafamíliadequatrofantasmascompleta,rei-
niciarocenárioaocomertodasaspastilhasecriarumacópiadocenáriopara
nãoperderaconfigura çãoinicial,bastaveraversãomaisavan çadadojogo
nocapítulo7.Paraadicionarfrutasqueaumentemapontua çãodojogador,
primeiroadicionamosumnovovaloraoarray cenario,responsávelpor
montarocenáriodojogo,naclasse Nivel.java.Paracontrolaraposi ção
nagradeemqueafrutavaiaparecer,criamosumnovovalor:
...
/** Fruta */
public static final int FT = 10;
...
Nossovalorserárepresentadopor FTeadicionadoaoladodaposi ção
inicialdojogador(representadopor PI)nocenário. Depoiscriamosum
novoelemento,que,alémderepresentarafrutanojogo,levaemcontao
espaçamentosuperiorqueusamosparaexibirospontosdojogador:
private Elemento fruta = new Elemento() {
@Override
public void desenha(Graphics2D g) {
if(!isAtivo())
return;
g.setColor(Color.RED);
g.fillOval(getPx() - 4, getPy() + JogoCenario.ESPACO_TOPO,
260
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 283

CasadoCódigo Capítulo10. Últimafase,últimochefeepróximosjogos
getLargura() / 2,
getAltura() / 2);
g.fillOval(getPx() + 4, getPy() + JogoCenario.ESPACO_TOPO,
getLargura() / 2,
getAltura() / 2);
g.fillOval(getPx(), getPy() + 5 + JogoCenario.ESPACO_TOPO,
getLargura() / 2,
getAltura() / 2);
}
};
Deformasimples,desenhamostrêsbolasvermelhasparasimularuma
cereja.Então,configuramosoobjeto frutadentrodométodo carregar,
aopercorreroarray grade:
...
} else if (grade[lin][col] == Nivel.FT) {
fruta.setLargura(largEl);
fruta.setAltura(largEl);
fruta.setPx(converteInidicePosicao(col));
fruta.setPy(converteInidicePosicao(lin));
}
Nométodo atualizar,paraativarafrutafazendo-aficarvisível,pode-
mosusarumcontadoroualeatoriamentedestaforma:
...
if (!fruta.isAtivo() && rand.nextInt(1000) == 5) {
fruta.setAtivo(true);
}
if (Util.colide(pizza, fruta)) {
fruta.setAtivo(false);
pontos += 100;
}
...
261
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 284

10.1. Desafios CasadoCódigo
Seafrutaestiverativa,ométodo Util.colideretornaráverdadeiro.
Logo,desativamosafrutaedamos100pontosparaojogador.Sónãoesque ça
dedesenhá-laantesdosdemaiselementos:
...
texto.desenha(g, "Pontos: " + pontos, 10, 20);
fruta.desenha(g);
pizza.desenha(g);
...
Fig.10.3:Algoquepareceumacereja
No capítulo 7, trabalhamos com sprites e tiles, mas, para aplicar ro-
tação nas imagens, olhe os exemplos no capítulo 9. Para apresentar
os personagens na introdução do jogo, modificamos somente a classe
InicioCenario.java:
...
private Pizza pizza;
private Legume[] inimigos;
private Elemento superPastilha;
@Override
public void carregar() {
...
pizza = new Pizza();
pizza.setVel(3);
262
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 285

CasadoCódigo Capítulo10. Últimafase,últimochefeepróximosjogos
pizza.setAtivo(true);
pizza.setDx(-1);
pizza.setPx(largura + pizza.getLargura());
pizza.setPy(200);
superPastilha = new Elemento() {
@Override
public void desenha(Graphics2D g) {
if (!isAtivo())
return;
g.drawImage(getImagem().getImage(),
getPx(),
getPy() + JogoCenario.ESPACO_TOPO, null);
}
};
Adicionamosopersonagemprincipal,osinimigoseumasuperpastilha,
queéum Elementocomum;apenasmodificamosométodo desenhapara
levaremconsidera çãooespa çamentonotopo,tambémutilizadoparade-
senharosoutroselementos. Oobjetivoémostraropersonagemprincipal
correndodosinimigosdadireitaparaaesquerda,atéchegaràpastilhaonde
entraránomodosuper,invertendoospapéisefazendoosinimigosfugirem.
ImageIcon pepperoni = new ImageIcon("imagens/pepperoni.png");
superPastilha.setAtivo(true);
superPastilha.setPx(5);
superPastilha.setPy(pizza.getPy());
superPastilha.setImagem(pepperoni);
superPastilha.setLargura(pepperoni.getIconWidth());
superPastilha.setAltura(pepperoni.getIconHeight());
inimigos = new Legume[Legume.Tipo.values().length];
for (int i = 0; i < inimigos.length; i++) {
inimigos[i] = new Legume(Legume.Tipo.values()[i]);
inimigos[i].setVel(3);
inimigos[i].setAtivo(true);
inimigos[i].setDx(-1);
263
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 286

10.1. Desafios CasadoCódigo
inimigos[i].setPy(pizza.getPy());
inimigos[i].setPx(largura +
(pizza.getLargura() * 2) * (i + 2));
}
}
Todososelementosficarãonomesmoalinhamentohorizontaldoele-
mento pizzae,alémdeutilizarmosaimagemdo pepperoni.pngpara
apastilha,atualizamosseutamanhoparaqueadetec çãodecolisãofuncione
corretamente.Configuramostodososinimigosdeumasóvez,adicionando
espaçamentosuficienteentreelesparaapareceremforadatela,depoisdoper-
sonagemprincipal.
@Override
public void atualizar() {
...
if (pizza.getPx() > largura * 2) {
return;
}
pizza.atualiza();
for (Legume legume : inimigos) {
legume.atualiza();
if (Util.colide(pizza, legume)) {
legume.setModo(Legume.Modo.FANTASMA);
}
}
Ospersonagenssóserãoatualizadosdentrodeumlimitequeéodobroda
larguradatelaparagarantirquetodossaiamdecenaenãoacabemcongelados
nomeiodocaminho.Seoobjeto pizzacolidircomum legume,oinimigo
viraumfantasma,masissosóacontecerádepoisqueopersonagemcolidir
comasuperpastilha,quandoinvertemosadire çãodeles.
if (Util.colide(pizza, superPastilha)) {
pizza.setDx(1);
pizza.setVel(pizza.getVel() + 2);
264
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 287

CasadoCódigo Capítulo10. Últimafase,últimochefeepróximosjogos
superPastilha.setAtivo(false);
for (Legume legume : inimigos) {
legume.setDx(1);
legume.setModo(Legume.Modo.FUGINDO);
}
}
}
@Override
public void desenhar(Graphics2D g) {
superPastilha.desenha(g);
pizza.desenha(g);
for (Legume legume : inimigos) {
legume.desenha(g);
}
menuJogo.desenha(g);
}
Porfim,antesdedesenharmosomenu,desenhamososnovoselementos.
Vimoscomoaplicarefeitossonorosnocapítulo5,edeixamosporsuaconta
usarsuasprópriasimagensparapersonalizarojogo.
Nocapítulo8,sedeixamosdemovimentaranavepelatelaecontrolara
navecomomouse,foiparafazermosissonocapítulo9,quetambémmos-
tracomocontaracertosseguidosparaaumentarapontua çãodojogadore
utilizarimagens.
Paracriarmosformasdetiroqueusemângulosdiferentes,utilizamosum
enumparacontrolarotipodedisparo:
enum TipoTiro {
COMUM, DUPLO, TRIPLO
}
private void proximoTiro() {
if (contadorTiro > 1)
contadorTiro--;
else
265
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 288

10.1. Desafios CasadoCódigo
contadorTiro = tiros.length - 1;
}
Comopodemostermaisdeumdisparoporvez,separamosdométodo
adicionarTiroocontadordetiros,parapoderchamá-lodeacordocoma
quantidadedeprojéteisnecessária.
private void adicionarTiro(float angulo, TipoTiro tipo) {
if (TipoTiro.COMUM == tipo || TipoTiro.TRIPLO == tipo) {
proximoTiro();
Tiro t = tiros[contadorTiro];
t.setAngulo(angulo);
t.setPx(nave.getPx() +
nave.getLargura() / 2  t.getLargura() / 2);
t.setPy(nave.getPy() +
nave.getAltura() / 2  t.getAltura() / 2);
t.setAtivo(true);
}
Otipodetirocomumcontinuasendoumdisparocentral,oduplotam-
bémcomeçanocentro,massegueemdire çãoopostaumdooutro,eotriplo
acabasendoamisturadessesdois.
if (TipoTiro.DUPLO == tipo || TipoTiro.TRIPLO == tipo) {
proximoTiro();
Tiro tiroA = tiros[contadorTiro];
proximoTiro();
Tiro tiroB = tiros[contadorTiro];
tiroA.setAngulo(angulo - 10);
tiroA.setPx(nave.getPx() + nave.getLargura() / 2 -
tiroA.getLargura() / 2);
266
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 289

CasadoCódigo Capítulo10. Últimafase,últimochefeepróximosjogos
tiroA.setPy(nave.getPy() + nave.getAltura() / 2 -
tiroA.getAltura() / 2);
tiroB.setAngulo(angulo + 10);
tiroB.setPx(nave.getPx() + nave.getLargura() / 2 -
tiroB.getLargura() / 2);
tiroB.setPy(nave.getPy() + nave.getAltura() / 2 -
tiroB.getAltura() / 2);
tiroA.setAtivo(true);
tiroB.setAtivo(true);
}
}
Estamoscentralizandoostirosusandoindividualmentealarguraealtura
decadaum,issosófarádiferen çaseosobjetos Tirotiveremtamanhosdi-
ferentes.O tiroArecebeoângulodanavemenos10,jáo tiroB,oângulo
danavemais10.
Fig.10.4:Tirocomum,duploetriplo
Amudançaentreostiposdetiropodeacontecerdediversasmaneiras,
comoporexemplo,ojogadoracertarumaquantidadedeinimigos,oualgum
itemqueelepossaconseguiracertaroucolidir,ofamoso power up.
Nocapítulo9,paratermosumtirodiferenteparaosegundojogador,além
demudançasnaspropriedadesdotirocomovelocidadeouângulo,podemos
utilizarumanovaimagem. Paraisso,jádeixamosalgumascoisasprontas.
Começamosalterandoométodo carregarImagens,daclasse Recursos,
paraquecarregueumnovoarquivo:
public static void carregarImagens() {
...
267
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 290

10.1. Desafios CasadoCódigo
imagens[Imagem.TIRO_A.ordinal()] =
new ImageIcon(DIR_IMG + "tiro.png");
imagens[Imagem.TIRO_B.ordinal()] =
new ImageIcon(DIR_IMG + "tiro_b.png");
...
}
Depois,nométodo adicionarTironaclasse JogoCenario,defini-
mosaimagemdotirodeacordocomojogador:
private void adicionarTiro(Nave jogador) {
...
if (navJogUm == jogador)
t.setImagem(Recursos.getImagem(Recursos.Imagem.TIRO_A));
else
t.setImagem(Recursos.getImagem(Recursos.Imagem.TIRO_B));
t.setAtivo(true);
}
Paraomodojogadorversusjogador,dentrodométodo atualizar
(aindadentrodaclasse JogoCenario),casonãotenhasaídodatela,atu-
alizamoseverificamosseo tirodojogadoratingiuanaveoposta:
for (Tiro tiro : tiros) {
if (!tiro.isAtivo())
continue;
if (Util.saiu(tiro, largura, altura, 20)) {
tiro.setAtivo(false);
tiro.getNave().errou();
} else {
tiro.atualiza();
if (navJogUm != tiro.getNave()
&& Util.colide(tiro, navJogUm)) {
tiro.setAtivo(false);
navJogUm.danos();
268
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 291

CasadoCódigo Capítulo10. Últimafase,últimochefeepróximosjogos
navJogUm.setAngulo(
MatUtil.corrigeGraus(
navJogUm.getAngulo() + 90));
} else if (navJogDois != tiro.getNave()
&& Util.colide(tiro, navJogDois)) {
tiro.setAtivo(false);
navJogDois.danos();
navJogDois.setAngulo(
MatUtil.corrigeGraus(
navJogDois.getAngulo() - 90));
}
}
}
Paracontaromáximodeacertosseguidos,fa çaalgoparecidocomoque
fizemoscomocontadordeerrose,paraexibirplacarfinalnaintrodu çãodo
jogo,criamosumarrayestáticoparaarmazenarapontua çãomáximadecada
jogador,algoparecidocom public static short[] jogadorPontos
= new short[2] .Depoisdeverificarmosacolisãoentreasteroidesetiros,
esomarmosospontosdosjogadores,atualizamosapontua çãocasoelaseja
maiorqueaanterior.
for (Tiro tiro : tiros) {
if (Util.colide(ast, tiro)) {
...
tiro.getNave().somaPontos(ast.getPonto());
short pontos = tiro.getNave().getPontos();
if (navJogUm == tiro.getNave() &&
pontos > Jogo.jogadorPontos[0])
Jogo.jogadorPontos[0] = pontos;
else if (navJogDois == tiro.getNave() &&
pontos > Jogo.jogadorPontos[1])
Jogo.jogadorPontos[1] = tiro.getNave().getPontos();
...
}
269
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 292

10.1. Desafios CasadoCódigo
Modificamosaclasse InicioCenario.javaparaexibiroplacarcom
umefeitoderolamentovertical,utilizandoavariável novaPyeumobjeto
texto.
private int novaPy;
private Texto texto = new Texto();
@Override
public void atualizar() {
novaPy++;
if (novaPy + 100 > altura)
novaPy = -100;
...
}
Então,desenhamosapontua çãousando novaPyparadefiniroposicio-
namentonoeixoY.
@Override
public void desenhar(Graphics2D g) {
...
g.setColor(Color.WHITE);
texto.desenha(g, String.format("Tupã | %04d",
Jogo.jogadorPontos[0]), largura / 4, novaPy);
texto.desenha(g, String.format("Îasy | %04d",
Jogo.jogadorPontos[1]), largura / 2 + 100, novaPy);
menuJogo.desenha(g);
}
Obtendooseguinteresultado:
270
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 293

CasadoCódigo Capítulo10. Últimafase,últimochefeepróximosjogos
Fig.10.5:Omelhordosmelhores
Assim como todo código apresentado neste livro, você encontra as
versõesmodificadasdocódigo-fonteem: https://github.com/logicadojogo/
fontes/tree/desafios.
10.2 U se a caixa de ferramentas para criar seus
próprios jogos
Duranteoscapítulos,construímosumcódigobaseparaauxiliarnodesen-
volvimentodosjogos. Emboraeletenhasidovistocomoparteintegralde
cadajogoemesmosendomuitobásico,vocêpodeusá-locomoumabiblio-
tecaàparteemseusprojetos,melhorandoocódigoexistenteecontribuindo
comnovosmétodosauxiliares:https://github.com/logicadojogo/fontes/tree/
master/base.
271
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 294

E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com

## Página 295

Capítulo11
Referênciasbibliográficas
DEITEL,H.M. Java:comoprogramar.6.ed.Trad.EdsonFurmankiewicz.
SãoPaulo:PearsonPrenticeHall,2005.
HARBOUR,JonathanS. Programação de games com Java. Trad. Carlos
EduardoSanti.SãoPaulo:CengageLearning,2010.
KENT,StevenL. The ultimate history of video games:fromPongtoPo-
kemon- Thestorybehindthecrazethattouchedourlivesandchangedthe
world.NewYork: ThreeRiversPress,2001.
MOOT,Tony. 1001 videogames para jogar antes de morrer.Trad.Liviade
Almeida.RiodeJaneiro:Sextante,2013.
NOVAK,Jeannie. Desenvolvimento de games.Trad.PedroCesardeConti.
SãoPaulo:CengageLearning,2010.
E-book gerado especialmente para JOSE DOS SANTOS CARVALHO NETO - santoscarvalhobs@gmail.com